from django.urls import path,include
from .views import createsuperuser,createuser,dashboard,users,delete_user,user_details
from django.contrib import admin
urlpatterns=[
    path("",dashboard,name="super-user-dashboard"),
    path("users/<int:num>/",users,name="users"),
    path("createuser/",createuser,name="create-user"),
    path("createsuperuser/",createsuperuser,name="create-super-user"),
    path("user/<int:num>/",user_details,name="user-details"),
    path("delete/<int:num>/",delete_user,name="delete-user")
    ]