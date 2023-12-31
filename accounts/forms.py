from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """CustomUserCreationForm Form Class"""

    class Meta:
        """Meta class for CustomUserCreationForm Form"""

        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """CustomUserChangeForm Form Class"""

    class Meta:
        """Meta class for CustomUserChangeForm Form"""

        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "slug",
        )
