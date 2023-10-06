from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField()
    ingredients = models.TextField()
    difficulty = models.CharField(max_length=120)
    pic = models.ImageField(upload_to="recipes", default="no_picture.png")

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) <= 4:
            difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients) > 4:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients) <= 4:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients) > 4:
            difficulty = "Hard"
        return difficulty

    def ingredient_list(self):
        if self.ingredients=="":
            return []
        return self.ingredients.split(", ")
    
    def numb_of_ingredients(self):
        return len(self.ingredient_list())

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})