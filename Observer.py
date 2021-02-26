# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/2/26
email:jid@hwtc.com.cn
description:观察者模式
"""


class Observer:
    """
    观察者
    """

    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(self.name + "收到信息：" + msg)


class Subject:
    """
    主题
    """

    def __init__(self):
        self.observers = []

    def add_observers(self, observer: Observer):
        if observer in self.observers:
            return print('observer already in observers')
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer not in self.observers:
            return print('observer not in observers')
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


xiao_ming = Observer("XiaoMing")
li_hua = Observer("LiHua")
rain = Subject()
# 添加订阅
rain.add_observers(xiao_ming)
rain.add_observers(li_hua)
rain.notify("下雨了！")
# 取消订阅
rain.remove_observer(li_hua)
rain.notify("打雷了！")
