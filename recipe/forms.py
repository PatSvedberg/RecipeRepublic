from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form to create a new recipe"""

    category = forms.ChoiceField(
        choices=Recipe.CATEGORY_CHOICES, widget=forms.RadioSelect, label="Category"
    )

    vegan = forms.ChoiceField(
        choices=Recipe.VEGAN_CHOICES, widget=forms.RadioSelect, label="Vegan"
    )

    publicity = forms.ChoiceField(
        choices=Recipe.PUBLICITY_CHOICES, widget=forms.RadioSelect, label="Publicity"
    )

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "instructions",
            "ingredients",
            "image",
            "category",
            "vegan",
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
        }
