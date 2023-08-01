import auto_prefetch
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class CustomUser(AbstractUser):
    """CustomUser Model Class"""

    email = models.EmailField()
    slug = models.SlugField(
        blank=True,
        unique=True,
        default="",
        max_length=200,
        help_text="The slug is the direct link to your profile, it's auto generated based on your Username",
    )

    def __str__(self):
        """String representation of CustomUser Model"""
        return self.username

    def save(self, *args, **kwargs):
        """Save method for CustomUser Model"""
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get absolute url for CustomUser Model"""
        return reverse("accounts:profile", kwargs={"slug": self.slug})

    def get_absolute_update_url(self):
        """Get absolute url for CustomUser Model"""
        return reverse("accounts:edit_profile", kwargs={"slug": self.slug})

    def get_absolute_admin_update_url(self):
        """Get the absolute admin update url"""
        return reverse(
            "admin:accounts_customuser_change", kwargs={"object_id": self.pk}
        )

    def get_index_view_url(self):
        """Get the absolute index view url"""
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse(f"{content_type.app_label}:profile", kwargs={"slug": self.slug})

    @property
    def number(self):
        """User's number"""
        return f"#{self.pk}"
