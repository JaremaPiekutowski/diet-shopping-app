# Generated by Django 4.1.6 on 2024-02-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0007_alter_ingredient_grams_per_unit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="quantity_grams",
            field=models.FloatField(verbose_name="quantity grams"),
        ),
    ]
