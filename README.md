It is a very useful warehouse to collect and sort out some daily work in learning and thinking.Including C/C + +, Java, javascript, python, HTML, CSS, result, django, Linux, Windows programming knowledge, etc

## 起步

### 创建python虚拟环境  
> 1.安装 `virtualenvwrapper` (windows开发环境)  
```pip install virtualenvwrapper-win```

> 2.创建系统环境变量

| Key | Value | 
| ------ | ------ |
| WORKON_HOME | %USERPROFILE%\Envs |

> 3.创建 `Knowledge-Box` 项目的虚拟环境  
```mkvirtualenv KnowledgeBoxEnv```

> 4.进入python的虚拟环境  
```workon KnowledgeBoxEnv```

> 5.退出python的虚拟环境  
```deactivate```

※更多关于 `virtualenvwrapper` 的使用方法，请参照[windows下安装Python虚拟环境virtualenvwrapper-win](https://www.cnblogs.com/suke99/p/5355894.html)

### 加入进来一起干

> 1.克隆 `Knowledge-Box` 项目到本地
> 2.创建python虚拟环境
> 3.进入python虚拟环境
> 4.在python虚拟环境下，使用`cd`命令切入到`Knowledge-Box` 项目文件夹下
>> 切入到`Knowledge-Box` 项目文件夹下  
```
D:\C work>workon KnowledgeBoxEnv
(KnowledgeBoxEnv) D:\C work>cd D:\python work\Knowledge-Box\Knowledge-Box\django
```
> 5.重建开发环境  
```pip install -r PyPackages.txt```

> 6.开始写代码，测试... `just do it`  

> 7.冻结开发环境  
```	
pip freeze > PyPackages.txt　　# 安装包列表保存到文件packages.txt中　
```
> 8.`git commit`提交成果  

> 9.`pull request`提出贡献  

## 欢迎你的加入！

