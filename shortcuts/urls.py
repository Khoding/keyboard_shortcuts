from django.urls import path

from shortcuts.views import ShortcutDetailView, ShortcutInApplicationListView, ShortcutListView

app_name = "shortcuts"
urlpatterns = [
    path("", ShortcutListView.as_view(), name="shortcut_list"),
    path("shortcut/<slug:slug>/", ShortcutDetailView.as_view(), name="shortcut_detail"),
    path("application/<slug:slug>/", ShortcutInApplicationListView.as_view(), name="shortcut_in_application_list"),
]
