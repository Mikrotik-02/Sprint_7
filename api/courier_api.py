import requests

from urls import BASE_URL, CREATE_COURIER, LOGIN_COURIER


class CourierAPI:
    def create_courier(self, payload):
        response = requests.post(BASE_URL + CREATE_COURIER, json=payload)
        return response

    def login_courier(self, payload):
        response = requests.post(BASE_URL + LOGIN_COURIER, json=payload)
        return response
