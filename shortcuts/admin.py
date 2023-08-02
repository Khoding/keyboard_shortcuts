from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from shortcuts.models import Application, Shortcut


@admin.register(Shortcut)
class ShortcutAdmin(SimpleHistoryAdmin):
    """ShortcutAdminAdmin Class"""

    list_display = (
        "shortcut",
        "default",
        "short_description",
        "slug",
        "deleted_at",
    )
    ordering = ("-pk",)
    prepopulated_fields = {
        "slug": (
            "short_description",
            "shortcut",
        )
    }
    list_filter = ("deleted_at", "none_default")


@admin.register(Application)
class ApplicationAdmin(SimpleHistoryAdmin):
    """ApplicationAdmin Class"""

    list_display = ("title", "slug", "deleted_at")
    ordering = ("-pk",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("deleted_at",)
