import uuid

from django.db import models
from django.utils.translation import gettext as _

from sandbox.pages.models.component_model import ComponentModel


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=200, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=600, blank=True)
    picture = models.ImageField(verbose_name=_("Picture"), max_length=200, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)


class EventTeaser(ComponentModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    @property
    def name(self):
        return self.event.name

    def __str__(self):
        return "{}-Teaser - {}".format(self.name, self.id)
