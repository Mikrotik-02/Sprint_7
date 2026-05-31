class OrderData:
    BASE_ORDER_PAYLOAD = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "Moscow, Test street, 1",
        "metroStation": 4,
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2026-06-06",
        "comment": "Test order"
    }

    ORDER_COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

    @staticmethod
    def get_order_payload_with_color(color):
        payload = OrderData.BASE_ORDER_PAYLOAD.copy()
        payload["color"] = color
        return payload
