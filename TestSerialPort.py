# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/8/25 13:54
email:jid@hwtc.com.cn
description:
"""
import threading

import serial


def start_read_serial():
    self.scheduler.enter(0.5, 1, self.read_serial_data)
    thread = threading.Thread(target=self.scheduler.run)
    thread.setDaemon(True)
    thread.start()


def read_serial_data(self):
    try:
        if self.analyzer_serial.is_open:
            data = self.analyzer_serial.read_all()
            if len(data) > 0:
                print('read_serial_data data: %s', data)
                self.analysis_measure_data(data)
            self.scheduler.enter(0.5, 1, self.read_serial_data)
    except Exception as e:
        print('read_serial_data -> %s' % str(e.args))


if __name__ == '__main__':
    burn_serial = serial.Serial(port='COM15', baudrate=9600, timeout=1)
    start_read_serial()
