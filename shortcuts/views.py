from shortcuts.models import Shortcut
from django.views.generic import ListView


# Create your views here.
class ShortcutListView(ListView):
    """ShortcutListView List View

    The default List View for Shortcuts

    Args:
        ListView (ListView): Lists elements

    Returns:
        posts: A list of posts
    """

    template_name = "shortcuts/shortcut_list.html"

    def get_queryset(self):
        """Get queryset"""
        Shortcut.objects.all()

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Latest Shortcuts"
        context["objects"] = Shortcut.objects.all()
        return context
