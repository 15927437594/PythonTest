# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/2/26
email:jid@hwtc.com.cn
description:单例模式
"""
import multiprocessing
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    @classmethod
    def instance(cls):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton()
        return Singleton._instance


def p1_start():
    s1 = Singleton.instance()
    print(id(s1))


def p2_start():
    s1 = Singleton.instance()
    print(id(s1))


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=p1_start)
    p2 = multiprocessing.Process(target=p2_start)
    p1.start()
    p2.start()
    p1_start()
    p2_start()
