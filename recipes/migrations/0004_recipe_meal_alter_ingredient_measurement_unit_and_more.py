# Generated by Django 4.1.6 on 2024-02-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0003_measurementunit_alter_ingredient_price_per_unit_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="meal",
            field=models.CharField(
                choices=[
                    ("breakfast", "Breakfast"),
                    ("lunch", "Lunch"),
                    ("dinner", "Dinner"),
                    ("supper", "Supper"),
                ],
                max_length=50,
                null=True,
                verbose_name="meal",
            ),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="measurement_unit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="recipes.measurementunit",
                verbose_name="measurement unit",
            ),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=100, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="price_per_unit",
            field=models.DecimalField(
                decimal_places=2, max_digits=5, null=True, verbose_name="price per unit"
            ),
        ),
        migrations.AlterField(
            model_name="measurementunit",
            name="abbreviation",
            field=models.CharField(
                max_length=10, unique=True, verbose_name="abbreviation"
            ),
        ),
        migrations.AlterField(
            model_name="measurementunit",
            name="description",
            field=models.TextField(blank=True, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="measurementunit",
            name="name",
            field=models.CharField(max_length=50, unique=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cooking_instructions",
            field=models.TextField(verbose_name="cooking instructions"),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.ingredient",
                verbose_name="ingredient",
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="quantity",
            field=models.FloatField(verbose_name="quantity"),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.recipe",
                verbose_name="recipe",
            ),
        ),
    ]