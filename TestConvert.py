# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/10/26 16:25
email:jid@hwtc.com.cn
description:
"""
import datetime
import time


def convert_capacitance_to_angle(p1, p2, capacitance):
    return 90 / (p2 - p1) * capacitance + 90 * p1 / (p1 - p2)


if __name__ == '__main__':
    p1 = 50
    p2 = 200
    capacitance = 120
    angle = convert_capacitance_to_angle(p1, p2, capacitance)
    print(angle)

    a = int(str(0x0025), 16)
    print(a)
    print(0x0025)

    data = datetime.datetime.now()
    print(data.month)
    data = '2019-7-15 11:24:26'
    struct_time = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    print(struct_time.year)
