import json
import os

import requests as requests


def login():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        url = 'http://10.8.1.20:80/' + 'sfcapi/auth/'
        response = requests.post(url=url, data=json.dumps({'name': 'decail', 'password': '123456'}), headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if response_json['status_code'] in (200, "200"):
                username = response_json['data']['user'].get('name')
                token = response_json['data']['token']
                print(token)
                token = token
                return_data = {
                    "command": 0x01,
                    "data": {"user": {
                        "name": username,
                        "realName": response_json['data']['user'].get('realName'),
                        "staffNo": response_json['data']['user'].get('staffNo'),
                        "role": response_json['data']['roles'][0].get('name'),
                        "token": token
                    },
                        "status_code": 200,
                        "message": "登录成功",
                    }
                }
                return token
            else:
                return {'command': 0x01,
                        'data': {"user": {}, "message": response_json, "status_code": response_json['status_code']}}
        else:
            return {'command': 0x01,
                    'data': {"user": {}, "message": response.content, "status_code": response.status_code}}
    except requests.exceptions.ConnectionError as e:
        return {'command': 0x01, 'data': {"user": {}, "message": str(e.args), "status_code": 404}}


def iqc_test_report(data, token):
    url = 'http://10.8.1.20:80/' + 'sfcapi/1.0/iqc-testreport/'
    print('iqc_test_report url=%s, data=%s' % (url, data))
    try:
        print('token=', token)
        headers = {"Authorization": "Bearer %s" % token}
        response = requests.post(url=url, data=data, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print('iqc_test_report status_code=%s, response_json=%s' % (status_code, response_json))
        return response_json
    except requests.exceptions.ConnectionError as e:
        print('iqc_test_report exception: %s' % str(e.args))
        return {'status_code': 500, 'message': str(e.args)}


token = login()
path = os.path.join(os.getcwd())
sn_list = []
for root, _, files in os.walk(path):
    for file_name in files:
        print(root, file_name)
        file_path = os.path.join(root, file_name)
        sheet_name = root.split('\\')[1]
        with open(file_path, encoding='utf8') as file:
            lines = file.readlines()
            row = 0
            for line in lines:
                line = line.strip()
                line = line.replace('\r', '')
                line = line.replace('\n', '')
                if len(line) > 0:
                    row = row + 1
                    temp = line.split('&')
                    sn = temp[0]
                    items = temp[1]
                    items = items.replace('[', '')
                    items = items.replace(']', '')
                    items = items.replace('\'', '\"')
                    items = items.replace('True', 'true')
                    items = items.replace('False', 'false')
                    items = items.replace('},', '}&')
                    items = items.split('&')
                    sn_list.append(sn)
                    report_case_list = []
                    is_ok = True
                    for item in items:
                        a = json.loads(item)
                        print(a)
                        if not a['测试结果']:
                            is_ok = False
                        case_data = {"item": a['测试名称'], "check": a['测试结果'], "sample": a['测试值'], "standard": a['测试标定值']}
                        report_case_list.append(case_data)
                    data = {'sn': sn[:21], "isok": is_ok, 'result': report_case_list}
                    iqc_test_report(data=json.dumps(data), token=token)
