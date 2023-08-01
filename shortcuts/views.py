from django.http import Http404
from shortcuts.models import Shortcut
from django.views.generic import ListView
from django.views.generic import DetailView


class ShortcutListView(ListView):
    """ShortcutListView List View

    The default List View for Shortcuts

    Args:
        ListView (ListView): Lists elements

    Returns:
        posts: A list of posts
    """

    model = Shortcut
    template_name = "shortcuts/shortcut_list.html"

    def get_queryset(self):
        """Get queryset"""
        Shortcut.objects.all()

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Shortcuts"
        context["objects"] = Shortcut.objects.all()
        return context


class ShortcutDetailView(DetailView):
    """ShortcutDetailView Detail View

    The default Detail View for Shortcuts

    Args:
        DetailView (DetailView): Shows a single element

    Returns:
        post: A single post
    """

    model = Shortcut
    template_name = "shortcuts/shortcut_detail.html"

    def get_object(self, queryset=None):
        """Get object"""
        obj = super(ShortcutDetailView, self).get_object(queryset=queryset)
        if obj.deleted_at:
            raise Http404
        return super().get_object()

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = f"Shortcut '{self.object.title}'"
        return context
