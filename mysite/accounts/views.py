from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.utils.translation import gettext_lazy as _, ngettext

from accounts.forms import ProfileForm
from accounts.models import Profile


class HelloView(View):
    welcome_message = _("welcome hello world!")

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get("items") or 0
        items = int(items_str)
        products_line = ngettext(
            "one product",
            "{count} products",
            items
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f"<h1>{self.welcome_message}</h1>"
            f"\n<h2>{products_line}</h2>"
        )


class AboutMeView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/about-me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            profile = user.profile
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=user)

        context['user'] = user
        context['profile'] = profile

        if 'form' not in context:
            context['form'] = ProfileForm(instance=profile)

        return context

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:about-me')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default_value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("accounts.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'accounts/user_list.html', {'users': users})


class UserDetailView(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'

    def test_func(self):
        user = self.request.user
        return user.is_staff or user == self.get_object().profile.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        context['user'] = self.get_object()
        return context

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет разрешения на просмотр этой страницы.")


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'accounts/user_update.html'
    fields = ['avatar', ]

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        user = self.request.user
        profile_user = self.get_object().user
        return user.is_staff or user == profile_user
