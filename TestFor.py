import datetime
import time

from hw_fixture_library.utils import int_to_four_byte, iterable_int_to_hex_str

if __name__ == '__main__':
    touch_case_dict = {0x27: 0, 0x28: 1, 0x29: 2, 0x5E: 3, 0x5F: 4}
    for case_id in touch_case_dict.keys():
        print(case_id)

    start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(start)

    print(len('HW-MSNCN10-T-0005'))
    data = [0, 32, 64, 96, 128, 160, 192, 224, 225]

    r = []
    for i in range(81):
        r.extend(data)
    print(r)
    print(len(r))

    g = []
    temp = []
    for j in range(9):
        for i in range(9):
            temp.append(data[j])

    for i in range(9):
        g.extend(temp)

    print(g)
    print(len(g))

    b = []
    for j in range(9):
        for i in range(81):
            b.append(data[j])

    print(b)
    print(len(b))

pass


def day_to_date(year, day):
    fir_day = datetime.datetime(year, 1, 1)
    zone = datetime.timedelta(days=day - 1)
    date = fir_day + zone
    return date.month, date.day


if __name__ == '__main__':
    month, day = day_to_date(22, 338)
    print(month, day)

    psn = "[>16P0296496VAAD33822V3839850011AN02936"
    sn = psn[-5:]
    print(sn)

    print(len("H97C7912005AA10020206202212220026"))

    print(len("LCD-EQ100-010002000100072023060100018420095"))

    print(len("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))

    red_data = []
    red_split_list = None

    a = "800~1100;680~880;750~950"
    if a.__contains__('mA'):
        b = a.replace('mA', '')
    else:
        b = a
    print(b)
    if b.__contains__(';'):
        red_split_list = b.split(';')
    print(red_split_list)

    for i in range(len(red_split_list)):
        if red_split_list[i].__contains__('~'):
            r = red_split_list[i].split('~')
            print(r)
            min_value = int(r[0])
            print(r[0])
            max_value = int(r[1])
            print(r[1])
            min_value = int_to_four_byte(int(min_value * 1000))
            red_data.extend(min_value)
            max_value = int_to_four_byte(int(max_value * 1000))
            red_data.extend(max_value)

    print(iterable_int_to_hex_str(red_data, ' '))

    minute = int((1800 - 1790) / 60)
    second = (1800 - 1790) % 60
    print(minute, second)


    print('' in ['HW-ICSCN07-T-0001'])

    print(len("18100002AA1022320042210080025"))
    print(len("115817232304120008"))
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(len(a))
