"""
user: Created by jid on 2022/12/31 20:25
email: jid@hwtc.com.cn
description: 
"""
import time

if __name__ == '__main__':
    for i in range(10000):
        time.sleep(3)
        print('sleep 3s', time.asctime())
