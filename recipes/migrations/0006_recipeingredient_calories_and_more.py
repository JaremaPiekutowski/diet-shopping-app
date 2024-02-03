# Generated by Django 4.1.6 on 2024-02-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0005_rename_quantity_recipeingredient_quantity_grams_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipeingredient",
            name="calories",
            field=models.FloatField(null=True, verbose_name="calories"),
        ),
        migrations.AddField(
            model_name="recipeingredient",
            name="other_unit",
            field=models.CharField(max_length=50, null=True, verbose_name="other unit"),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="other_measurement_unit",
            field=models.CharField(
                max_length=50, null=True, verbose_name="other measurement unit"
            ),
        ),
        migrations.DeleteModel(
            name="MeasurementUnit",
        ),
    ]
