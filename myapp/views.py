from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import UserType, User
from .serializers import UserTypeSerializer, UserSerializer
# Create your views here.
'''
@api_view(['GET'])
def userList(ListAPIView):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def userDetail(RetrieveAPIView, pk):
    queryset = User.objects.get(userId=pk)
    serializer = UserSerializer(queryset)
    return Response(serializer.data)

@api_view(['GET'])
def userTypeList(ListAPIView):
    users = UserType.objects.all()
    serializer = UserTypeSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userTypeDetail(RetrieveAPIView, pk):
    queryset = UserType.objects.get(userTypeName=pk)
    serializer = UserTypeSerializer(queryset)
    return Response(serializer.data)'''

class UserTypeList(ListAPIView):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()

class UserTypeDetail(RetrieveAPIView):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()
class UserTypeCreate(CreateAPIView, ListAPIView):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()

    def perform_create(self, serializer):
        name = self.request.data.get('userTypeName')
        desc = self.request.data.get('userTypeDesc')
        return serializer.save(userTypeName=name, userTypeDesc=desc)

class UserTypeUpdate(generics.UpdateAPIView):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()

class UserTypeDelete(generics.DestroyAPIView):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()

#################################################################

class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCreate(CreateAPIView, ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        name = self.request.data.get('namePlate')
        stars = self.request.data.get('stars')
        type = self.request.data.get('userTypeName')
        type = UserType.objects.get(userTypeName=type)
        return serializer.save(namePlate=name, stars=stars, userTypeName=type)

class UserUpdate(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDelete(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
