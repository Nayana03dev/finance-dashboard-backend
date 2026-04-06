from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [IsAuthenticated(), IsAdmin()]