from rest_framework import serializers
from .models import ToDo, User


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["id", "task", "completed"]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
