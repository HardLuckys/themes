from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser, MyUserModel

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display = ['email', 'username', 'is_coded']
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MyUserModel)
