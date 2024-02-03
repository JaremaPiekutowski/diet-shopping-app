from django.db import models

from recipes.models import Recipe


# Create your models here.
class Day(models.Model):
    '''
    Model for a day diet plan
    '''
    date = models.DateField()
    breakfast = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name='breakfast',
        null=True,
        blank=True,
    )
    lunch = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name='lunch',
        null=True,
        blank=True,
    )
    dinner = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name='dinner',
        null=True,
        blank=True,
    )
    supper = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name='supper',
        null=True,
        blank=True,
    )

    @property
    def weekday(self):
        return self.date.strftime('%A')

    @property
    def total_price(self):
        meals = [self.breakfast, self.lunch, self.dinner, self.supper]
        total_price = sum(
            meal.total_price
            for meal in meals
            if meal
        )
        # TODO: Handle no price in any meal
        return total_price

    @property
    def total_calories(self):
        meals = [self.breakfast, self.lunch, self.dinner, self.supper]
        total_calories = sum(
            meal.total_calories
            for meal in meals
            if meal
        )
        # TODO: Handle no calories in any meal (shouldn't be so!)
        return total_calories

    def __str__(self):
        return f"Menu for {self.date}"
