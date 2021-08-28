from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email',]


class TaskSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    estimated_finish_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M',
                                                      input_formats = ['%d-%m-%Y %H:%M'], )
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Task
        fields = ['id', 'title', 'author', 'body', 'estimated_finish_time', 'created_at', 'is_completed']
        read_only_fields = ['created_at', 'is_completed'] 