from django.test import TestCase
from .models import Recipes
from .forms import RecipesSearchForm
# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipes.objects.create(name="Tea", cooking_time="5", ingredients=["water", "tea leaves", "sugar"], difficulty="easy")

    def test_recipe_name(self):
        recipe = Recipes.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_recipe_name_length(self):
        recipe = Recipes.objects.get(id=1)
        name_max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(name_max_length, 120)
    
    def test_difficulty(self):
        recipe = Recipes.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), "Easy")
    
    def test_get_absolute_url(self):
        recipe = Recipes.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/list/1")
    
class RecipeFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {'recipe_name': 'Test Recipe'}
        form = RecipesSearchForm(data = form_data)
        self.assertTrue(form.is_valid())

class RecipeViewAccessTest(TestCase):
    def recipe_view_login_required(self):
        url = reverse('recipes:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    
    def recipe_search_login_required(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)