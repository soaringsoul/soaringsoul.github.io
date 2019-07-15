---
layout:     post
title:      "pandas read_excel IndexError: list index out of range 解决办法 "
subtitle:   "pandas_read_excel_error_process"
date:       2019-07-15 12:36:05
author:     "soaringsoul"
header-img: "img/posts/default_post.jpg"
catalog: true
tags:
    - 数据处理
---





上午的时候，同事给我反馈我之前写的银行卡流水智能识别与计算程序运行错误，我看了下错误提示：

```IndexError: list index out of range```

银行卡流水智能识别与计算程序 是为解决风控审批过程中的授信额度问题而开发的一个数据策略类产品，分两个版本：一个针对线下风控人员使用，一个是针对线上风控审批平台使用。

针对 线下的风控人员使用的是把通过读取本地excel文件的形式来获取客户的个人信息和银行卡流水数据。以上这个运行错误就是个针对线下风控人员使用的版本。



我debug了下，发现是pandas 在read_excel时无法读取到excel文件的sheet,以至于出现以上问题。

通过**Stack Overflow** 搜索了下这个错误，也未找到答案。只能自己解决了：

先使用排除法，看是不是代码有bug:先通过把这个问题excel文件中的数据复制到新建excel文件中去，再启动计算程序，正常运行。



那就是这个excel文件本身的问题了，观察探索多次，无果。

最后另存为其他格式的时候发现了问题所在：

![pandas_read_excel_errror_process1](/img/posts/pandas_read_excel_errror_process1.png)



原来这个无法读取sheet的excel文件类型为`Stirct Open XML 电子表格(*.xlsx)`，pandas无法直接读取这类excel文件，把它另存为一般的.xlsx文件即可。

![pandas_read_excel_errror_process2](/img/posts/pandas_read_excel_errror_process2.png)