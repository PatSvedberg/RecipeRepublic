from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin,
    LoginRequiredMixin,
)

from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q


class Index(ListView):
    template_name = "recipe/index.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return self.model.objects.all()[:10]


class RecipeList(ListView):
    """View Recipes as list"""

    template_name = "recipe/recipe_list.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category=category)

        vegan = self.request.GET.get("vegan")
        if vegan == "yes":
            queryset = queryset.filter(vegan=vegan)

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(instructions__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = context["recipes"]
        paginator = Paginator(recipes, self.paginate_by)

        page_number = self.request.GET.get("page")
        recipes = paginator.get_page(page_number)

        context["recipes"] = recipes
        return context


class RecipeDetail(DetailView):
    """Detailed view of recipe"""

    template_name = "recipe/recipe_view.html"
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
    """Delete Recipe"""

    model = Recipe
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        return self.request.user == self.get_object().user


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit Recipe"""

    template_name = "recipe/recipe_edit.html"
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        return self.request.user == self.get_object().user
