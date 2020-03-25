from django.forms import ModelForm
from django.views.generic import DetailView, UpdateView

from sandbox.pages.models import Page


class PageView(DetailView):
    model = Page
    context_object_name = "page"

    def get_template_names(self):
        return [self.object.page_type.base_template_path]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit_mode"] = False
        return context


class PageEditForm(ModelForm):
    class Meta:
        model = Page
        fields = ["name", "page_type"]


class PageEditView(UpdateView):
    model = Page
    form_class = PageEditForm
    context_object_name = "page"

    def get_template_names(self):
        return [self.object.page_type.base_template_path]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit_mode"] = True
        return context
