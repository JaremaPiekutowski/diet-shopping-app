'''
Models for the Recipes app
'''
from decimal import Decimal

from django.db import models


class MeasurementUnit(models.Model):
    '''
    Model for storing measurement units of ingredients
    '''
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class Recipe(models.Model):
    '''
    Model for a recipe
    '''
    title = models.CharField(max_length=100)
    cooking_instructions = models.TextField()

    @property
    def total_price(self):
        total_price = sum(
            Decimal(str(ri.quantity)) * ri.ingredient.price_per_unit
            for ri in self.recipeingredient_set.all()
        )
        return f"{total_price:.2f} PLN"

    def __str__(self):
        return f"{self.title}"


class Ingredient(models.Model):
    '''
    Model for an ingredient
    '''
    name = models.CharField(max_length=100)
    measurement_unit = models.ForeignKey(
        MeasurementUnit,
        on_delete=models.SET_NULL,  # TODO: are we sure?
        null=True,  # TODO: are we sure?
        )
    price_per_unit = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,  # TODO: are we sure?
        )

    def __str__(self):
        return f"{self.name} ({self.measurement_unit.abbreviation})"


class RecipeIngredient(models.Model):
    '''
    Model for the relationship between a recipe and its ingredients
    '''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return (
            f"{self.recipe} - "
            f"{self.ingredient.name}({self.ingredient.measurement_unit.abbreviation}) - "
            f"{self.quantity}"
        )
