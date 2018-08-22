#!/usr/bin/python3
import pprint
from bitrix24 import bitrix24
import sys
import subprocess
b24_webhook_key = 'some_key'
b24_webhook_user = 1
b24_domain = 'some_domain'
page = 1
user_id = [16, 10, 6, 55, 8, 14, 67, 20, 40, 85, 87, 28, 12, 61, 50, 1]
ord_status = 5
order_list = 0
total_orders = 0
bx24 =  bitrix24.Bitrix24(b24_domain, webhook_key=b24_webhook_key, webhook_user=b24_webhook_user)

def get_order_list_len(_user_id):
    result_ = bx24.call(
    'task.item.list',
    {'ORDER': {'DEADLINE': 'desc'}},
    {'FILTER': {'RESPONSIBLE_ID': _user_id,'REAL_STATUS': ord_status}},
    {'PARAMS': {'NAV_PARAMS': {'nPageSize': 50, 'iNumPage': page}}}
)

    if result_:
        return (len(result_['result']))

for user in user_id:
    while True:
        order_list = get_order_list_len(user)
        total_orders = total_orders + order_list
        page = page + 1
        if(order_list < 50):
            subprocess.call("mosquitto_pub -t /devices/%s/controls/orders_finished/on  -r  -m %s" % (user, total_orders), shell=True)
            page = 1
            total_orders = 0
            break