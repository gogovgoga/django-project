from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import (
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    get_session_view,
    MyLogoutView,
    AboutMeView,
    RegisterView,
    FooBarView,
    UserListView,
    UserDetailView,
    UserUpdateView,
)

app_name = 'accounts'

urlpatterns = [
    path("login/",
         LoginView.as_view(
             template_name="accounts/login.html",
             redirect_authenticated_user=True,
         ),
         name="login"
         ),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),

    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),

    path("session/set/", set_session_view, name="session-set"),
    path("session/get/", get_session_view, name="session-get"),

    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),

    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='profile_update'),
]
