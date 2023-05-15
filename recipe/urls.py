from django.urls import path
from .views import Index, NewRecipe, RecipeList, RecipeDetail

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("newrecipe/", NewRecipe.as_view(), name="new_recipe"),
    path("recipes/", RecipeList.as_view(), name="recipe_list"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_view"),
]
