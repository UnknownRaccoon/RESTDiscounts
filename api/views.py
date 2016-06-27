from api.permissions import CardAccessPermission
from api.serializers import CardSerializer
from discounts.models import Card
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class CardListView(ListCreateAPIView):
    serializer_class = CardSerializer
    permission_classes = (CardAccessPermission,IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['profile'] = request.user.profile.id
        return super(CardListView, self).post(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_company:
            return Card.objects.filter(company=self.request.user.company)
        else:
            return Card.objects.filter(profile=self.request.user.profile)


class CardElementView(RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    permission_classes = (CardAccessPermission,IsAuthenticated)

    def put(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['profile'] = request.user.profile.id
        return super(CardElementView, self).put(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_company:
            return Card.objects.filter(company=self.request.user.company)
        else:
            return Card.objects.filter(profile=self.request.user.profile)
