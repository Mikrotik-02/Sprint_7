import pytest

from api.courier_api import CourierAPI
from helpers.generators import register_new_courier_and_return_login_password


@pytest.fixture
def courier_data():
    courier = register_new_courier_and_return_login_password()
    yield courier

    if courier:
        login_payload = {
            "login": courier[0],
            "password": courier[1]
        }
        try:
            login_response = CourierAPI().login_courier(login_payload)
            if login_response.status_code == 200:
                courier_id = login_response.json().get("id")
                if courier_id:
                    CourierAPI().delete_courier(courier_id)
        except Exception:
            pass
