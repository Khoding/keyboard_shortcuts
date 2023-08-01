from django.db import models
from django.template.defaultfilters import slugify
import auto_prefetch

from keyboard_shortcuts import settings


# create a new model called Shortcut
class Shortcut(auto_prefetch.Model):
    shortcut = models.CharField(max_length=100)
    description = models.TextField()
    application = auto_prefetch.ForeignKey(
        "shortcuts.Application", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    @property
    def title(self):
        return self.shortcut


# create a new model called Application
class Application(auto_prefetch.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
