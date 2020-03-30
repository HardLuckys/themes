from django.shortcuts import render, get_object_or_404, redirect
from .models import Categories, Exercises
from .forms import ExerciseCreateForm, CategoriesCreateForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import Q
from users.models import CustomUser

def categories_list(request):
    if request.user.is_authenticated:
        coded = CustomUser.objects.get(slug=request.user.slug).is_coded
        if coded == True:
            categories = Categories.objects.all()[:10]
            form = CategoriesCreateForm()
            if request.method == 'GET':
                context = {
                    'categories': categories,
                    'form': form,
                }
                return render(request, 'base.html', context)
            elif request.method == 'POST':
                author = request.user
                bound_form = CategoriesCreateForm(request.POST, request.FILES)
                categories = list(categories)
                if bound_form.is_valid():
                    bound_form.instance.categories = categories
                    bound_form.instance.author = author
                    new_category = bound_form.save()
                    categories.append(new_category)
                    return redirect(new_category.get_absolute_url())
                return render(request, 'base.html', context={'categories': categories, 'form': bound_form})
        else:
            return redirect('get_code')
    else:
        return HttpResponseRedirect('/users/login/')


def category(request, categories_pk=None, **kwargs):
    if request.user.is_authenticated:
        coded = CustomUser.objects.get(slug=request.user.slug).is_coded
        if coded == True:
            categories = Categories.objects.all()[:10]
            category = get_object_or_404(Categories, pk=categories_pk)
            exercises = Exercises.objects.filter(categories=category)
            form = ExerciseCreateForm()
            if request.method == 'GET':
                context = {
                    'categories': categories,
                    'category': category,
                    'exercises': exercises,
                    'form':form,
                }
                return render(request, 'category.html', context)
            elif request.method == 'POST':
                author = request.user
                bound_form = ExerciseCreateForm(request.POST, request.FILES)
                exercises = list(exercises)
                if bound_form.is_valid():
                    bound_form.instance.author = author
                    bound_form.instance.categories = category
                    new_exercise = bound_form.save()
                    exercises.append(new_exercise)
                    return redirect(category)
                return render(request, 'category.html', context={'categories': categories, 'category': category, 'exercises': exercises, 'form': bound_form,})
        else:
            return redirect('get_code')
    else:
        return HttpResponseRedirect('/users/login/')


def exercise(request, exercises_pk=None, **kwargs):
    if request.user.is_authenticated:
        coded = CustomUser.objects.get(slug=request.user.slug).is_coded
        if coded == True:
            exercise = Exercises.objects.get(pk=exercises_pk)
            categories = Categories.objects.all()
            if request.method == 'GET':
                context = {
                    'exercise': exercise,
                    'categories': categories,
                }
                return render(request, 'item_detail.html', context)
        else:
            return redirect('get_code')
    else:
        return HttpResponseRedirect('/users/login/')

class CategoriesListView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            coded = CustomUser.objects.get(slug=self.request.user.slug).is_coded
            if coded == True:
                search_query = request.GET.get('search', '')
                if search_query:
                    categories = Categories.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
                else:
                    categories = Categories.objects.all()
                context = {
                    'categories': categories,
                }
                return render(request, 'categories_all.html', context)
            else:
                return redirect('get_code')
        else:
            return HttpResponseRedirect('/users/login/')
