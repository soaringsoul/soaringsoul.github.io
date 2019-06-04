---
layout:     post
title:      "What is PWA?"
subtitle:   "pwa学习小记"
date:       2018-10-22 17:36:28
author:     "soaringsoul"
header-img: "img/ubuntu_login.png"
catalog: true
tags:
    - 学习笔记
---

> PWA（Progressive Web App）是一种理念，使用多种技术来增强web app的功能，可以让网站的体验变得更好，能够模拟一些原生功能，比如通知推送。在移动端利用标准化框架，让网页应用呈现和原生应用相似的体验。
————from 百度百科


# 概述

了解`pwa`的动机是在fork的github.io模板中有一个名为pwa的文件夹，并且从代码来看，这个pwa还用在了github.io中。

通过查询到的资料并结合自己的github.io看来看，`pwa`主要功能就是离线缓存页面。



主要涉及两个关键文件：

1. manifest.json

	
	
		{
		  "name": "夜雨微寒的博客",
		  "short_name": "Soaringsoul Blog",
		  "description": "要有最朴素的生活与最遥远的梦想",
		  "icons": [{
		    "src": "icons/128.png",
		    "sizes": "128x128",
		    "type": "image/png"
		  }, {
		    "src": "icons/512.png",
		    "sizes": "512x512",
		    "type": "image/png"
		  }],
		  "background_color": "#fff",
		  "theme_color": "#000",
		  "start_url": "/",
		  "display": "standalone",
		  "orientation": "portrait"
		}


这个`json`文件主要用于控制手机端的显示 ，使网页在手机可以像打开APP一样的效果。

2. `sw.js`,Service Workers的缩写

功能：配置Web App离线功能，代码过长就不在这里展示了

# 实例说明

我在搭建自己的 [github.io博客](https://xugongli.github.io/)时，使用了 [https://github.com/Huxpro/huxpro.github.io](https://github.com/Huxpro/huxpro.github.io "Hux Blog")提供的Jekyll模板，作者在这个模板里使用到了PWA，我把这个示例过程写在知乎的一个回答里了，链接如下：


*  [PWA使用实例说明](https://www.zhihu.com/question/20223939/answer/516986071)
 