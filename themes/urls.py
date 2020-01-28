from django.urls import path
from . import views

app_name = 'themes'

urlpatterns = [
    path('', views.categories_list, name = 'categories_list'),
    path('categories/', views.CategoriesListView.as_view(), name = 'categories_all'),
    path('category/<int:categories_pk>/', views.category, name = 'category'),
    path('category/<int:categories_pk>/<int:exercises_pk>/', views.exercise, name = 'exercise'),
]
