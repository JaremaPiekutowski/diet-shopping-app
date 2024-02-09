import pandas as pd

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Exports ingredient names to excel"

    def handle(self, *args, **kwargs):
        # Fetch all ingredient names
        ingredients = Ingredient.objects.all().values_list('name', flat=True)

        # Create a DataFrame
        df = pd.DataFrame(list(ingredients), columns=['name'])

        # Save to Excel
        df.to_excel('data_extraction/ingredient_prices.xlsx', index=False)
