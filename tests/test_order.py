import allure
import pytest

from utils.send_methods import Methods
from utils.data import list_param_color


class TestOrder:
    @allure.title('Успешное получение списка заказов. Эндпойнт /api/v1/orders')
    def test_get_list_orders_success(self):
        with allure.step("Получение информации о заказах"):
            response = Methods.get_orders()
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка, что список заказов не пустой"):
            assert response.json()["orders"] is not None

    @allure.title('Успешное создание списка заказов. Эндпойнт /api/v1/orders')
    @pytest.mark.parametrize('color', list_param_color)
    def test_create_orders_success(self, color):
        with allure.step("Создания заказа и получение track id"):
            response, track_id = Methods.create_orders(list_param_color)
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 201
        with allure.step("Проверка, что track_id не пустой"):
            assert track_id is not None
