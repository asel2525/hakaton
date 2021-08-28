from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import LoginSerializer, RegisterSerializer


User = get_user_model()

class RegisterAPIView(APIView): 
  def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)



class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        user = request.user

        if serializer.is_valid():
            username = serializer._validated_data.get('username')
            password = serializer._validated_data.get('password')
            user = User.objects.create(username=username,
                                       password=password)
            serializer = RegisterSerializer(instance=user)
            return Response(serializer.data)

        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
