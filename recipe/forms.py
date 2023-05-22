from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form to create new recipe"""

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "instructions",
            "ingredients",
            "image",
            "category",
            "publicity",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Image",
            "category": "Category Type",
            "publicity": "Publicity",
        }
