from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'about_me', 'avatar')

class CustomUserUpdate(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'about_me', 'avatar')
