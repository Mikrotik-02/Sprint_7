import requests

from urls import BASE_URL, CREATE_ORDER, GET_ORDERS


class OrderAPI:
    def create_order(self, payload):
        response = requests.post(BASE_URL + CREATE_ORDER, json=payload)
        return response

    def get_orders(self):
        response = requests.get(BASE_URL + GET_ORDERS)
        return response
