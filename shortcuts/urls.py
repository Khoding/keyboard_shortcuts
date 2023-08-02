from django.urls import path

from shortcuts.views import ShortcutDetailView, ShortcutListView

app_name = "shortcuts"
urlpatterns = [
    path("", ShortcutListView.as_view(), name="shortcut_list"),
    path("shortcut/<slug:slug>", ShortcutDetailView.as_view(), name="shortcut_detail"),
]
