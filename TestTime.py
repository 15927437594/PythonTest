# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/3/4 9:56
email:jid@hwtc.com.cn
description:
"""
import datetime
import operator
import os
import threading
import time


# current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# print(current_time)
# print(type(current_time))
#
# time1 = time.time()
# print(time1)
# time.sleep(2)
# time2 = time.time()
# print(time2)
# print(time2 - time1)
#
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


def day_to_date(year, day):
    fir_day = datetime.datetime(year, 1, 1)
    zone = datetime.timedelta(days=day - 1)
    date = fir_day + zone
    return date.month, date.day


if __name__ == '__main__':
    # month, day = day_to_date(22, 309)
    # print(month, day)

    def get_timestamp():
        timestamp = int(round(time.time() * 1000))
        return timestamp


    print(get_timestamp())

    # data = [{
    #     "设备名": "HWTV01",
    #     "报警信息": "",
    #     "主程序号": "O3K-00.NC",
    #     "机器坐标X": 65,
    #     "机器坐标Y": -258,
    #     "机器坐标Z": -364,
    #     "工作状态": "暂停",
    #     "累计加工数": 1209,
    #     "Z轴转速": 7998
    # }, {
    #     "设备名": "HWTV02",
    #     "报警信息": "",
    #     "主程序号": "7777",
    #     "机器坐标X": 199,
    #     "机器坐标Y": -348,
    #     "机器坐标Z": -476,
    #     "工作状态": "加工",
    #     "累计加工数": 2396,
    #     "Z轴转速": 7503
    # }]
    #
    # for item in data:
    #     print(f'MQTTGateway receive payload: {item}')
    #     sn = item.get('设备名', "")
    #     print(sn)
    #     print(item)

    a = "H97C_BURN-ME02-01"
    if a.__contains__("_"):
        split = a.split('_')
        print(split)
        if len(split) == 2:
            station_code = split[1]
            print(station_code)
        elif len(split) == 3:
            station_code = split[2]
            print(station_code)
    print(station_code)


    def update_vds_state():
        if vds_status:
            print("VDS已连接")
        else:
            print("VDS未连接")

    threading.Timer(interval=0.2, function=update_vds_state).start()
    vds_status = True
    cmd = 'adb shell'
    os.system(cmd)
    output = os.popen(cmd).readlines()
    print(output)
    print(type(output))
    if operator.eq(list, type(output)) and len(output) == 0:
        vds_status = False


