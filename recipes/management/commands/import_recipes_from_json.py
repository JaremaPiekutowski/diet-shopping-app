import json
import re
from django.core.management.base import BaseCommand
from recipes.models import Recipe, Ingredient, RecipeIngredient, Meal


NOMINATIVE_MAP = {
    "butelek": "butelka",
    "butelki": "butelka",
    "garści": "garść",
    "kawałki": "kawałek",
    "kawałków": "kawałek",
    "kostek": "kostka",
    "kostki": "kostka",
    "kromek": "kromka",
    "kromki": "kromka",
    "kubka": "kubek",
    "kubków": "kubek",
    "liścia": "liść",
    "liście": "liść",
    "liści": "liść",
    "listka": "listek",
    "listków": "listek",
    "listki": "listek",
    "łodyg": "łodyga",
    "łodygi": "łodyga",
    "opakowań": "opakowanie",
    "opakowania": "opakowanie",
    "paczek": "paczka",
    "paczki": "paczka",
    "pasków": "pasek",
    "paski": "pasek",
    "plastra": "plaster",
    "plastry": "plaster",
    "porcji": "porcja",
    "porcje": "porcja",
    "puszki": "puszka",
    "puszek": "puszka",
    "różyczek": "różyczka",
    "różyczki": "różyczka",
    "szklanek": "szklanka",
    "szklanki": "szklanka",
    "szt": "sztuka",
    "sztuk": "sztuka",
    "sztuki": "sztuka",
    "woreczka": "woreczek",
    "woreczków": "woreczek",
    "ząbka": "ząbek",
    "ząbki": "ząbek",
    "ząbków": "ząbek",
    "łyżeczki": "łyżeczka",
    "łyżki": "łyżka",
    "łyżeczek": "łyżeczka",
    "łyżek": "łyżka",
}


class Command(BaseCommand):
    help = "Loads recipes from a JSON file into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file", type=str, help="Path to the JSON file containing the recipes"
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs["json_file"]
        with open(file_path, "r", encoding="utf-8") as file:
            recipes = json.load(file)
            for recipe_data in recipes:
                self.create_recipe(recipe_data)

    def get_meal(self, meal_number):
        meals = {
            1: Meal.BREAKFAST,
            2: Meal.LUNCH,
            3: Meal.DINNER,
            4: Meal.SUPPER,
        }
        return meals.get(meal_number, Meal.BREAKFAST)

    def to_nominative(self, item):
        words = item.split()
        if len(words) > 0:
            last_word = words[-1]
            return NOMINATIVE_MAP.get(last_word, last_word)
        return ""

    def create_recipe(self, recipe_data):
        print("Processing recipe: ", recipe_data["name"])
        # Create or get the Recipe object
        recipe, created = Recipe.objects.get_or_create(
            title=recipe_data["name"],
            defaults={
                'meal': self.get_meal(recipe_data["meal_number"]),
                'cooking_instructions': recipe_data["cooking_instructions"]
                }
        )
        if not created:
            # Update meal and cooking_instructions if recipe already exists
            recipe.meal = self.get_meal(recipe_data["meal_number"])
            recipe.cooking_instructions = recipe_data["cooking_instructions"]
            recipe.save()

        for ingredient_data in recipe_data["ingredients"]:
            units = re.findall(r"\b\w+\b", ingredient_data.get("unit", ""))
            other_measurement_unit = units[-1] if units else ""
            nominative_unit = self.to_nominative(other_measurement_unit)

            # Check if ingredient exists
            calories = ingredient_data.get("calories")
            if calories is None:
                calories = 0
            grams = ingredient_data.get("grams")
            if grams is None:
                grams = 0
            ingredient, created = Ingredient.objects.get_or_create(
                name=ingredient_data["name"],
                defaults={
                    'calories_per_hundred_gram': calories * (100 / grams),
                    'other_measurement_unit': nominative_unit
                    }
            )
            if not created:
                # Update existing ingredient
                ingredient.calories_per_hundred_gram = calories * (100 / grams)
                ingredient.other_measurement_unit = nominative_unit
                ingredient.save()

            # Create RecipeIngredient
            RecipeIngredient.objects.get_or_create(
                recipe=recipe,
                ingredient=ingredient,
                defaults={'quantity_grams': ingredient_data["grams"]}
            )
