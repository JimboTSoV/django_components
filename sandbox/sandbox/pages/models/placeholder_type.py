import uuid

from django.db import models
from django.utils.translation import gettext as _


class PlaceholderType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=200, blank=True)
    page_type = models.ForeignKey('PageType', on_delete=models.CASCADE, verbose_name="Page Type", related_name="placeholders")

    def __str__(self):
        return "{} - {}".format(self.name, self.id)