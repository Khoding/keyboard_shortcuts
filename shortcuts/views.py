from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from shortcuts.models import Application, Category, Shortcut


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
    context_object_name = "object_list"
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """Get queryset"""
        if self.request.GET.get("q"):
            return Shortcut.objects.filter(default__slug__icontains=self.request.GET.get("q"), deleted_at__isnull=True)
        return Shortcut.objects.filter(deleted_at__isnull=True)

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = "Khodok's Shortcuts"
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
    paginate_by = 20
    paginate_orphans = 5

    def get_object(self, queryset=None):
        """Get object"""
        obj = super(ShortcutDetailView, self).get_object(queryset=queryset)
        obj.clicked()
        if obj.deleted_at:
            raise Http404
        return super().get_object()

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = f"Shortcut '{self.object.title}'"
        return context


class ShortcutInCategoryListView(ListView):
    """ShortcutInCategoryListView List View

    List View for Shortcuts in Category

    Args:
        ListView (ListView): Lists elements

    Returns:
        posts: A list of posts
    """

    model = Category
    template_name = "shortcuts/shortcut_list.html"
    context_object_name = "object_list"
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """Get queryset"""
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return Shortcut.objects.filter(categories=self.category, deleted_at__isnull=True)

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = f"Shortcuts in {self.category.title}"
        return context


class ShortcutInApplicationListView(ListView):
    """ShortcutInApplicationListView List View

    List View for Shortcuts in application

    Args:
        ListView (ListView): Lists elements

    Returns:
        posts: A list of posts
    """

    model = Shortcut
    template_name = "shortcuts/shortcut_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        """Get queryset"""
        self.application = get_object_or_404(Application, slug=self.kwargs["slug"])
        return Shortcut.objects.filter(application=self.application, deleted_at__isnull=True)

    def get_context_data(self, **kwargs):
        """Get context data"""
        context = super().get_context_data(**kwargs)
        context["title"] = f"Shortcuts in {self.application.title}"
        return context
