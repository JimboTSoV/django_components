import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from sandbox.pages.models import Component


class ComponentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component = GenericRelation(Component, related_query_name="component")

    def __str__(self):
        return self.name