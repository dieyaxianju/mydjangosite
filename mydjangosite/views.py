from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! my name is cailu ")

# def runoob(request):
#     context = {}
#     context['hello1'] = 'Hello World 这个是具体的文案!'
#     return render(request, 'register.html', context)

def runoob(request):
    views_name = "菜鸟教程这个是输出的"
    return render(request, "register.html", {"name": views_name})