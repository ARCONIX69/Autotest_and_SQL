import data
import configuration
import requests

# Функция на создание заказа
def post_create_order(body):
        return requests.post(url=configuration.URL + configuration.CREATE_ORDERS,
                                            json=body)

# Функция на сохранения номера заказа

def save_track():
    order_track = post_create_order(data.create_orders)
    order_track_number= order_track.json()["track"]
    return order_track_number

# Функция на получения заказа по трек номеру

def get_order ():
    track = save_track()
    return requests.get(configuration.URL + configuration.GET_ORDERS + str(track))




