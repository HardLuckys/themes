from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, MyUserModel
from django.forms import PasswordInput


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'about_me', 'avatar')

class CustomUserUpdate(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('about_me', 'avatar', 'username')

class GetCode(forms.ModelForm):
    class Meta:
        model = MyUserModel
        fields = ('url', )

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput())
