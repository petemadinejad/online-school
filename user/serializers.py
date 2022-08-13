from rest_framework import serializers
from user.models import User


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", "password", "last_login", "date_joined"]
