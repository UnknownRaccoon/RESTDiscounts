from api.serializers import UserSerializer, CompanySerializer
from django.contrib.auth.models import User

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class UserElementView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        result = super(UserElementView, self).put()