import allure
import pytest

from api.order_api import OrderAPI
from data.order_data import OrderData


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание заказа")
class TestCreateOrder:
    def setup_method(self):
        self.order_api = OrderAPI()

    @pytest.mark.parametrize("color", OrderData.ORDER_COLORS)
    @allure.title("Создание заказа с разными цветами")
    @allure.description("Проверяет, что заказ можно создать с разными вариантами цвета и получить track.")
    def test_create_order_with_different_colors_returns_track(self, color):
        payload = OrderData.get_order_payload_with_color(color)

        response = self.order_api.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert response.json()["track"]
