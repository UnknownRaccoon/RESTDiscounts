from api.views import CardElementView, CardListView
from django.conf.urls import url
urlpatterns = [
    url(r'^cards/(?P<pk>[0-9]+)$', CardElementView.as_view(), name='card_element'),
    url(r'^cards/$', CardListView.as_view(), name='card_list'),
]
