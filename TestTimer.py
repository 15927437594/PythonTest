# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/1/24 10:08
email:jid@hwtc.com.cn
description:
"""
import threading


class Test:
    def __init__(self):
        self.timer = threading.Timer(interval=2, function=self.test)
        self.timer.start()
        self.timer.cancel()
        self.timer = threading.Timer(interval=2, function=self.test)
        self.timer.start()

    def test(self):
        print('aaa')


if __name__ == '__main__':
    Test()
