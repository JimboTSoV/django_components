from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from sandbox.pages.models import *


class ComponentInline(GenericTabularInline):
    model = Component
    extra = 0


# Register your models here.
admin.site.register(Component)
admin.site.register(ComponentType)
admin.site.register(PageType)
admin.site.register(Page)
admin.site.register(Placeholder)
admin.site.register(PlaceholderType)
