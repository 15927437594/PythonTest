import os

os.system('chcp 65001')
for i in range(1, 255):
    ip = '10.8.7.' + str(i)
    response = os.system("ping -n 1 " + ip)
    # print(response)
    if response == 0:
        print(ip, 'is up')
    else:
        print(ip, 'is down')
