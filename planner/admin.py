from django.contrib import admin

from .models import Day


# Create admin for Day model
class DayAdmin(admin.ModelAdmin):
    """
    Admin interface for the Day model
    """

    list_display = ("date", "weekday")
    ordering = ("date",)
    readonly_fields = ("total_price", "total_calories")
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


admin.site.register(Day, DayAdmin)
