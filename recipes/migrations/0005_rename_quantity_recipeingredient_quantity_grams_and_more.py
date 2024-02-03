# Generated by Django 4.1.6 on 2024-02-03 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0004_recipe_meal_alter_ingredient_measurement_unit_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipeingredient",
            old_name="quantity",
            new_name="quantity_grams",
        ),
        migrations.RemoveField(
            model_name="ingredient",
            name="measurement_unit",
        ),
        migrations.AddField(
            model_name="ingredient",
            name="grams_per_unit",
            field=models.FloatField(null=True, verbose_name="grams per unit"),
        ),
        migrations.AddField(
            model_name="ingredient",
            name="other_measurement_unit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="recipes.measurementunit",
                verbose_name="other measurement unit",
            ),
        ),
        migrations.AddField(
            model_name="ingredient",
            name="price_per_hundred_gram",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="price per 100 gram",
            ),
        ),
    ]