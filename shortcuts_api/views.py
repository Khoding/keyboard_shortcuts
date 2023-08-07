from rest_framework import viewsets
from shortcuts.models import Shortcut, Application
from shortcuts_api.serializers import ShortcutSerializer, ApplicationSerializer


class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.filter(deleted_at__isnull=True)
    serializer_class = ShortcutSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.filter(deleted_at__isnull=True)
    serializer_class = ApplicationSerializer
