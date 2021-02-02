from django.shortcuts import render,redirect,HttpResponse
from user.models import User
from user import models
# Create your views here.

def index(request):
    pass
    return render(request,'index.html')

#构建注册视图函数
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User()
        user.username = username
        user.password = password
        user.save()
    return render(request, 'register.html')


#构建登录视图函数
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                print(user)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')


def logout(request):
    pass
    return redirect('/index/')