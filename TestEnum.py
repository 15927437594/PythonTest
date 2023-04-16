# -*- coding: utf-8 -*-
"""
user:Created by jid on 2022/5/8 19:23
email:jid@hwtc.com.cn
description:
"""
from enum import Enum


class HWMesMode(Enum):
    PRODUCT = 0x00  # 生产服务器
    DEBUG = 0x01    # 测试服务器


if __name__ == '__main__':
    mes_mode = HWMesMode(0x01)
    print(mes_mode)
