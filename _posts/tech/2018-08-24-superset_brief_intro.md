---
layout:     post
title:      "自助数据分析平台-Superset简介"
subtitle:   "Superset简介"
date:       2018-08-24 18:30:00
author:     "soaringsoul"
header-img: "img/superset/superset_m.jpg"
catalog: true
tags:
    - 精选开源项目
---




> 工欲善其事，必先利其器。


> Apache Superset (incubating) is a modern, enterprise-ready business intelligence web application


以上是Superset 官网对superset的简介，翻译一下：


> Superset是一个是一个现代化的企业级商业智能Web平台


web application 的直译应该是 web应用程序，但是我觉着Superset应该是一个平台，而非一个应用程序。
因为Superset提供的功能决定了这是一个可以满足多人协作的数据分析平台，而非一个简单的数据分析应用程序。
## 1.Superset是什么？提供了哪些功能？

让我们先来看一下Superset官网上对其提供的功能所作的说明：

*   An intuitive interface to explore and visualize datasets, and create interactive dashboards.
*   A wide array of beautiful visualizations to showcase your data.
*   Easy, code-free, user flows to drill down and slice and dice the data underlying exposed dashboards. The dashboards and charts acts as a starting point for deeper analysis.
*   A state of the art SQL editor/IDE exposing a rich metadata browser, and an easy workflow to create visualizations out of any result set.
*   An extensible, high granularity security model allowing intricate rules on who can access which product features and datasets. Integration with major authentication backends (database, OpenID, LDAP, OAuth, REMOTE_USER, ...)
*   A lightweight semantic layer, allowing to control how data sources are exposed to the user by defining dimensions and metrics
*   Out of the box support for most SQL-speaking databases
*   Deep integration with Druid allows for Superset to stay blazing fast while slicing and dicing large, realtime datasets
*   Fast loading dashboards with configurable caching

翻译一下并加上我个人的一些使用体会：
* **提供一个直观的数据挖掘和数据可视化的交互界面，并且可以建立一套可交互的 Dashboards。**
 通过Superset可以与各种主流的数据库，如sqlserver、mysql等进行实时交互，并且可以对数据表进行即时的可视化，支持建立Dashboards（看板）功能。

* **提供一套美观的数据可视化图表**，superset提供了一套基于d3.js的数据可视化解决方案，也可以通过二次开发加入一些诸如echarts,antv等数据化图表，但开发起来比较有难度，建议学习一下d3.js的知识，在d3的基础上作修改。
* **简单，即使无代码基础的用户也可以通过对数据的拖曳完成slice(可以理解 为图表）和Dashbord的制作，为进一步的数据挖掘提供可视化分析的基础**
* **可以作为一个优雅的SQL IDE，运行sql指令从数据库提数，并且可以对查询结果进行实时的可视化**
* **高粒度权限控制体系，通过基于flask-appbuilder的权限设计，可以对各个数据集和dashbord的访问设计权限**
* **轻量级语义层设计，允许通过定义维度和指标来控制数据源向用户公开的方式**
* **开箱即用，支持大部分数据库语言**
* **与Druid深度集成，可快速处理海量数据**
* **缓存配置设计，可快速加载Dashboards**

## 2.Superset解决了什么问题？
* 动态Dashboards，可对数据库中的数据进行动态可视化，以满足监控或者研究的需要
![bank_dash](/img/superset/bank_dash.png)

* 支持目前主流的大多数sql语言，可以对各种数据库进行动态查询、管理与可视化
![sqllab](/img/superset/sqllab.png)

* 开箱即用的数据可视化解决方案
*
![explore](/img/superset/explore.png)
