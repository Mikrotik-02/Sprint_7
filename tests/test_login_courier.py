import allure

from api.courier_api import CourierAPI
from data.courier_data import CourierData


@allure.epic("API Яндекс Самокат")
@allure.feature("Логин курьера")
class TestLoginCourier:
    def setup_method(self):
        self.courier_api = CourierAPI()

    def _get_login_payload(self, courier_data):
        return {
            "login": courier_data[0],
            "password": courier_data[1]
        }

    @allure.title("Логин курьера")
    @allure.description("Проверяет, что созданный курьер может авторизоваться.")
    def test_login_courier_success(self, courier_data):
        login_payload = self._get_login_payload(courier_data)

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин курьера без логина")
    @allure.description("Проверяет, что запрос логина без поля login возвращает ошибку.")
    def test_login_courier_without_login_returns_error(self, courier_data):
        login_payload = self._get_login_payload(courier_data)
        login_payload.pop("login")

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа"
        }

    @allure.title("Логин курьера без пароля")
    @allure.description("Проверяет, что запрос логина без поля password возвращает ошибку.")
    def test_login_courier_without_password_returns_error(self, courier_data):
        login_payload = self._get_login_payload(courier_data)
        login_payload.pop("password")

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 504
        assert response.text == "Service unavailable"

    @allure.title("Логин несуществующего курьера")
    @allure.description("Проверяет, что нельзя авторизоваться под несуществующим пользователем.")
    def test_login_non_existent_courier_returns_error(self):
        response = self.courier_api.login_courier(CourierData.NON_EXISTENT_COURIER)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    @allure.title("Логин курьера с неверным логином")
    @allure.description("Проверяет, что нельзя авторизоваться с неправильным логином.")
    def test_login_courier_with_wrong_login_returns_error(self, courier_data):
        login_payload = self._get_login_payload(courier_data)
        login_payload["login"] = "wrong" + login_payload["login"]

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    @allure.title("Логин курьера с неверным паролем")
    @allure.description("Проверяет, что нельзя авторизоваться с неправильным паролем.")
    def test_login_courier_with_wrong_password_returns_error(self, courier_data):
        login_payload = self._get_login_payload(courier_data)
        login_payload["password"] = "wrong" + login_payload["password"]

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }
