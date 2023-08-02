from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from shortcuts.models import Application, Shortcut


@admin.register(Shortcut)
class ShortcutAdmin(SimpleHistoryAdmin):
    """ShortcutAdminAdmin Class"""

    list_display = (
        "shortcut",
        "description",
        "alt_shortcut",
        "default_shortcut",
        "how_to_activate",
        "slug",
        "user",
        "deleted_at",
    )
    ordering = ("-pk",)
    prepopulated_fields = {
        "slug": (
            "description",
            "shortcut",
        )
    }
    list_filter = ("deleted_at",)


@admin.register(Application)
class ApplicationAdmin(SimpleHistoryAdmin):
    """ApplicationAdmin Class"""

    list_display = ("title", "slug", "deleted_at")
    ordering = ("-pk",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("deleted_at",)
