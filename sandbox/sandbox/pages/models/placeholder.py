import uuid

from django.db import models


class Placeholder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey('Page', on_delete=models.CASCADE, verbose_name="Page", related_name="placeholders",
                             null=True)
    placeholder_type = models.ForeignKey('PlaceholderType', on_delete=models.CASCADE, verbose_name="Placeholder Type",
                                         related_name="placeholders", null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['page', 'placeholder_type'], name='unique_placeholder')
        ]

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    @property
    def name(self):
        return "{}_{}".format(self.placeholder_type.name, self.page.id)

    @property
    def human_readable_name(self):
        return self.placeholder_type.name