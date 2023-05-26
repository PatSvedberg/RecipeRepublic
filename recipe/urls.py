from django.urls import path
from .views import (
    Index,
    NewRecipe,
    RecipeList,
    RecipeDetail,
    DeleteRecipe,
    EditRecipe
)


urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("newrecipe/", NewRecipe.as_view(), name="new_recipe"),
    path("recipes/", RecipeList.as_view(), name="recipe_list"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_view"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path(
        "edit/<slug:pk>/",
        EditRecipe.as_view(),
        name="edit_recipe",
    ),
]
