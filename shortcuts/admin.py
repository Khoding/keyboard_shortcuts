from django.contrib import admin

from shortcuts.models import Shortcut, Application
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Shortcut)
class ShortcutAdmin(SimpleHistoryAdmin):
    """ShortcutAdminAdmin Class"""

    list_display = (
        "shortcut",
        "description",
        "slug",
        "application",
        "user",
        "deleted_at",
    )
    ordering = ("-pk",)
    prepopulated_fields = {"slug": ("description",)}
    list_filter = ("deleted_at",)


@admin.register(Application)
class ApplicationAdmin(SimpleHistoryAdmin):
    """ApplicationAdmin Class"""

    list_display = ("title", "slug", "deleted_at")
    ordering = ("-pk",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("deleted_at",)
