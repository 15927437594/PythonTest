# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/2/26
email:jid@hwtc.com.cn
description:单例模式
"""


class S:
    instance = None

    def __new__(cls, *args, **kwargs):
        if S.instance is None:
            S.instance = super().__new__(cls)

    def __init__(self):
        pass


s1 = S()
print(id(s1))
s2 = S()
print(id(s2))
s3 = S()
print(id(s3))
s4 = S()
print(id(s4))
