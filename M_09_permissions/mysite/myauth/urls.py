from django.urls import path


from .views import (
    AboutMeView,
)

app_name = "accounts"

urlpatterns = [
    path("about-me/", AboutMeView.as_view(), name="about-me"),
]
