from django.views.generic import TemplateView, CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class Index(TemplateView):
    template_name = 'recipe/index.html'


class RecipeList(ListView):
    '''View Recipes as list'''
    template_name = 'recipe/recipe_list.html'
    model = Recipe
    context_object_name = 'recipes'


class NewRecipe(LoginRequiredMixin, CreateView):
    '''New Recipe View'''
    template_name = 'recipe/new_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = 'home'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewRecipe, self).form_valid(form)
