from rest_framework import serializers
from shortcuts.models import Shortcut, Application


class ShortcutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortcut
        fields = ["title", "key", "description", "slug", "clicks", "application", "when"]


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ["title", "description", "slug"]
