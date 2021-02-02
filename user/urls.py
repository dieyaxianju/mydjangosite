# # from django.conf.urls import url

from user.views import *
from django.urls import path

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),

]