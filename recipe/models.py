from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choises
CATEGORY = (("food", "Food"), ("drink", "Drink"), ("other", "Other"))
PUBLICITY = (("private", "Private"), ("public", "Public"))


class Recipe(models.Model):
    """
    Recipe model
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    category = models.CharField(max_length=50, choices=CATEGORY, default="food")
    publicity = models.CharField(max_length=50, choices=PUBLICITY, default="private")
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return str(self.title)
