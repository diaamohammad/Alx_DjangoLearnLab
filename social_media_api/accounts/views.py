from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterApiView(APIView):

    def post(request):
        if request.method == 'POST':
            serializer = UserModelSerializer(data=request.data)
            if serializer.is_vaild():
                user=serializer.save()
                return Response({'message':'user created successfuly'},status=status.HTTP_201_CREATED)
                
                 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):

    def post(request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            token, created=Token.objects.get_or_create(user=user)
            login(request,user)
            return Response({'message':'user loged in successfuly',
            "token":token.key},status=status.HTTP_200_OK)
        return Response({'message':'authencation failed'},status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(request):
        user = request.user
        serializer = UserModelSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(request):
        user = request.user
        serializer = UserModelSerializer(user,request.data)

        if serializer.is_vaild():
            serializer.save()
            return Response({'message':'profile updated successfuly'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 