---
layout:     post
title:      "ubuntu18.04安装Superset"
subtitle:   "superset的安装与配置"
date:       2018-08-26 21:00:00
author:     "soaringsoul"
header-img: "img/ubuntu_login.png"
catalog: true
tags:
    - 技术教程
---
# ubuntu18.04下安装 Superset 

## 概述
本篇主要是讲解下如何在ubuntu18.04中安装superset。
本次安装为常规安装，主要针对的是普通用户;如果想对superset进行二次开发，需要配置开发环境，后面会再写一篇专门的博客讲解一下如何在ubuntu18.04下安装配置superset的开发环境。

---
## 1 准备工作-安装superset系统依赖项
### 1.1 安装ubuntu 依赖项

```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev
```

### 1.2 **安装 python 虚拟环境管理工具：virtualenv**
```
sudo apt install python3-pip
pip3 install virtualenv
```

## 2 安装superset
### 2.1 创建superset虚拟安装环境
```
# 在主目录下新建一个文件夹，此步骤也可以略过，并cd到此目录
sudo mkdir ~/superset_dev
cd ~/superset_dev
# 更新pip和setuptools
sudo pip install --upgrade setuptools pip
# # 创建一个python3的虚拟环境,如果需要指定其他版本可以自行百度virtualenv 指定python版本
sudo virtualenv -p /usr/bin/python3 superset_venv
# 如果提示以下错误:
Command 'virtualenv' not found, but can be installed with:
使用sudo apt install virtualenv 再次安装virtualenv
# 激活虚拟环境 
. superset_venv/bin/activate
```
![posts_2018-08-26-superset_setup_normal_venv_init](/img/superset_normal_setup/posts_2018-08-26-superset_setup_normal_venv_init.png)

### 2.2 更新pip源，提高安装速度
ubuntu 默认使用的pip官方源，安装速度比较慢，所以一定要替换为国内的源，不然如果使用pip install的方式安装一些诸如pandas, superset等一些比较大的第三方库时那就真的很痛苦了，可能会在中途中断和重新运行命令多次。
ubuntu下更换pip的方式和windows下更换pip源的方法都比较简单，在这里顺便把在windows下和ubuntu下更换源的方法都说一下。
**之所以把更换pip源放到这一步骤是因为，如果放到第1步的时候 ，在运行pip install --upgrade setuptools pip 命令时可能会提示以下错误：**
> pip._vendor.requests.exceptions.HTTPError: 404 Client Error: Not Found for url: >https://pypi.tuna.tsinghua.edu.cn/simple/pkg-resources/


* **Ubuntu下更换pip的方法(其他linux系统也是通用的）**

这里以使用清华源为例，不过之前在使用清华源安装一个机器学习类的第三方库里一直失败，切换为官方源后可以正常安装。所以可能在一些比较新的第三方库的更新时效性方面有点问题，不过常规使用应该问题不大。
```
# 1 在当前用户主目录下创建.pip文件夹
sudo mkdir ~/.pip
# 2 在~/.pip文件夹下创建pip.conf
sudo vi ~/.pip/pip.conf
输入以下内容后保存（如果不会使用vi的保存命令，请换用sudo gedit ~/.pip/pip.conf)：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```
---
![posts_2018-08-26-superset_setup_normal_pip](/img/superset_normal_setup/posts_2018-08-26-superset_setup_normal_pip.png)

* **Windows 下更换pip源的方法**
```
1. 在C:\Users\<当前用户名>目录下新建名为pip的文件夹
2. 新建txt文档，更名为pip.ini
3. 输入以下内容后保存:
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```
---

### 2.3 使用pip命令安装superset
```
# 如果提示[Errno 13] 权限不够，使用sudo chmod 777 -r <虚拟环境包所在文件夹>，再运行以下命令
pip3 install superset
```
### 2.4 superset 的配置与初始化

* 初始化superset app 并且创建登录账号、设置登录密码
superset 是基于flask-appbuilder，所以初始化指令使用fabmanager 命令
```
fabmanager create-admin --app superset
```
* 初始化database
默认是使用sqlite，一般使用可以先使用默认的配置，如果有特殊要求，可以在superset_config.py中进行配置
默认在主目录下创建.superset/superset.db文件
```
superset db upgrade
```
* 加载示例数据
此步骤可以略过
```
superset load_examples
```
* 初始化
```
superset runserver -d
```
![posts_2018-08-26-superset_setup_normal_run](/img/superset_normal_setup/posts_2018-08-26-superset_setup_normal_run.png)

## 3 开始使用superset
### 3.1 登录superset 
![posts_2018-08-26-superset_setup_login](/img/superset_normal_setup/posts_2018-08-26-superset_setup_login.png)

### 3.2 开始体验superset吧
![posts_2018-08-26-superset_setup_normal_experice](/img/superset_normal_setup/posts_2018-08-26-superset_setup_normal_experice.png)


![posts_2018-08-26-superset_setup_normal_pie](/img/superset_normal_setup/superset_setup_normal_pie.png)



