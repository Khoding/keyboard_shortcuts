from ..django import BASE_DIR

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR + "/keyboard_shortcuts/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "cards": "keyboard_shortcuts.templatetags.cards",
            },
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = ("django.core.context_processors.request",)

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
