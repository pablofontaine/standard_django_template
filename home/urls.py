from django.urls import include, path
from .views import (
    HomeView,
    SingupView,
    ProfileView,
    PersonalizedPasswordChangeView
    )

app_name = "home"
urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("accounts/password_change/", PersonalizedPasswordChangeView.as_view(), name="password_change"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/singup/", SingupView.as_view(), name="singup"),
    path("accounts/profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
