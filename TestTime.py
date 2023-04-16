# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/3/4 9:56
email:jid@hwtc.com.cn
description:
"""
import datetime
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

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


def day_to_date(year, day):
    fir_day = datetime.datetime(year, 1, 1)
    zone = datetime.timedelta(days=day - 1)
    date = fir_day + zone
    return date.month, date.day


if __name__ == '__main__':
    month, day = day_to_date(22, 309)
    print(month, day)
