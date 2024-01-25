from django.urls import path
from .views import *

urlpatterns = [
    path('userType/', UserTypeList.as_view(), name='userType'),
    path('userType/<str:pk>/', UserTypeDetail.as_view(), name='userTypeDetail'),
    path('userType/create/', UserTypeCreate.as_view(), name='createUserType'),
    path('userType/<str:pk>/update/', UserTypeUpdate.as_view(), name='updateUserType'),
    path('userType/<str:pk>/delete/', UserTypeDelete.as_view(), name='deleteUserType'),

    path('user/', UserList.as_view(), name='user'),
    path('user/<int:pk>/', UserDetail.as_view(), name='userDetail'),
    path('user/create/', UserCreate.as_view(), name='createUser'),
    path('user/<int:pk>/update/', UserUpdate.as_view(), name='updateUser'),
    path('user/<int:pk>/delete/', UserDelete.as_view(), name='deleteUser'),
]
