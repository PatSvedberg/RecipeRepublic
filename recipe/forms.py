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

    ingredients = forms.CharField(widget=RichTextWidget())
    instructions = forms.CharField(widget=RichTextWidget())

    title = forms.CharField(label="Title")
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5}), label="Description"
    )
    image = forms.ImageField(label="Image")

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "category",
            "vegan",
            "publicity",
        ]
