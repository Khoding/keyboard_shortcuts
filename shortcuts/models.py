import itertools

from django.db import models
from django.db.models import F, Q
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

import auto_prefetch
from simple_history.models import HistoricalRecords

from keyboard_shortcuts import settings


class Shortcut(auto_prefetch.Model):
    title = models.CharField(max_length=50)
    key = models.CharField(max_length=100)
    key_in_app = models.CharField(
        max_length=100, blank=True, null=True, help_text="Basically the key but as like 'shift+alt+oem_period'"
    )
    command = models.CharField(
        max_length=255, blank=True, null=True, help_text="The command that the shortcut executes."
    )
    description = models.TextField()
    how_to_activate = models.TextField(
        blank=True, null=True, help_text="If the shortcut isn't possible without some other action, describe it here."
    )
    when = models.TextField(blank=True, null=True, help_text="When this shortcut works.")
    application = models.ManyToManyField("shortcuts.Application", related_name="shortcuts")
    default = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="modified")
    alternative = models.ManyToManyField(
        "self", blank=True, help_text="Alternative shortcuts, does the same thing but different keys."
    )
    related = models.ManyToManyField("self", blank=True, help_text="Related shortcuts, does something similar.")
    categories = models.ManyToManyField("shortcuts.Category", related_name="shortcuts")
    user = auto_prefetch.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    order = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=200, help_text="Shortcut slug")
    clicks = models.IntegerField(default=0, help_text="How many times the shortcut has been seen")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="Deletion date for soft delete")
    history = HistoricalRecords()

    class Meta:
        base_manager_name = "prefetch_manager"
        ordering = ["order", "-pk"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Save Post"""
        if not self.slug:
            max_length = self._meta.get_field("slug").max_length
            self.slug = orig = slugify(self.title, self.key)[:max_length]
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

    def save_without_historical_record(self, *args, **kwargs):
        """Save Post without Historical Record"""
        self.skip_history_when_saving = True  # skipcq: PYL-W0201
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret

    def get_absolute_url(self):
        return reverse("shortcuts:shortcut_detail", kwargs={"slug": self.slug})

    def clicked(self):
        """Clicked Post"""
        self.clicks = F("clicks") + 1
        self.save_without_historical_record(update_fields=["clicks"])

    def soft_delete(self):
        """Soft delete Category"""
        self.deleted_at = timezone.now()
        self.save()


class Category(auto_prefetch.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=200, help_text="Shortcut slug")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="Deletion date for soft delete")
    history = HistoricalRecords()

    class Meta:
        base_manager_name = "prefetch_manager"
        verbose_name_plural = "Categories"

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

    def get_absolute_url(self):
        return reverse("shortcuts:shortcut_in_category_list", kwargs={"slug": self.slug})

    def soft_delete(self):
        """Soft delete Category"""
        self.deleted_at = timezone.now()
        self.save()


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

    def get_absolute_url(self):
        return reverse("shortcuts:shortcut_in_application_list", kwargs={"slug": self.slug})

    def soft_delete(self):
        """Soft delete Category"""
        self.deleted_at = timezone.now()
        self.save()
