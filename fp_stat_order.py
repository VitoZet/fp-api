import prestashop_api
from prestashop_api import PrestashopApi


api_url = 'https://fisherpoint.ru/api'
api_key = ''

api = PrestashopApi(api_url, api_key)

# help(PrestashopApi)
res = api.get('orders', params={'limit':3, 'date': '2017-06-03'})
for p in res['orders']['order']:
    print(p['@id'], p['@xlink:href'])

# print(dir(res))
#     print(res['products']['product'])
#
#     product = api.get('products/'+p['@id'])
#     print(product['product']['name']['language']['#text'])
#     print('Проивзодитель:', product['product']['manufacturer_name']['#text'])
#     print('------------------------------------')