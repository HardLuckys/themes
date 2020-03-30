from django.shortcuts import render, redirect
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserUpdate, GetCode, LoginForm
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.views.generic import View, TemplateView
from .models import CustomUser, MyUserModel
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from .signup_backend import signup_back, time_code, get_degree
from datetime import datetime, timedelta

class SignUp(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def signup(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.user.is_authenticated:
        return redirect('themes:categories_list')
    else:
        if request.method == 'GET':
            form = CustomUserCreationForm()
            context = {
                'form': form
            }
            return render(request, 'users/signup.html', context)
        elif request.method == 'POST':
            bound_form = CustomUserCreationForm(request.POST, request.FILES)
            if bound_form.is_valid():
                bound_form.save()
                email = bound_form.cleaned_data.get('email')
                password = bound_form.cleaned_data.get('password1')

                auth_user = authenticate(request, email=email, password=password)
                login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')

                sign_back = signup_back(request)
                if sign_back == True:
                    return redirect('get_code')
                else:
                    return render(request, 'users/signup.html', context={'form': bound_form, 'error_mess': 'Error, please try again.'})
            return render(request, 'users/signup.html', context={'form': bound_form})


def get_code_view(request):
    if request.user.is_authenticated:
        coded = CustomUser.objects.get(slug=request.user.slug).is_coded
        if coded == True:
            return redirect('themes:categories_list')
        else:
            time_cod = time_code(request)
            if time_cod == True:
                form = GetCode()
                degree = get_degree(request)
                if request.method == 'GET':
                    context = {
                        'degree': degree,
                        'form': form
                    }
                    return render(request, 'users/get_code.html', context)
                elif request.method == 'POST':
                    bound_form = GetCode(request.POST)
                    if bound_form.is_valid():
                        code = bound_form.cleaned_data['url']
                        code_user = CustomUser.objects.get(slug=request.user.slug)
                        back_code = MyUserModel.objects.get(code_user=code_user).url
                        if code == back_code:
                            coded = CustomUser.objects.get(slug=request.user.slug)
                            coded.is_coded = True
                            coded.save()
                            MyUserModel.objects.get(url=back_code).delete()
                            return redirect('themes:categories_list')
                        else:
                            return render(request, 'users/get_code.html', context={'form': form, 'degree': degree, 'error_mess': 'Code is invalid. Try again.'})
                    return render(request, 'users/get_code.html', context={'form': bound_form, 'degree': degree})
            else:
                form = {}
                return render(request, 'users/get_code.html', context={'error_mess': 'Время кода вышло'})
    else:
        return redirect('signup')


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    logout(request)
    return HttpResponseRedirect('/')


def login_user(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.user.is_authenticated:
        return redirect('themes:categories_list')
    else:
        form = LoginForm()
        if request.method == 'GET':
            context = {
                'form': form
            }
            return render(request, 'users/login.html', context)
        elif request.method == 'POST':
            bound_form = LoginForm(request.POST)
            if bound_form.is_valid():
                email = bound_form.cleaned_data['email'] #bound_form.cleaned_data.get('email')
                password = bound_form.cleaned_data['password'] #bound_form.cleaned_data.get('password')
                if CustomUser.objects.filter(email=email).exists():
                    auth_user = authenticate(request, email=email, password=password)
                    try:
                        login(request, auth_user, backend='django.contrib.auth.backends.ModelBackend')
                        return HttpResponseRedirect(reverse('avataruser_detail', args=[request.user.slug]))
                    except:
                        return render(request, 'users/login.html', context={'form':bound_form, 'error_mess':'Неправильно введен пароль.'})
                else:
                    return render(request, 'users/login.html', context={'form':bound_form, 'error_mess':'Такого пользователя не существует.'})
            return render(request, 'users/login.html', context={'form':bound_form})


class CreateCodeView(View):
    def post(self, request):
        time_cod = time_code(request)
        if time_cod == False:
            signup_back(request)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('get_code')

    def get(self, request):
        return redirect('get_code')


class AvatarUserUpdateView(UpdateView):
    form_class = CustomUserUpdate
    model = CustomUser
    template_name = 'users/avataruser_edit.html'

    def dispatch(self, *args, **kwargs):
        coded = CustomUser.objects.get(slug=self.request.user.slug).is_coded
        if coded == True:
            return super().dispatch(*args, **kwargs)
        else:
            return redirect('get_code')

    def get_object(self, *args, **kwargs):
        obj = super(AvatarUserUpdateView, self).get_object(*args, **kwargs)
        if obj != self.request.user:
            raise PermissionDenied()
        return obj


class AvatarUserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/avataruser_detail.html'
    context_object_name = 'author'

    def dispatch(self, *args, **kwargs):
        coded = CustomUser.objects.get(slug=self.request.user.slug).is_coded
        if coded == True:
            return super().dispatch(*args, **kwargs)
        else:
            return redirect('get_code')


class AvatarUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/avataruser_delete.html'
    success_url = reverse_lazy('themes:categories_list')

    def get_object(self, *args, **kwargs):
        obj = super(AvatarUserDeleteView, self).get_object(*args, **kwargs)
        if obj != self.request.user:
            raise PermissionDenied()
        return obj
