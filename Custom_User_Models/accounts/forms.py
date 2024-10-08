from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "gender", "email", "password1", "password2"]
