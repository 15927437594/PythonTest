# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/2/23 15:46
email:jid@hwtc.com.cn
description:
"""
import os
import time

import serial

if __name__ == '__main__':
    # analyzer_serial = serial.Serial('COM3', 115200, timeout=1)
    #
    # cmd = b'MES,0\r'
    # analyzer_serial.write(cmd)
    # line = analyzer_serial.readlines()
    # print(line)
    #
    # str = line[0].decode('utf-8')
    # print(str)
    # str = str.split(' ')
    # print(str)
    # str = str[1][0:-1]
    # str = str.split(';')
    # x = float(str[0]) / 10000
    # y = float(str[1]) / 10000
    # Lv = float(str[2])
    # ret = (x, y, Lv)
    # print(ret)

    capture_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print(capture_time)

    sn = 'dshugiawfbiesgb.wav'

    if sn.__contains__('.'):
        sn = sn.split('.')[0]

    record_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

    backup_path = os.path.join(os.getcwd(), 'backup')
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    filename = os.path.join(backup_path, '%s_%s.wav' % (sn, record_time))
    print(filename)
