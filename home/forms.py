# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obligatorio. No puede ser repetido.')
    first_name = forms.CharField(max_length=30, required=True, label="Nombre/s")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido/s")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está en uso. Intenta otro.')
        return email