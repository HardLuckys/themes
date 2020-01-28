from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUp.as_view(), name = 'signup'),
    path('id<str:slug>/', views.AvatarUserDetailView.as_view(), name = 'avataruser_detail'),
    path('id<str:slug>/edit/', views.AvatarUserUpdateView.as_view(), name = 'avataruser_edit'),
    path('id<str:slug>/delete/', views.AvatarUserDeleteView.as_view(), name = 'avataruser_delete'),
]
