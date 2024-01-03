# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/3/4 9:01
email:jid@hwtc.com.cn
description:
"""
import csv

if __name__ == '__main__':
    print(pow(9.329000, 6))
    print(9.329000 + 0.01)
    print((9.329000 * 100000 + 0.01 * 100000) / 100000)
    data = ['工站', "产品SN", '动作/测试项', '耗时', '开始时间', '结束时间']
    f = open('Test.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(data)
    writer.writerow(data)
    writer.writerow(data)
    writer.writerow(data)
    writer.writerow(data)
    writer.writerow(data)
    writer.writerow(data)
