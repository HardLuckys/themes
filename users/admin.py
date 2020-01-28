from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display = ['email', 'username', ]
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)