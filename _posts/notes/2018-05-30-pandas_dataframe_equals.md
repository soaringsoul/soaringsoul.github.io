---
layout:     post
title:      "判断pandas的两个DataFrame是否相同"
subtitle:   "pandas使用速记"
date:       2018-04-24 21:00:00
author:     ""
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 编程速记
---

# 官网说明
语法：

	DataFrame.equals(other)[source]
用途：

Determines if two NDFrame objects contain the same elements. NaNs in the same location are considered equal.

即比较两个dataframe是否相同。NaN值所在的位置也必须完全相同才会认定两者一一致。

# 使用示例

```
results = df1.equals(df2)
results取值：True or False
```