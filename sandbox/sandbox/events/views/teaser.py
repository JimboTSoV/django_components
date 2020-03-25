from django.views.generic import DetailView

from sandbox.events.models import Teaser


class TeaserView(DetailView):
    model = Teaser
