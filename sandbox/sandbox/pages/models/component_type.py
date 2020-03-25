import uuid

from django.db import models
from django.utils.translation import gettext as _


class ComponentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=200, blank=True)
    registered_placeholders = models.ManyToManyField('PlaceholderType', verbose_name=_("Registered Placeholders"), related_name="component_types")
    template_name = models.CharField(verbose_name=_("Template Name"), max_length=400, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)