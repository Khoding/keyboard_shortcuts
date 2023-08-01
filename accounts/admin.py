from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Admin class for CustomUserAdmin"""

    model = CustomUser

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            ("Personal Info"),
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            ("Metadata"),
            {
                "fields": (
                    "is_active",
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
