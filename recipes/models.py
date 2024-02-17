"""
Models for the Recipes app
"""

from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _


class Meal(models.TextChoices):
    """
    Choices for the meal field in the Recipe model
    """

    BREAKFAST = "breakfast", _("Breakfast")
    LUNCH = "lunch", _("Lunch")
    DINNER = "dinner", _("Dinner")
    SUPPER = "supper", _("Supper")


class IngredientCategory(models.TextChoices):
    """
    Categories of ingredients
    """

    FRUIT = "fruit", _("Fruit")
    VEGETABLES = "vegetables", _("Vegetables")
    BREAD = "bread", _("Bread")
    DAIRY = "dairy", _("Dairy")
    MEAT = "meat", _("Meat")
    FISH = "fish", _("Fish")
    FLOUR = "flour", _("Flour")
    TINNED = "tinned", _("Tinned")
    SPICES = "spices", _("Spices")
    OTHER = "other", _("Other")


class Recipe(models.Model):
    """
    Model for a recipe
    """

    title = models.CharField(max_length=100)
    meal = models.CharField(
        max_length=50,
        choices=Meal.choices,
        null=True,
        verbose_name=_("meal"),
    )
    cooking_instructions = models.TextField(
        verbose_name=_("cooking instructions"),
    )

    @property
    def total_price(self):
        total_price = sum(
            Decimal(str(ri.quantity_grams))
            * (ri.ingredient.price_per_hundred_gram / 100)
            for ri in self.recipeingredient_set.all()
            if ri.quantity_grams and ri.ingredient.price_per_hundred_gram
        )
        return round(total_price, 2)

    @property
    def total_calories(self):
        total_calories = sum(
            float(str(ri.quantity_grams))
            * (ri.ingredient.calories_per_hundred_gram / 100)
            for ri in self.recipeingredient_set.all()
            if ri.quantity_grams and ri.ingredient.calories_per_hundred_gram
        )
        return round(total_calories)

    @property
    def ingredients(self):
        all_ingredients = self.recipeingredient_set.all()
        return [f"{ri.ingredient} - {ri.quantity_grams} g" for ri in all_ingredients]

    def __str__(self):
        return f"({self.meal}){self.title}"


class Ingredient(models.Model):
    """
    Model for an ingredient
    """

    name = models.CharField(max_length=100, verbose_name=_("name"))
    category = models.CharField(
        max_length=50,
        choices=IngredientCategory.choices,
        null=True,
        blank=True,
        verbose_name=_("category"),
    )
    price_per_hundred_gram = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("price per 100 gram"),
    )
    calories_per_hundred_gram = models.FloatField(
        verbose_name=_("calories per 100 gram"),
    )
    other_measurement_unit = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("other measurement unit"),
    )
    grams_per_unit = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("grams per unit"),
    )

    @property
    def price_per_unit(self):
        return (
            self.price_per_hundred_gram / (100 / Decimal(self.grams_per_unit))
            if self.grams_per_unit
            else None
        )

    def __str__(self):
        if self.other_measurement_unit is not None:
            other_measurement_unit = self.other_measurement_unit
        else:
            other_measurement_unit = ""
        if self.grams_per_unit is not None:
            grams_per_unit = self.grams_per_unit
        else:
            grams_per_unit = ""
        return f"{self.name} ({other_measurement_unit}-{grams_per_unit} g)"


class RecipeIngredient(models.Model):
    """
    Model for the relationship between a recipe and its ingredients
    """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name=_("recipe"),
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name=_("ingredient"),
    )
    quantity_grams = models.FloatField(
        verbose_name=_("quantity grams"),
    )

    def __str__(self):
        return f"{self.recipe}: {self.ingredient.name} - {self.quantity_grams} g"
