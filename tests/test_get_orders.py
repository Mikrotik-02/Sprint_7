import allure

from api.order_api import OrderAPI


@allure.epic("API Яндекс Самокат")
@allure.feature("Получение списка заказов")
class TestGetOrders:
    def setup_method(self):
        self.order_api = OrderAPI()

    @allure.title("Получение списка заказов")
    @allure.description("Проверяет, что ручка возвращает список заказов.")
    def test_get_orders_returns_orders_list(self):
        response = self.order_api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
