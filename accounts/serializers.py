from rest_framework import serializers
from django.contrib.auth import get_user_model
from todos.models import Task
from rest_framework.exceptions import ValidationError
User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', ]

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'name', 'password', 'confirm_password', ]

    def create(self, validated_data):
        username = validated_data['username']
        name = validated_data['name']
        password = validated_data['password']
        user_obj = User(
            username=username,
            name = name
        )
        user_obj.set_password(password)
        user_obj.save()

        return validated_data
    
    def validate_confirm_password(self, value):
        data = self.get_initial()
        password = data.get('password')
        password2 = value
        if password != password2:
            raise ValidationError('Passwords must match')
        return value
