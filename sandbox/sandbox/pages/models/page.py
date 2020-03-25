import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=200, blank=False)
    slug = models.SlugField(verbose_name=_("Slug"), null=True, blank=True)
    url_path = models.CharField(verbose_name=_("Url Path"), max_length=200, blank=True)
    page_type = models.ForeignKey('PageType', on_delete=models.CASCADE, verbose_name=_("Page Type"))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['url_path', 'slug'], name='unique_url')
        ]

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def url(self):
        return "{} - {}".format(self.url_path, self.slug)