import time

if __name__ == '__main__':
    touch_case_dict = {0x27: 0, 0x28: 1, 0x29: 2, 0x5E: 3, 0x5F: 4}
    for case_id in touch_case_dict.keys():
        print(case_id)

    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(start)

    print(len('HW-MSNCN10-T-0005'))
