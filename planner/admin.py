from django import forms
from django.contrib import admin
from django.db.models import Case, IntegerField, Value, When

from .models import Day, Plan, PlanDay
from recipes.models import Recipe


class DayAdminForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DayAdminForm, self).__init__(*args, **kwargs)

        meal_order = ["breakfast", "lunch", "dinner", "supper"]

        # Create a mapping of meal to a custom sort order
        ordering = Case(
            *[When(meal=meal, then=Value(i)) for i, meal in enumerate(meal_order)],
            output_field=IntegerField()
        )

        # Apply the custom ordering
        recipes = Recipe.objects.annotate(custom_order=ordering).order_by(
            "custom_order", "title"
        )

        # Convert to list of IDs to preserve order in subsequent query
        ordered_ids = list(recipes.values_list("id", flat=True))

        # Retrieve the recipes in the custom order using the preserved IDs
        preserved_order = Case(
            *[When(pk=pk, then=pos) for pos, pk in enumerate(ordered_ids)],
            output_field=IntegerField()
        )
        ordered_recipes = Recipe.objects.filter(pk__in=ordered_ids).order_by(
            preserved_order
        )

        for meal in meal_order:
            self.fields[meal].queryset = ordered_recipes


class PlanDayInline(admin.TabularInline):
    model = PlanDay
    extra = 1


# Create admin for Day model
class DayAdmin(admin.ModelAdmin):
    """
    Admin interface for the Day model
    """

    form = DayAdminForm
    list_display = ("date_formatted",)
    ordering = ("date",)
    readonly_fields = ("date_formatted", "total_price", "total_calories")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "date",
                    "breakfast",
                    "lunch",
                    "dinner",
                    "supper",
                    "total_price",
                    "total_calories",
                )
            },
        ),
    )


class PlanAdmin(admin.ModelAdmin):
    """
    Admin interface for the Plan model
    """

    list_display = (
        "date_start",
        "date_end",
    )
    inlines = [PlanDayInline]
    readonly_fields = (
        "date_start",
        "date_end",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "date_start",
                    "date_end",
                )
            },
        ),
    )


admin.site.register(Plan, PlanAdmin)
admin.site.register(Day, DayAdmin)
