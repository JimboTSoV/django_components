from django.contrib import admin

from sandbox.events.models.event import EventTeaser, Event
from sandbox.pages.admin import ComponentInline


# Register your models here.
class EventTeaserAdmin(admin.ModelAdmin):
    inlines = [
        ComponentInline,
    ]


admin.site.register(Event)
admin.site.register(EventTeaser, EventTeaserAdmin)
