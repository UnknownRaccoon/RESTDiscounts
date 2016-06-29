from api.views import CardElementView, CardListView, AddressElementView, AddressListView
from django.conf.urls import url
urlpatterns = [
    url(r'^cards/$', CardListView.as_view(), name='card_list'),
    url(r'^cards/(?P<pk>[0-9]+)$', CardElementView.as_view(), name='card_element'),
    url(r'^companies/(?P<company_id>[0-9]+)/addresses/$', AddressListView.as_view(), name='address_list'),
    url(r'^companies/(?P<company_id>[0-9]+)/addresses/(?P<pk>[0-9]+)$', AddressElementView.as_view(), name='address_element'),
]
