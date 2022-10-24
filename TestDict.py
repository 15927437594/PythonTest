# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/5/11 20:20
email:jid@hwtc.com.cn
description:
"""
if __name__ == '__main__':
    station_dict = {}
    station_dict.update({'LCMCN02_EOL': 1})
    station_dict.update({'ACSCN02_EOL': 1})
    station_dict.update({'ICSCN07_EOL': 1})

    if 'HW-ICSCN07-T-0004' in station_dict.keys() or 'ICSCN07_EOL' in station_dict.keys():
        print(station_dict['ICSCN07_EOL'])
