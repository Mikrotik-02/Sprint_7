import allure
import requests

from urls import BASE_URL, CREATE_COURIER, LOGIN_COURIER


class CourierAPI:
    @allure.step("Создание курьера")
    def create_courier(self, payload):
        response = requests.post(BASE_URL + CREATE_COURIER, json=payload)
        return response

    @allure.step("Логин курьера")
    def login_courier(self, payload):
        response = requests.post(BASE_URL + LOGIN_COURIER, json=payload)
        return response

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(BASE_URL + CREATE_COURIER + f"/{courier_id}")
        return response
