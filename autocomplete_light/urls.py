"""
An url to AutocompleteView.

autocomplete_light_autocomplete
    Given a 'autocomplete' argument with the name of the autocomplete, this url
    routes to AutocompleteView.

autocomplete_light_registry
    Renders the autocomplete registry, good for debugging, requires being
    authenticated as superuser.
"""
from django.conf.urls import url

from .views import AutocompleteView, RegistryView


urlpatterns = [
    url(r'^(?P<autocomplete>[-\w]+)/$',
        AutocompleteView.as_view(),
        name='autocomplete_light_autocomplete'
    ),
    url(r'^$',
        RegistryView.as_view(),
        name='autocomplete_light_registry'
    ),
]
