'''
The admin interface for the Recipe, Ingredient, and RecipeIngredient models.
'''
from django.contrib import admin
from recipes.models import MeasurementUnit, Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class MeasurementUnitAdmin(admin.ModelAdmin):
    '''
    Admin interface for the MeasurementUnit model
    '''
    list_display = ('name', 'abbreviation')
    search_fields = ('name', 'abbreviation')
    ordering = ('name',)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'abbreviation'
                    )
                }
            ),
    )


# Create admin for Recipe model
class RecipeAdmin(admin.ModelAdmin):
    '''
    Admin interface for the Recipe model
    '''
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    inlines = [RecipeIngredientInline]
    readonly_fields = ('total_price',)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'cooking_instructions',
                    'total_price',
                    )
                }
            ),
    )


# Create admin for Ingredient model
class IngredientAdmin(admin.ModelAdmin):
    '''
    Admin interface for the Ingredient model
    '''
    list_display = ('name', 'measurement_unit', 'price_per_unit')
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'measurement_unit',
                    'price_per_unit'
                    )
                }
            ),
    )


# Register RecipeIngredient model
admin.site.register(MeasurementUnit, MeasurementUnitAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
