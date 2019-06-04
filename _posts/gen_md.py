from datetime import date, datetime

today = date.today()
now = datetime.now()
now = datetime.strftime(now, format('%Y-%m-%d %H:%M:%S'))

result = []
lay_outs = """---
layout:     post
title:      "标题"
subtitle:   "{subtitle}"
date:       {format_date}
author:     "soaringsoul"
header-img: "img/posts/default_post.jpg"
catalog: true
tags:
    - 学习笔记
---
"""
input_file_name = input("please input file name:\n")

file_name = "{date}-{name}".format(date=today, name=input_file_name)
result.append(lay_outs.format(subtitle=input_file_name, format_date = now))
with open('%s.md' % file_name, 'w') as fw:
    fw.write('%s' % '\n'.join(result))
