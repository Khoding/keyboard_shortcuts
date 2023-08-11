from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from shortcuts.models import Application, Category, Shortcut


@admin.register(Shortcut)
class ShortcutAdmin(SimpleHistoryAdmin):
    """ShortcutAdminAdmin Class"""

    list_display = (
        "title",
        "key",
        "key_in_app",
        "default",
        "order",
        "slug",
        "deleted_at",
    )
    ordering = ("-pk",)
    prepopulated_fields = {
        "slug": (
            "title",
            "key",
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


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin):
    """CategoryAdmin Class"""

    list_display = ("title", "slug", "deleted_at")
    ordering = ("-pk",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("deleted_at",)
