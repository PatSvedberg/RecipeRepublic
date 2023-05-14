from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'instructions',
        'ingredients',
        'image',
        'category',
        'publicity',
    )
    list_filter = ('category',)
