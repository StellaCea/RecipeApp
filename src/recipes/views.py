from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart

# Create your views here.
class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipes
    template_name = 'recipes/main.html'

class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'

def home(request):
    return render(request, 'recipes/home.html')

@login_required
#define function-based view
def search(request):
    #create an instance of RecipesSearchForm
    form = RecipesSearchForm(request.POST or None)
    recipes = None
    recipes_df = None #initialize dataframe to None
    chart1 = None
    chart2 = None
    chart3 = None

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        #apply filter to extract data
        qs = Recipes.objects.filter(name__icontains=recipe_name)

        if qs:
            recipes = qs
            #convert the queryset values to pandas df
            recipes_df=pd.DataFrame(qs.values())
            
            #chart1
            chart1 = get_chart("plot", recipes_df)

            #chart2
            chart2_data = {
                "difficulty": ["Easy", "Medium", "Intermediate", "Hard"],
                "count": [0, 0, 0, 0]
            }
            for recipe in recipes:
                difficulty = recipe.calculate_difficulty()
                if difficulty in chart2_data["difficulty"]:
                    index = chart2_data["difficulty"].index(difficulty)
                    chart2_data["count"][index] += 1
            
            #filter out labels and counts with a count of 0
            filtered_labels = []
            filtered_counts = []
            for label, count in zip(chart2_data["difficulty"], chart2_data["count"]):
                if count > 0:
                    filtered_labels.append(label)
                    filtered_counts.append(count)
            
            #create new disctionary with filtered data
            filtered_chart2_data = {
                "difficulty": filtered_labels,
                "count": filtered_counts,
            }

            chart2 = get_chart("pie", filtered_chart2_data, labels=filtered_labels)

            #chart3
            chart3_data = {
                "name": [recipe.name for recipe in recipes],
                "nr_ingredients": [recipe.numb_of_ingredients() for recipe in recipes]
            }
            chart3 = get_chart("bar", chart3_data)

            #recipes_df=recipes_df.to_html()

    #pack up data to be sent to template in the context dictionary
    context={
        'form':form,
        'recipes': recipes,
        'chart1': chart1,
        'chart2': chart2,
        'chart3': chart3
    }
    #load the record.html page using the data
    return render(request, 'recipes/search.html', context)
