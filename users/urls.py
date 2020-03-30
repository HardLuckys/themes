from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name = 'signup'),
    path('code/', views.get_code_view, name = 'get_code'),
    path('login/', views.login_user, name = 'login'),
    path('code_create/', views.CreateCodeView.as_view(), name = 'code_create'),
    path('code_create/', views.logout_view, name = 'logout'),
    path('id<str:slug>/', views.AvatarUserDetailView.as_view(), name = 'avataruser_detail'),
    path('id<str:slug>/edit/', views.AvatarUserUpdateView.as_view(), name = 'avataruser_edit'),
    path('id<str:slug>/delete/', views.AvatarUserDeleteView.as_view(), name = 'avataruser_delete'),
]
