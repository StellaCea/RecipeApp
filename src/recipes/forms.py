from django import forms

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120)