# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/2/26
email:jid@hwtc.com.cn
description:单例模式
"""
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


s1 = Singleton().instance()
print(id(s1))
s2 = Singleton().instance()
print(id(s2))
s3 = Singleton().instance()
print(id(s3))
s4 = Singleton().instance()
print(id(s4))
