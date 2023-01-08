It is a very useful warehouse to collect and sort out some daily work in learning and thinking.Including C/C + +, Java, javascript, python, HTML, CSS, result, django, Linux, Windows programming knowledge, etc

## 起步

### 创建python虚拟环境 
#### Windows
1. 安装 `virtualenvwrapper-win`   
```pip install virtualenvwrapper-win```

2. 创建系统环境变量

| Key | Value | 
| ------ | ------ |
| WORKON_HOME | %USERPROFILE%\Envs |

3. 创建 `Knowledge-Box` 项目的虚拟环境  

```mkvirtualenv KnowledgeBoxEnv```

4. 进入python的虚拟环境  

```workon KnowledgeBoxEnv```


5. 退出python的虚拟环境  
```deactivate```

6. 显示python虚拟环境一览  
```lsvirtualenv```


※更多关于 `virtualenvwrapper-win` 的使用方法，请参照[windows下安装Python虚拟环境virtualenvwrapper-win](https://www.cnblogs.com/suke99/p/5355894.html)

#### Linux 
1. 安装 `virtualenvwrapper`   
```pip3 install virtualenvwrapper```

2. 配置全局变量，让每次登陆linux时候，就加载这个virtualenvwrapper.sh脚本文件，使得virtualenvwrapper这个工具生效。

```~/.bashrc中添加下面的内容。```
```python
vim ~/.bashrc
export WORKON_HOME=~/Envs
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 #python3的安装路径

source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc
```

3. 创建 `Knowledge-Box` 项目的虚拟环境 
```mkvirtualenv KnowledgeBoxEnv```

4. 激活python的虚拟环境 

```workon KnowledgeBoxEnv```

5. 退出python的虚拟环境  
```deactivate```

### vscode设置python代码自动补全
1. `vscode`的`设置`检索`python.autocomplete`
2. 点击`在settings.json中编辑`
3. 设置`python.languageServer = Jedi`,[参照说明1](https://github.com/microsoft/vscode-python/issues/7010),[参照说明2](https://stackoverflow.com/questions/55897160/what-is-the-difference-between-jedi-and-python-language-server-in-vs-code-ide)
4. 设置`python.autoComplete.extraPaths`
```json
"python.autoComplete.extraPaths": [        
        "C:/Python310/Lib/site-packages",
        "C:/Python310/Scripts"
    ]
```

### pip升级package
1. 升级pip
`python -m pip install --upgrade pip`
2. 查看已经安装的package
`pip list`
3. 检查所有可以升级的package
`pip list --outdated`
4. 升级package
`pip install --upgrade package_name`  

## 加入进来一起干

1. 克隆 `Knowledge-Box` 项目到本地
2. 创建python虚拟环境
3. 进入python虚拟环境
4. 在python虚拟环境下，使用`cd`命令切入到`Knowledge-Box` 项目文件夹下
>> 切入到`Knowledge-Box` 项目文件夹下  
```
D:\C work>workon KnowledgeBoxEnv
(KnowledgeBoxEnv) D:\C work>cd D:\python work\Knowledge-Box\Knowledge-Box\django
```
5. 重建开发环境  
```pip install -r requirement.txt```

6. 开始写代码，测试... `just do it`  

7. 冻结开发环境  
```python	
pip freeze > requirement.txt　　# 安装包列表保存到文件packages.txt中　
```
8. `git commit`提交成果  

9. `pull request`提出贡献  

## 欢迎你的加入！

1. Django项目：[AlpsSnow](./django/README.md)
