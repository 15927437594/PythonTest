# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/3/4 9:56
email:jid@hwtc.com.cn
description:
"""
import time

current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(current_time)
print(type(current_time))

time1 = time.time()
print(time1)
time.sleep(2)
time2 = time.time()
print(time2)
print(time2 - time1)
