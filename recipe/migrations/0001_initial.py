# Generated by Django 3.2.19 on 2023-05-14 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                ("description", models.CharField(max_length=500)),
                (
                    "instructions",
                    djrichtextfield.models.RichTextField(max_length=10000),
                ),
                ("ingredients", djrichtextfield.models.RichTextField(max_length=10000)),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="recipes/",
                    ),
                ),
                ("image_alt", models.CharField(max_length=200)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("food", "Food"),
                            ("drink", "Drink"),
                            ("other", "Other"),
                        ],
                        default="food",
                        max_length=50,
                    ),
                ),
                (
                    "publicity",
                    models.CharField(
                        choices=[("private", "Private"), ("public", "Public")],
                        default="private",
                        max_length=50,
                    ),
                ),
                ("post_date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-post_date"],
            },
        ),
    ]
