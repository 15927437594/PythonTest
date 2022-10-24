# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/3/12 13:02
email:
description:
"""
import datetime
import operator
import socket
import uuid

import netifaces


def int_to_four_byte(value):
    src_bytes = []
    first = ((value >> 24) & 0xff)
    second = ((value >> 16) & 0xff)
    third = ((value >> 8) & 0xff)
    forth = (value & 0xff)
    src_bytes.append(first)
    src_bytes.append(second)
    src_bytes.append(third)
    src_bytes.append(forth)
    return src_bytes


def get_host_ip():
    host_name = socket.gethostname()
    socket.gethostname()
    ip_list = socket.getaddrinfo(host_name, None)
    for ip in ip_list:
        print(ip[0].imag)


if __name__ == '__main__':
    # src_bytes = int_to_four_byte(350000)
    # print(src_bytes)

    # internal_ip = socket.gethostbyname(socket.gethostname())
    # if internal_ip is not None and not operator.eq('', internal_ip):
    #     print(internal_ip)

    # routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    # print(routingGateway)
    # gateway_list = routingGateway.split('.')
    # ip_mark = gateway_list[0]+'.'+gateway_list[1]+'.'+gateway_list[2]
    # print(ip_mark)

    routing_gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    print('routing_gateway=', routing_gateway)
    if routing_gateway is not None and not operator.eq('', routing_gateway):
        if '192.168' in routing_gateway:
            gateway_list = routing_gateway.split('.')
            ip_mark = gateway_list[0] + '.' + gateway_list[1] + '.' + gateway_list[2]
            host_name = socket.gethostname()
            ip_list = socket.getaddrinfo(host_name, None)
            for ip in ip_list:
                if ip_mark in ip[4][0]:
                    current_ip = ip[4][0]
                    print(current_ip)
        else:
            internal_ip = socket.gethostbyname(socket.gethostname())
            print(internal_ip)
            if internal_ip is not None and not operator.eq('', internal_ip):
                current_ip = internal_ip
                print(current_ip)

    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    print(mac)

    psn = '[>16P0211978VAHD12922V38398S0001X1N00322'
    date = psn[16:21]
    serial_number = psn[35:]
    day = int(date[:3])
    year = int(date[3:])
    print(date)
    print(serial_number)
    print(day)
    print(year)

    time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    print(time + '-middle.png')

