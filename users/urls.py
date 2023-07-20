from django.urls import path
from users.views import  ProfileView
from django.contrib import admin
from .views import *


urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
]
