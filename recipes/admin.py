"""
The admin interface for the Recipe, Ingredient, and RecipeIngredient models.
"""

from django.contrib import admin
from recipes.models import Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


# Create admin for Recipe model
class RecipeAdmin(admin.ModelAdmin):
    """
    Admin interface for the Recipe model
    """

    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)
    inlines = [RecipeIngredientInline]
    readonly_fields = ("total_price",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "cooking_instructions",
                    "total_price",
                )
            },
        ),
    )


# Create admin for Ingredient model
class IngredientAdmin(admin.ModelAdmin):
    """
    Admin interface for the Ingredient model
    """

    list_display = (
        "name",
        "price_per_hundred_gram",
        "other_measurement_unit",
        "grams_per_unit",
        "price_per_unit",
    )
    search_fields = ("name",)
    ordering = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "price_per_hundred_gram",
                    "other_measurement_unit",
                    "grams_per_unit",
                    "price_per_unit",
                )
            },
        ),
    )


# Register RecipeIngredient model
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
