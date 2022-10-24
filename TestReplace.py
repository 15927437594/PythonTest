# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/6/28 21:13
email:jid@hwtc.com.cn
description:
"""
import json
import time


def sub(string, p, c):
    new = []
    for s in string:
        new.append(s)
    new[p] = c
    return ''.join(new)


if __name__ == '__main__':
    s = sub('X01-790000128BK2262800001M04', -9, '1')
    print(s)
    a = str([15999, 0])
    print(a)
    data = {'sn': '[>16P0257869VAAD17422V38398SQ011AN00175', 'check_md5': '5ddfa746063b14a2b75ce04eecc54820',
            'result': [
                {'item': '短路电流检测[mA]', 'check': True, 'sample': '287.35', 'rawdata': [1, 0, 4, 98, 120, 0, 0, 0, 0]},
                {'item': 'CAN1检测', 'check': True, 'sample': '', 'rawdata': [1, 1, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'CAN2检测', 'check': True, 'sample': '', 'rawdata': [1, 1, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'NIO零件版本检测', 'check': True, 'sample': 'P0257869 AA',
                 'rawdata': [1, 80, 48, 50, 53, 55, 56, 54, 57, 32, 65, 65]},
                {'item': '软件版本检测', 'check': True, 'sample': 'P0089261 AS',
                 'rawdata': [1, 80, 48, 48, 56, 57, 50, 54, 49, 32, 65, 83]},
                {'item': 'Base马达温度采集检测[°C]', 'check': True, 'sample': '26.00', 'rawdata': [1, 66, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'Base-X板温度采集检测[°C]', 'check': True, 'sample': '26.00',
                 'rawdata': [1, 66, 0, 0, 0, 0, 0, 0, 0]},
                {'item': '工作电压检测[V]', 'check': True, 'sample': '11.17', 'rawdata': [1, 43, 160, 0, 0, 0, 0, 0, 0]},
                {'item': '工作电流检测[mA]', 'check': True, 'sample': '287.68', 'rawdata': [1, 0, 4, 99, 188, 0, 0, 0, 0]},
                {'item': '静态电流检测[mA]', 'check': True, 'sample': '0.03', 'rawdata': [1, 0, 0, 0, 28, 0, 0, 0, 0]},
                {'item': 'Base马达和转动角度检测', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': '内部ECU自检异常检测', 'check': True, 'sample': '', 'rawdata': [1, 0, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'AMOLED驱动IC故障检测', 'check': True, 'sample': '', 'rawdata': [1, 0, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'Motor低速故障检测', 'check': True, 'sample': '', 'rawdata': [1, 0, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'AMOLED温度超阈值检测', 'check': True, 'sample': '', 'rawdata': [1, 0, 0, 0, 0, 0, 0, 0, 0]},
                {'item': 'LVDS视频信号丢失检测', 'check': True, 'sample': '', 'rawdata': [1, 0, 0, 0, 0, 0, 0, 0, 0]},
                {'item': '屏幕显示检测 - 红画面', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': '屏幕显示检测 - 绿画面', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': '屏幕显示检测 - 蓝画面', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': '屏幕显示检测 - 黑画面', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': '屏幕显示检测 - 白画面', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': '屏幕显示检测 - 特殊画面', 'check': True, 'sample': '', 'rawdata': ''},
                {'item': 'Base马达归位检测', 'check': True, 'sample': '', 'rawdata': [1, 0, 0, 0, 0, 0, 0, 0, 0]}]}
    a = json.dumps(data)
    print(a)

    millis = int(round(time.time() * 1000))
    print(millis)
