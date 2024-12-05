# # import time
# # def pros():
# #     for x in range(2*10**8,10*10**9):
# #         flag = True
# #         for i in range(2,int(x**0.5)+1):
# #             if x % i ==0 and i != x:
# #                 flag = False
# #         if flag and x > 9*10**8:
# #             yield x
# # start = time.time()
# # a=pros()
# # _=list(a)
# # print(_)
# # end = time.time()
# # print(end-start)
#
# from pybit import HTTP
# from datetime import datetime, timedelta
#
# # Создание сессии API
# session = HTTP(api_key='Ваш_API_KEY', api_secret='Ваш_SECRET_KEY')
# symbol = 'BTCUSDT'  # Замените на нужную вам пару
# ticker = session.get_tickers(symbol=symbol)
# current_price = ticker['result'][0]['lastPrice']
# print(f'Текущая цена {symbol}: {current_price}')
# # Получение времени три дня назад в формате timestamp
# three_days_ago = int((datetime.now() - timedelta(days=3)).timestamp() * 1000)
#
# # Получение исторических данных (свечей)
# kline_data = session.get_kline(symbol=symbol, interval='D', limit=3)
#
# if kline_data['result']:
#     price_three_days_ago = kline_data['result'][0]['close']
#     print(f'Цена три дня назад {symbol}: {price_three_days_ago}')
# else:
#     print('Нет данных для указанной даты.')
