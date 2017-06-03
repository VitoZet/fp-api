# coding: utf-8
from datetime import timedelta, datetime
from prestashop_api import PrestashopApi
from time import time

tic = time()

api_url = 'https://fisherpoint.ru/api'
api_key = ''

today = datetime.today()
thirty_days = timedelta(30)
quarter_days = timedelta(120)
year_days = timedelta(365)

last_thirty_days = today - timedelta(30)
last_quarter_days = today - timedelta(120)
last_year_days = today - timedelta(365)

api = PrestashopApi(api_url, api_key)
orders_date = api.get('orders/?display=full&filter[date_add]=>[' + str(last_year_days) + ']&date=1')

# print(orders_date['orders']['order'])
print('Количество заказов ' + str(len(orders_date['orders']['order'])))
toc = time()
print(toc-tic)