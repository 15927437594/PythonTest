import random
import struct
import time
import datetime

import zcanpro

task_statue = True


def send_time(busID, mode=0, data=None):
    """
    :param busID:
    :param mode: 0-单次发送，1-循环发送
    :param data: None-读取系统当前时间
    :return:
    """
    global task_statue
    task_statue = True
    frm_id = 1
    while task_statue:
        if data is None:
            # data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            data = datetime.datetime.now()

        # zcanpro.write_log('time: ' + data)
        # time_ms = int(time.mktime(time.strptime(data, '%Y-%m-%d %H:%M:%S')) * 1000)
        # time_ms = struct.pack('>Q', time_ms)
        year = data.year - 2000
        month = data.month
        day = data.day
        hour = data.hour
        minute = data.minute
        second = data.second
        
        zcanpro.write_log('data: ' + str(data))
        zcanpro.write_log('f_id: ' + str(frm_id))
        frames = [
            {
                "can_id": 0x380,
                "is_canfd": 0,
                "canfd_brs": 0,
                "data": [year, month, day, hour, minute, second, frm_id, 0x00]
            },
            # {
            #     "can_id": 0x285,
            #     "is_canfd": 0,
            #     "canfd_brs": 0,
            #     "data": [frm_id, time_ms[4], time_ms[5], time_ms[6], time_ms[7], 0x00, 0x00, 0x00]
            # }
        ]
        zcanpro.write_log('frames: ' + str(frames))
        result = zcanpro.transmit(busID, frames)
        if not result:
            zcanpro.write_log("Transmit error!")
        else:
            zcanpro.write_log("Transmit success!")

        if mode == 0:
            task_statue = False

        frm_id += 1
        frm_id = frm_id % 16
        time.sleep(0.1)


def z_notify(operation, obj):
    zcanpro.write_log("Notify " + str(operation) + " " + str(obj))
    if operation == "stop":
        zcanpro.write_log("Stop...")
        global task_statue
        task_statue = False


def z_main():
    buses = zcanpro.get_buses()
    zcanpro.write_log("Get buses: " + str(buses))
    busID = buses[0]["busID"]

    # 读取系统时间 单次发送
    # send_time(busID)
    # 读取系统时间 循环发送
    # send_time(busID, mode=1)

    data = '2019-7-15 11:24:26'
    struct_time = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    # 自定义时间 单次发送
    # send_time(busID, data=struct_time)
    # 自定义时间 循环发送
    send_time(busID, mode=1, data=struct_time)


