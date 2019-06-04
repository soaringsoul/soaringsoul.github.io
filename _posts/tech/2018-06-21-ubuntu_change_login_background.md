---
layout:     post
title:      "ubuntu18.04美化之更换登录背景"
subtitle:   "ubuntu18.04美化"
date:       2018-06-21 21:00:00
author:     "soaringsoul"
header-img: "img/ubuntu_login.png"
catalog: true
tags:
    - 技术教程
---
# ubuntu 更换登录背景
1.准备一张与当前显示器分辨率一致的图片，复制到:
 > /usr/share/backgrounds/
 
 2.编辑配置文件 /etc/alternatives/gdm3.css,找到
 
```
 sudo vim /etc/alternatives/gdm3.css
```
找到

```
#lockDialogGroup {                                                               
  background: #2c001e url(resource:///org/gnome/shell/theme/noise-texture.png); 
  background-repeat: repeat; }
  
```

替换为

```
#lockDialogGroup {
  background: #2c001e url(file:///usr/share/backgrounds/mypaper.jpg);
  background-repeat: repeat;
  # 我的电脑分辨率是1920x1080所以将background-size设置为 1920px 1080px
  background-size: 1920px 1080px; 
  background-position: center;
 }

```

3.重启，效果预览

![修改完成后的登录界面](/img/ubuntu_login_done.jpg  "修改完成后的登录界面")

4.涉及css3语法学习笔记

* background-size:规定背景图像的尺寸：
```
div
{
background:url(img_flwr.gif);
background-size:80px 60px;
background-repeat:no-repeat;
}
```
>语法：
```
background-size: length|percentage|cover|contain;
```
```
length	设置背景图片高度和宽度。第一个值设置宽度，第二个值设置的高度。如果只给出一个值，第二个是设置为 auto(自动)
percentage	将计算相对于背景定位区域的百分比。第一个值设置宽度，第二个值设置的高度。如果只给出一个值，第二个是设置为"auto(自动)"
cover	此时会保持图像的纵横比并将图像缩放成将完全覆盖背景定位区域的最小大小。
contain	此时会保持图像的纵横比并将图像缩放成将适合背景定位区域的最大大小。
```
* background-repeat:设置如何平铺对象的 background-image 属性。默认情况下，重复background-image的垂直和水平方向。
```
{
background-image:url('paper.gif');
background-repeat:repeat-y;
}
```
>语法参数说明
```
repeat	背景图像将向垂直和水平方向重复。这是默认
repeat-x	只有水平位置会重复背景图像
repeat-y	只有垂直位置会重复背景图像
no-repeat	background-image不会重复
inherit	指定background-repea属性设置应该从父元素继承
```


