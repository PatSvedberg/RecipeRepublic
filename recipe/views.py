from django.views.generic import (
    TemplateView, CreateView,
    ListView, DetailView, DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin,
    LoginRequiredMixin,
)

from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy

from django.db.models import Q


class Index(ListView):
    template_name = 'recipe/index.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        return self.model.objects.all()[:10]


class RecipeList(ListView):
    """View Recipes as list"""

    template_name = "recipe/recipe_list.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(category__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes



class RecipeDetail(DetailView):
    """Detailed view of recipe"""

    template_name = "recipe/recipe_veiw.html"
    model = Recipe
    context_object_name = "recipe"


class NewRecipe(LoginRequiredMixin, CreateView):
    """New Recipe View"""

    template_name = "recipe/new_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipe_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewRecipe, self).form_valid(form)


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''Delete Recipe'''
    model = Recipe
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        return self.request.user == self.get_object().user


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Edit Recipe'''
    template_name = "recipe/recipe_edit.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        return self.request.user == self.get_object().user