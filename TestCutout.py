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
