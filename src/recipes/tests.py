from django.test import TestCase
from .models import Recipes

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