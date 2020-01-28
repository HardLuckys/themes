from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserUpdate
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class AvatarUserUpdateView(UpdateView):
    form_class = CustomUserUpdate
    model = CustomUser
    #fields = ['username', 'avatar', 'name', 'surname', 'about_me', 'age', 'profile']
    template_name = 'users/avataruser_edit.html'

    def get_object(self, *args, **kwargs):
        obj = super(AvatarUserUpdateView, self).get_object(*args, **kwargs)
        if obj != self.request.user:
            raise PermissionDenied()
        return obj

class AvatarUserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/avataruser_detail.html'
    context_object_name = 'author'

class AvatarUserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/avataruser_delete.html'
    success_url = reverse_lazy('categories_list')

    def get_object(self, *args, **kwargs):
        obj = super(AvatarUserDeleteView, self).get_object(*args, **kwargs)
        if obj != self.request.user:
            raise PermissionDenied()
        return obj


class UserSubscribe(View):
    def post(self, request, user_id):
        user_id = int(user_id)
        if not request.user.Subs.filter(pk=user_id).exists():
            self.subscribe(user_id)
        else:
            self.unsubsribe(user_id)

        return redirect(request.META.get('HTTP_REFERER'))

    def subscribe(self, user_id):
        print('sub +1')
        CustomUser.objects.get(pk=user_id).user_members.add(self.request.user)

    def unsubsribe(self, user_id):
        print('sub -1')
        CustomUser.objects.get(pk=user_id).user_members.remove(self.request.user)
