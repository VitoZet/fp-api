# coding: utf-8

from prestashop_api import PrestashopApi

api_url = 'https://fisherpoint.ru/api'
api_key = ''

api = PrestashopApi(api_url, api_key)

res = api.get('products', params={'limit':2})

product = api.get('products/58')

print(product['product']['name']['language']['#text'])
# print(product['product']['link_rewrite']['language']['#text'])
# print(product['product']['description']['language']['#text'])
# print(product['product']['id'])
# print(product['product']['id_manufacturer']['#text'])
# print(product['product']['id_supplier']['#text'])
print(product['product']['manufacturer_name']['#text'])
print(product['product']['price'])
print(product['product']['date_add'])
