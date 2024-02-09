"""
The admin interface for the Recipe, Ingredient, and RecipeIngredient models.
"""

from django.contrib import admin
from django.utils.html import format_html

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
    ordering = ("meal",)
    inlines = [RecipeIngredientInline]
    readonly_fields = ("total_price", "total_calories")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "meal",
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
        "formatted_price",
        "formatted_calories",
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

    def formatted_price(self, obj):
        return round(obj.price_per_hundred_gram, 2)

    def formatted_calories(self, obj):
        return round(obj.calories_per_hundred_gram)

    formatted_price.short_description = 'Price'
    formatted_price.admin_order_field = 'price_per_hundred_gram'
    formatted_calories.short_description = 'Calories'
    formatted_calories.admin_order_field = 'calories_per_hundred_gram'


# Register RecipeIngredient model
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
