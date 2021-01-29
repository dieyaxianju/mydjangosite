#项目目录说明
|---mydjangosite # 项目的/目录 
  |---mydjangosite # 项目目录 
    |---templates # myapp的应用 
         |---runoob.html #模板
    |---settings.py # 配置文件 
    |---asgi.py # 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目
    |---urls.py # 路由系统 ===> url与视图的对应关系 
    |---wsgi.py # runserver命令就使用wsgiref模块做简单的web server 
  |---myapp # myapp的应用 自己新建的
      |---admin.py 
      |---apps.py 
      |---models.py 
      |---tests.py 
      |---urls.py # myapp的应用路由系统 ===> url与视图的对应关系 
      |---views.py # myapp的应用 
  |---manage.py # 管理文件

#环境安装 #在线安装
Terminal执行  pip install -r requirements.txt 

#项目如何运行
1、进入根目录mydjangosite
2、python manage.py runserver 127.0.0.1:8000
3、启动后浏览器输入对应地址 如：http://127.0.0.1:8000/runoob/  即mydjangosite\mydjangosite\urls.py配置的路径

#git常见问题
一、如果git pull时和本地文件有冲突如何解决
    1、将本地文件暂时存储
        git stash
    2、查看本地保存的标记
        git stash list 可以看到保存的标记比如：stash@{0}就是刚才保存的标记
    3、再拉最新的代码
        git pull
    4、还原暂存的内容
        git stash pop stash@{0}
        


    
    