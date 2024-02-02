'''
This file is used to configure the recipes app.
It is used to define the default_auto_field and the name of the app.
'''
from django.apps import AppConfig


class RecipesConfig(AppConfig):
    '''
    Configuration for the Recipes app
    '''
    default_auto_field = "django.db.models.BigAutoField"
    name = "recipes"
