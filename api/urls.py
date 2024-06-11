from django.contrib import admin
from django.urls import path
from .views import UserList , UserDetail

urlpatterns = [
    
    path('userlist/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail')
  
]
