import configuration
import data

import requests

# Артемий Сальцин, 43 когорта, дипломный спринт
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.order_data)

def get_order_by_track(track):
    param = data.track_param.copy()
    param["t"] = track
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH, params=param)
