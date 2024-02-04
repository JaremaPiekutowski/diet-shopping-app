"""
Model for diet plans
"""

from django.db import models

from recipes.models import Recipe


class Day(models.Model):
    """
    Model for a day diet plan
    """

    date = models.DateField()
    breakfast = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name="breakfast",
        null=True,
        blank=True,
    )
    lunch = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name="lunch",
        null=True,
        blank=True,
    )
    dinner = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name="dinner",
        null=True,
        blank=True,
    )
    supper = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        related_name="supper",
        null=True,
        blank=True,
    )

    @property
    def date_formatted(self):
        return self.date.strftime("%d %B %Y, %A")

    @property
    def total_price(self):
        meal_prices = [
            float(meal.total_price)
            for meal in [self.breakfast, self.lunch, self.dinner, self.supper]
            if meal is not None
        ]
        total_price = sum(meal_prices)
        print(total_price)
        return total_price

    @property
    def total_calories(self):
        meals = [self.breakfast, self.lunch, self.dinner, self.supper]
        total_calories = sum(meal.total_calories for meal in meals if meal is not None)
        return total_calories

    def __str__(self):
        return f"Menu for {self.date_formatted}"


class Plan(models.Model):
    """
    Model for a diet plan
    """

    @property
    def total_price(self):
        return sum(day.total_price for day in self.days.all())

    @property
    def date_start(self):
        return self.planday_set.all().order_by("day__date").first().day

    @property
    def date_end(self):
        return self.planday_set.all().order_by("day__date").last().day

    # # TODO doesn't work
    # def __str__(self):
    #     return f"{self.date_start} - {self.date_end}"


class PlanDay(models.Model):
    """
    Model for a day in a diet plan
    """

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.plan.id} - {self.day.date_formatted}"
