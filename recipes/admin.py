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
    readonly_fields = ("total_price", "total_calories")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "cooking_instructions",
                    "total_price",
                    "total_calories",
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
        "category",
        "price_per_hundred_gram",
        "calories_per_hundred_gram",
        "other_measurement_unit",
        "grams_per_unit",
    )
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("price_per_unit",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "category",
                    "price_per_hundred_gram",
                    "calories_per_hundred_gram",
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
