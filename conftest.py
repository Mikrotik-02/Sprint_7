import pytest

from api.courier_api import CourierAPI
from helpers.generators import generate_courier_payload
from helpers.generators import register_new_courier_and_return_login_password


def delete_courier_by_payload(payload):
    login_payload = {
        "login": payload["login"],
        "password": payload["password"]
    }
    try:
        login_response = CourierAPI().login_courier(login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                CourierAPI().delete_courier(courier_id)
    except Exception:
        pass


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


@pytest.fixture
def courier_payload():
    payload = generate_courier_payload()
    yield payload
    delete_courier_by_payload(payload)
