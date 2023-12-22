# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/3/23 15:01
email:jid@hwtc.com.cn
description:
"""


def remove_underline(src_sn):
    if '_' in src_sn:
        index = src_sn.index('_')
        dst_sn = src_sn[:index]
        return dst_sn
    return src_sn


if __name__ == '__main__':
    sn = remove_underline(src_sn='30101028110A5M2230472_02_')
    print(sn)

    data = {
        "device": "HWTV01",
        "data": [
            {
                "cumulative_process_number": 1243,
                "time": "2023-11-24 15:39:28"
            },
            {
                "device_name": "HWTV01",
                "time": "2023-11-24 15:39:28"
            },
            {
                "machine_coordinate_x": 420,
                "time": "2023-11-24 15:39:28"
            },
            {
                "machine_coordinate_y": 0,
                "time": "2023-11-24 15:39:28"
            },
            {
                "machine_coordinate_z": 0,
                "time": "2023-11-24 15:39:28"
            },
            {
                "main_program_number": "O3K-03.NC",
                "time": "2023-11-24 15:39:28"
            },
            {
                "warning_info": "null",
                "time": "2023-11-24 15:39:28"
            },
            {
                "work_status": 4,
                "time": "2023-11-24 15:39:28"
            },
            {
                "work_status_display": "完工",
                "time": "2023-11-24 15:39:28"
            },
            {
                "z_axis_speed": 0,
                "time": "2023-11-24 15:39:28"
            }
        ]
    }

    a = {}
    device = data.get('device', "")
    info = data.get('data', [])
    for item in info:
        print(item)
        for i in item.keys():
            a.update({i: item[i]})
    print(a)
