# # from django.conf.urls import url
# from django.urls import path
from django.urls import re_path
from django.urls import include, path
from . import views

urlpatterns = [
    # url(r'^$', view.hello),
    path('hello/', views.hello),
    path('myapp/', include('myapp.urls')),
    path('runoob/', views.runoob),
    # re_path(r'^hello$',views.hello),
]