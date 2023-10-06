from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes

# Create your views here.
class RecipesListView(ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class RecipesDetailView(DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'


def home(request):
    return render(request, 'recipes/home.html')
