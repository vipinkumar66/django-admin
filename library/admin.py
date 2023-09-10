from django.contrib import admin
from .models import Profile
# Register your models here.

# class LibraryAdminArea(admin.AdminSite):
#     site_header = "Library Admin Area"

# library_admin = LibraryAdminArea(name="LibraryAdmin")


from django.contrib import admin

class EmailFilter(admin.SimpleListFilter):
    """
    Custom Django admin list filter to filter records based on the presence or absence of user email.

    This filter provides two options: "has_email" and "no_email".
    """

    # Human-readable title displayed in the admin interface.
    title = "Email Filter"

    # Name of the query parameter used in the URL.
    parameter_name = "user_email"

    def lookups(self, request, model_admin):
        """
        Define the filter options presented to the user.

        Returns:
            list of tuple: Each tuple contains a filter value and a human-readable label.
        """
        return (
            ("has_email", "Has Email"),
            ("no_email", "No Email")
        )

    def queryset(self, request, queryset):
        """
        Apply the selected filter option to the queryset.

        Args:
            request: The HTTP request object.
            queryset: The queryset of model instances to filter.

        Returns:
            queryset: The filtered queryset.
        """
        # Check if a filter value is selected; if not, return the unfiltered queryset.
        if not self.value():
            return queryset

        # Apply filtering based on the selected filter option.
        if self.value().lower() == "has_email":
            # Exclude records where the user's email field is empty.
            return queryset.exclude(user__email="")

        if self.value().lower() == "no_email":
            # Filter records where the user's email field is empty.
            return queryset.filter(user__email="")

# Usage:
# Add this filter to your admin view for the desired model.
# It will provide a filter option in the admin interface.



class Filter(admin.ModelAdmin):
    list_display = ("id", "email", "created_at", "role", "is_active")
    list_filter = ("is_active", "role","created_at",EmailFilter)
    # exclude = ("created_at",)

    # def email(self, obj):
    #     return obj.user.email
    # email.short_description = "Email"

admin.site.register(Profile, Filter)