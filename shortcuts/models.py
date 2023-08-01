import itertools

from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.utils import timezone

import auto_prefetch
from simple_history.models import HistoricalRecords

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
    slug = models.SlugField(unique=True, max_length=200, help_text="Shortcut slug")
    deleted_at = models.DateTimeField(
        blank=True, null=True, help_text="Deletion date for soft delete"
    )
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Save Post"""
        if not self.slug:
            max_length = self._meta.get_field("slug").max_length
            self.slug = orig = slugify(self.title)[:max_length]
            for x in itertools.count(2):
                if (
                    self.pk
                    and self.objects.filter(
                        Q(slug=self.slug),
                        Q(id=self.pk),
                    ).exists()
                ):
                    break
                if not self.objects.filter(slug=self.slug).exists():
                    break

                # Truncate & Minus 1 for the hyphen.
                self.slug = f"{orig[: max_length - len(str(x)) - 1]}-{x}"
        return super().save(*args, **kwargs)

    def soft_delete(self):
        """Soft delete Category"""
        self.deleted_at = timezone.now()
        self.save()

    @property
    def title(self):
        return self.shortcut


# create a new model called Application
class Application(auto_prefetch.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=200, help_text="Shortcut slug")
    deleted_at = models.DateTimeField(
        blank=True, null=True, help_text="Deletion date for soft delete"
    )
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Save Post"""
        if not self.slug:
            max_length = self._meta.get_field("slug").max_length
            self.slug = orig = slugify(self.title)[:max_length]
            for x in itertools.count(2):
                if (
                    self.pk
                    and self.objects.filter(
                        Q(slug=self.slug),
                        Q(id=self.pk),
                    ).exists()
                ):
                    break
                if not self.objects.filter(slug=self.slug).exists():
                    break

                # Truncate & Minus 1 for the hyphen.
                self.slug = f"{orig[: max_length - len(str(x)) - 1]}-{x}"
        return super().save(*args, **kwargs)

    def soft_delete(self):
        """Soft delete Category"""
        self.deleted_at = timezone.now()
        self.save()
