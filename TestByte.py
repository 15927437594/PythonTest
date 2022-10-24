# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/3/24 10:58
email:jid@hwtc.com.cn
description:
"""
import datetime


def four_byte_high_low_to_int(first, second, third, forth):
    """
    将四个字节的高低位转化为整数
    :param first:
    :param second:
    :param third:
    :param forth:
    :return:
    """
    value = forth | (third << 8) | (second << 16) | (first << 24)
    return value


def dayToDate(year, day):
    fir_day = datetime.datetime(year, 1, 1)
    zone = datetime.timedelta(days=day - 1)
    date = fir_day + zone
    return date.month, date.day


if __name__ == '__main__':
    psn = 'P0211978AG09622V38398N001100001'
    write_psn = []
    print(psn[10:15])
    print(psn[26:])
    date = psn[10:15]
    serial_number = psn[26:]
    day = int(date[:3])
    print(day)
    year = int(date[3:])
    print(year)
    month, day = dayToDate(year, day)
    print(month, day)
    write_psn.append(0x03)
    write_psn.extend([year, month, day])
    for i in serial_number:
        write_psn.append(int(i))
    write_psn.append(0x00)
    print(len(write_psn))
    print(write_psn)
