#项目目录说明
sis
├── .env
├── debugtalk.py
├── api
├── testcases
├── testsuites
├── reports
└── data

#环境安装 #在线安装
Terminal执行  pip install -r requirements.txt 

#用例如何运行（以sis为例）
1、进入sis目录
2、hrun api/Dorm/SetDormOrgUsers.yml --dot-env-path .env_test01
3、查看请求详情 加参数--log-level debug 如： hrun api/School/ListByIds.yml  --dot-env-path  .env_test06 --log-level debug

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
        


    
    