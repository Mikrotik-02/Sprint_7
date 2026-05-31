import pytest

from api.courier_api import CourierAPI
from data.courier_data import CourierData


class TestLoginCourier:
    def setup_method(self):
        self.courier_api = CourierAPI()

    def _get_login_payload(self, courier_data):
        return {
            "login": courier_data[0],
            "password": courier_data[1]
        }

    def test_login_courier_success(self, courier_data):
        login_payload = self._get_login_payload(courier_data)

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize(
        "required_field, expected_status_code, expected_body",
        [
            (
                "login",
                400,
                {
                    "code": 400,
                    "message": "Недостаточно данных для входа"
                }
            ),
            (
                "password",
                504,
                "Service unavailable"
            )
        ]
    )
    def test_login_courier_without_required_field_returns_error(
        self,
        courier_data,
        required_field,
        expected_status_code,
        expected_body
    ):
        login_payload = self._get_login_payload(courier_data)
        login_payload.pop(required_field)

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == expected_status_code
        if isinstance(expected_body, dict):
            assert response.json() == expected_body
        else:
            assert response.text == expected_body

    def test_login_non_existent_courier_returns_error(self):
        response = self.courier_api.login_courier(CourierData.NON_EXISTENT_COURIER)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    def test_login_courier_with_wrong_login_returns_error(self, courier_data):
        login_payload = self._get_login_payload(courier_data)
        login_payload["login"] = "wrong" + login_payload["login"]

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    def test_login_courier_with_wrong_password_returns_error(self, courier_data):
        login_payload = self._get_login_payload(courier_data)
        login_payload["password"] = "wrong" + login_payload["password"]

        response = self.courier_api.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }
