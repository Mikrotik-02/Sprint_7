import allure
import pytest

from api.courier_api import CourierAPI
from helpers.generators import generate_courier_payload


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание курьера")
class TestCreateCourier:
    courier_api = CourierAPI()

    def delete_created_courier(self, payload):
        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        login_response = self.courier_api.login_courier(login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                self.courier_api.delete_courier(courier_id)

    @allure.title("Создание курьера")
    @allure.description("Проверяет, что курьера можно создать с валидными данными.")
    def test_create_courier_success(self):
        payload = generate_courier_payload()

        try:
            response = self.courier_api.create_courier(payload)

            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            self.delete_created_courier(payload)

    @allure.title("Создание двух одинаковых курьеров")
    @allure.description("Проверяет, что нельзя создать двух курьеров с одинаковыми данными.")
    def test_create_two_same_couriers_returns_error(self):
        payload = generate_courier_payload()

        try:
            first_response = self.courier_api.create_courier(payload)
            second_response = self.courier_api.create_courier(payload)

            assert first_response.status_code == 201
            assert second_response.status_code == 409
            assert second_response.json() == {
                "code": 409,
                "message": "Этот логин уже используется. Попробуйте другой."
            }
        finally:
            self.delete_created_courier(payload)

    @pytest.mark.parametrize("required_field", ["login", "password"])
    @allure.title("Создание курьера без обязательного поля")
    @allure.description("Проверяет, что запрос без обязательного поля возвращает ошибку.")
    def test_create_courier_without_required_field_returns_error(self, required_field):
        payload = generate_courier_payload()
        payload_without_required_field = payload.copy()
        payload_without_required_field.pop(required_field)

        try:
            response = self.courier_api.create_courier(payload_without_required_field)

            assert response.status_code == 400
            assert response.json() == {
                "code": 400,
                "message": "Недостаточно данных для создания учетной записи"
            }
        finally:
            self.delete_created_courier(payload)
