import configuration
import requests
import data

#новый заказ (трек-номер)
def create_track():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)

#получаем значение трек-номера
def get_track():
    track = create_track().json()
    return str(track["track"])

#ищем заказ по трек-номеру

def check_order():
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_TRACK+'?t='+get_track())
response = check_order()
print(response.status_code)