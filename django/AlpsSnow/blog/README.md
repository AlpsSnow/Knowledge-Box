## `blog`应用的开发

### 编写视图

> 编辑视图文件：`blog/views.py`
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the blog app's index.")
```

### 配置路由

> 1.创建`blog`应用的路由配置文件：`urls.py`到`blog`目录下

> 2.编辑`blog/urls.py`
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
> 3.编辑`AlpsSnow`项目的路由配置文件：`AlpsSnow/urls.py`
```
# 将`AlpsSnow`项目到`blog`应用的路由加入到`urlpatterns`列表中
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
>> 函数 include() 允许引用其它 urls。每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 urls 以供进一步处理。
注意：当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外。

> 4.重新启动开发服务器，访问`http://127.0.0.1:8000/blog/`检验`blog`是否正常。
```manage.py runserver```

![示例图](blog-index.png)

