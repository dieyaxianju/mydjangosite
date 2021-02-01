# # from django.conf.urls import url
# from django.urls import path
from django.urls import re_path
from django.urls import include, path
from . import views,testdb
from django.views.generic import TemplateView   #使用vue时 添加

urlpatterns = [
    # url(r'^$', view.hello),
    path('hello/', views.hello),
    path('myapp/', include('myapp.urls')),
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    # re_path(r'^hello$',views.hello),
    path('index/', TemplateView.as_view(template_name="index.html")),  #使用vue时 添加
]