from django.urls import path

from shortcuts.views import ShortcutListView


app_name = "shortcuts"
urlpatterns = [
    path("", ShortcutListView.as_view(), name="shortcut_list"),
]
