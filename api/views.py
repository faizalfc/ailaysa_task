from django.shortcuts import render
from .models import UserInfo
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import Http404




class UserList(APIView):
    
    def get(self,request):
        user = UserInfo.objects.all()
        serializer = UserSerializer(user , many =True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class UserDetail(APIView):
    
    def get_object(self, pk):
        try:
            return UserInfo.objects.get(pk=pk)
        except UserInfo.DoesNotExist:
            raise Http404
        
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response({"message":"User deleted"}, status=status.HTTP_204_NO_CONTENT)