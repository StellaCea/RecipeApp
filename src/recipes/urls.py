from django.urls import path
from .views import home, RecipesListView, RecipesDetailView, search

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipesListView.as_view(), name='list'),
    path('list/<pk>', RecipesDetailView.as_view(), name='detail'),
    path('recipes/', search, name='search')
]