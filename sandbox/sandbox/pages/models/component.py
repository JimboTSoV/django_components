import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.loader import get_template
from django.utils.translation import gettext as _


class Component(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_type = models.ForeignKey('ComponentType', on_delete=models.CASCADE, verbose_name=_("Component Type"))
    placeholder = models.ForeignKey('Placeholder', on_delete=models.CASCADE, verbose_name="Placeholder",
                                    related_name="components")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def render(self, request=None):
        template = get_template(self.component_type.template_name)
        return template.render(context={'component_object':self.content_object}, request=request)

    @property
    def name(self):
        return self.component_type.name

    @property
    def placeholder_is_valid(self):
        return self.placeholder.placeholder_type in self.component_type.registered_placeholders

    def __str__(self):
        return "{}-Component for {} at {}".format(self.name, self.placeholder.page.name, self.placeholder.name)
