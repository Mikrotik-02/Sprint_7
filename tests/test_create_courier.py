import allure
import pytest

from api.courier_api import CourierAPI


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание курьера")
class TestCreateCourier:
    courier_api = CourierAPI()

    @allure.title("Создание курьера")
    @allure.description("Проверяет, что курьера можно создать с валидными данными.")
    def test_create_courier_success(self, courier_payload):
        response = self.courier_api.create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание двух одинаковых курьеров")
    @allure.description("Проверяет, что нельзя создать двух курьеров с одинаковыми данными.")
    def test_create_two_same_couriers_returns_error(self, courier_payload):
        first_response = self.courier_api.create_courier(courier_payload)
        second_response = self.courier_api.create_courier(courier_payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }

    @pytest.mark.parametrize("required_field", ["login", "password"])
    @allure.title("Создание курьера без обязательного поля")
    @allure.description("Проверяет, что запрос без обязательного поля возвращает ошибку.")
    def test_create_courier_without_required_field_returns_error(self, courier_payload, required_field):
        payload_without_required_field = courier_payload.copy()
        payload_without_required_field.pop(required_field)

        response = self.courier_api.create_courier(payload_without_required_field)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }
