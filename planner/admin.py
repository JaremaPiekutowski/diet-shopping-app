from django.contrib import admin

from .models import Day, Plan, PlanDay


class PlanDayInline(admin.TabularInline):
    model = PlanDay
    extra = 1


# Create admin for Day model
class DayAdmin(admin.ModelAdmin):
    """
    Admin interface for the Day model
    """

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
