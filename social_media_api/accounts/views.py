from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins, generics


class RegisterApiView(APIView):
    
    def POST(self,request):
            
            serializer = UserModelSerializer(data=request.data)
            if serializer.is_valid():
                  user=serializer.save()
                  return Response({'message':'user created successfuly'},status=status.HTTP_201_CREATED)
                
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):

    def POST(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            
            login(request,user)
            return Response({'message':'user loged in successfuly',
            },status=status.HTTP_200_OK)
        return Response({'message':'authencation failed'},status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(APIView):
    permission_classes = [IsAuthenticated]
    def GET(self,request):
        user = request.user
        serializer = UserModelSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def PUT(self,request):
        user = request.user
        serializer = UserModelSerializer(user,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'profile updated successfuly'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    

class FollowUser(generics.GenericAPIView, mixins.CreateModelMixin):
     
     permission_class = [IsAuthenticated]
     
     def POST(self,request,user_id,*args,**kwargs):
          
          
          try:
               follow_user = CustomUser.objects.get(id=user_id)

          except CustomUser.DoesNotExist:
               return Response({'error':'user not found'},status=status.HTTP_401_UNAUTHORIZED)
          
          request.user.following.add(follow_user)
          return Response({"message":f"now you following{follow_user.username}"})
     
class UnFollowUser(generics.GenericAPIView):
     permission_class = [IsAuthenticated]

     def POST(self,request,user_id,*args,**kwargs):
          
          try:
               follow_user = CustomUser.objects.get(id=user_id)
          
          except CustomUser.DoesNotExist:
               return Response({"error":"user not found"},status=status.HTTP_401_UNAUTHORIZED)
          
          return request.user.following.remove(follow_user)
     
          return Response({"message": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
               
          
          