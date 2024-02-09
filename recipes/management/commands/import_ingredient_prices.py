import pandas as pd

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Imports ingredient prices from excel"

    def handle(self, *args, **kwargs):
        # Load the updated Excel file
        df = pd.read_excel('data_extraction/ingredient_prices.xlsx')

        # Update the ingredients with prices
        for index, row in df.iterrows():
            ingredient_name = row['name']
            price = row['price']
            print("Updating price for", ingredient_name, "to", price)
            # Find the ingredient and update its price
            try:
                ingredient = Ingredient.objects.get(name=ingredient_name)
            except Ingredient.DoesNotExist:
                print("Ingredient not found:", ingredient_name)
                continue
            ingredient.price_per_hundred_gram = price
            ingredient.save(update_fields=['price_per_hundred_gram'])
