"""
user: Created by jid on 2023/4/13 20:25
email: jid@hwtc.com.cn
description: 
"""
import operator

import requests
from hw_fixture_library.utils import high_low_to_int


def get_error_message(error_type, error_code):
    try:
        url = "http://hq.hwauto.com.cn:45678/app/fixture/error_message?error_id=%d&error_code=%d" % (
        error_type, error_code)
        response = requests.get(url=url)
        status_code = response.status_code
        print(status_code)
        if status_code==200:
            response_json = response.json()
            print(response_json)
            if len(response_json) == 1:
                error_message = response_json[0]['info']
            else:
                error_message = error_code
        else:
            error_message = error_code
    except Exception as e:
        error_message = error_code
        print('get_error_message exception: %s' % str(e.args))
    return error_message

if __name__ == '__main__':
    error_message = get_error_message(5, 1234)
    print(error_message)
    print(type(error_message))
    if operator.eq(type(error_message), int):
        error_message = '0x%04X' % error_message

    print(error_message)


    a = high_low_to_int(0x39, 0x00)
    print(a)

    value = ((0x00 << 8) | (0x39 & 0xFF)) * 10
    print(value)