# coding: utf-8

from prestashop_api import PrestashopApi

api_url = 'https://fisherpoint.ru/api'
api_key = ''

api = PrestashopApi(api_url, api_key)

# res = api.get('orders', params={'limit':2})

order = api.get('orders/9389')

state = api.get('order_states/'+order['order']['current_state']['#text'])['order_state']['name']['language']['#text']

print(order['order']['id'])
print(order['order']['date_add'])
print(order['order']['total_products'])
print(order['order']['total_shipping'])
# print(order['order']['associations'])
print(order['order']['associations']['order_rows']['order_row']['product_name'])
print(order['order']['current_state']['@xlink:href'])
print(order['order']['current_state']['#text'])
# print(order['order']['associations']['product_name'])
# print(order['order']['invoice_date'])
print(state)