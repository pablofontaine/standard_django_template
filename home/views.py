from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView(TemplateView):
    template_name = "home/home_index.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = AuthenticationForm
    form_class = AuthenticationForm
    redirect_authenticated_user = True


class SingupView(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home:login")


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "home/profile.html"
    model = User


class PersonalizedPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/password_change.html"

    def get_success_url(self):
        user_id = self.request.user.id
        success_url = reverse("home:profile", kwargs={'pk': user_id})
        return success_url

