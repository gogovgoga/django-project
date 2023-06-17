from timeit import default_timer

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import OrderForm, GroupForm, ProductForm
from shopapp.models import Product, Order, ProductImage


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = Product.objects.all()
        context = {
            'time_running': default_timer(),
            'products': products,
            'items': 2,
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm(),
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class ProductDetailsView(DetailView):
    template_name = 'shopapp/products-details.html'
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shopapp:products_list")

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        elif self.request.user.has_perm("shopapp.add_product"):
            return True
        else:
            raise PermissionDenied

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    # fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"
    form_class = ProductForm

    def get_success_url(self):
        return reverse('shopapp:product_details', kwargs={'pk': self.object.pk})

    def test_func(self):
        product = self.get_object()
        return self.request.user.is_superuser or (
                self.request.user.has_perm('shopapp.change_product') and product.created_by == self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image,
            )
        return response


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related('products')
    )


class OrderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    template_name = 'shopapp/order_detail.html'
    context_object_name = 'order'
    permission_required = 'shopapp.view_order'

    def has_permission(self):
        return super().has_permission() and self.get_object().user == self.request.user

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.object.user
    #     context['products'] = self.object.products.all()
    #     return context
    #
    # def get_success_url(self):
    #     return reverse_lazy('shopapp:order_list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('shopapp:order_list')
    template_name = 'shopapp/order_create.html'


class OrderUpdateView(UpdateView):
    model = Order
    fields = "delivery_address", "promo_code", "user", "products"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:order_detail",
            kwargs={"pk": self.object.pk},
        )


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('shopapp:order_list')
    template_name = 'shopapp/order_delete.html'
    context_object_name = 'order'


class OrdersExportView(PermissionRequiredMixin, UserPassesTestMixin, View):
    permission_required = 'shopapp.view_order'

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        if not self.has_permission() or not self.test_func():
            raise PermissionDenied

        orders = Order.objects.all()
        orders_data = []
        for order in orders:
            order_data = {
                'order_id': order.id,
                'address': order.delivery_address,
                'promo_code': order.promo_code,
                'user_id': order.user.id,
                'product_ids': [product.id for product in order.products.all()]
            }
            orders_data.append(order_data)
        return JsonResponse({'orders': orders_data})
