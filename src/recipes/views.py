from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'


def home(request):
    return render(request, 'recipes/home.html')
