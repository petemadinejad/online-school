from rest_framework import viewsets
from user.serializers import AdminUserSerializer
from user.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = AdminUserSerializer
    queryset = User.objects.all()
