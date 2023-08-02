import itertools

from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

import auto_prefetch
from simple_history.models import HistoricalRecords

from keyboard_shortcuts import settings


class Shortcut(auto_prefetch.Model):
    shortcut = models.CharField(max_length=100)
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    how_to_activate = models.TextField(
        blank=True, null=True, help_text="If the shortcut isn't possible without some other action, describe it here."
    )
    application = models.ManyToManyField("shortcuts.Application", related_name="shortcuts")
    default = models.ManyToManyField("self", blank=True)
    alternative = models.ManyToManyField("self", blank=True)
    related = models.ManyToManyField("self", blank=True)
    user = auto_prefetch.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(unique=True, max_length=200, help_text="Shortcut slug")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="Deletion date for soft delete")
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Save Post"""
        if not self.slug:
            max_length = self._meta.get_field("slug").max_length
            self.slug = orig = slugify(self.title, self.short_description)[:max_length]
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

    def get_absolute_url(self):
        return reverse("shortcuts:shortcut_detail", kwargs={"slug": self.slug})

    def soft_delete(self):
        """Soft delete Category"""
        self.deleted_at = timezone.now()
        self.save()

    @property
    def title(self):
        return self.shortcut


class Application(auto_prefetch.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=200, help_text="Shortcut slug")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="Deletion date for soft delete")
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
