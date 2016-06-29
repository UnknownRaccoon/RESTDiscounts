from api.permissions import CardAccessPermission, CardCreatePermission, AddressCreatePermission, AddressAccessPermission
from api.serializers import CardSerializer, AddressSerializer
from custom_auth.models import Address
from discounts.models import Card
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class CardListView(ListCreateAPIView):
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, CardCreatePermission)

    def get_queryset(self):
        if self.request.user.is_company:
            return Card.objects.filter(company=self.request.user.company)
        else:
            return Card.objects.filter(profile=self.request.user.profile)

    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['profile'] = request.user.profile.id
        return super(CardListView, self).post(request, *args, **kwargs)


class CardElementView(RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, CardAccessPermission)

    def get_queryset(self):
        if self.request.user.is_company:
            return Card.objects.filter(company=self.request.user.company)
        else:
            return Card.objects.filter(profile=self.request.user.profile)


class AddressListView(ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated, AddressCreatePermission)

    def get_queryset(self):
            return Address.objects.filter(company_id=self.kwargs['company_id'])

    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['company'] = request.user.company.id
        return super(AddressListView, self).post(request, *args, **kwargs)


class AddressElementView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated, AddressAccessPermission)

    def get_queryset(self):
            return Address.objects.filter(company_id=self.kwargs['company_id'])

