import uuid

from django.db import models
from django.utils.translation import gettext as _


class PageType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=200, blank=True)
    base_template_path = models.CharField(verbose_name=_("Base Template Path"), max_length=400)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)
