## Django

#### 安装`Django`
 > ```(KnowledgeBoxEnv) D:\python work\Knowledge-Box\Knowledge-Box\django>pip install Django```

#### 使用`django-admin `创建项目`AlpsSnow`
 >  ```(KnowledgeBoxEnv) D:\python work\Knowledge-Box\Knowledge-Box\django>django-admin startproject AlpsSnow```

#### 项目`AlpsSnow`的文件结构 
```
(KnowledgeBoxEnv) D:\python work\Knowledge-Box\Knowledge-Box\django>cd AlpsSnow
(KnowledgeBoxEnv) D:\python work\Knowledge-Box\Knowledge-Box\django\AlpsSnow>tree /F
.
│  manage.py
│
└─AlpsSnow
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
#### 启动`AlpsSnow`项目
 ```
 (KnowledgeBoxEnv) D:\python work\Knowledge-Box\Knowledge-Box\django\AlpsSnow>manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 31, 2019 - 15:26:05
Django version 2.2.6, using settings 'AlpsSnow.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
 ```
### 访问`http://127.0.0.1:8000/`
![示例图](ProjectSuccessfully.png)



