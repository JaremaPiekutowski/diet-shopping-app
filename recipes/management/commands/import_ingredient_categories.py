import pandas as pd

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Imports ingredient categories from excel"

    def handle(self, *args, **kwargs):
        # Load the updated Excel file
        df = pd.read_excel("data_extraction/categories.xlsx")

        # Update the ingredients with prices
        for index, row in df.iterrows():
            ingredient_name = row["name"]
            category = row["category"]
            print("Updating category for", ingredient_name, "to", category)
            # Find the ingredient and update its price
            try:
                ingredient = Ingredient.objects.get(name=ingredient_name)
            except Ingredient.DoesNotExist:
                print("Ingredient not found:", ingredient_name)
                continue
            ingredient.category = category
            ingredient.save(update_fields=["category"])
