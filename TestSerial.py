# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/2/23 15:46
email:jid@hwtc.com.cn
description:
"""
import serial

if __name__ == '__main__':
    analyzer_serial = serial.Serial('COM3', 115200, timeout=1)

    cmd = b'MES,0\r'
    analyzer_serial.write(cmd)
    line = analyzer_serial.readlines()
    print(line)

    str = line[0].decode('utf-8')
    print(str)
    str = str.split(' ')
    print(str)
    str = str[1][0:-1]
    str = str.split(';')
    x = float(str[0]) / 10000
    y = float(str[1]) / 10000
    Lv = float(str[2])
    ret = (x, y, Lv)
    print(ret)
