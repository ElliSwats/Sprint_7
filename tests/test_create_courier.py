import pytest
import allure

from utils.send_methods import Methods
from utils.data import test_user_data, list_param_reg


class TestCreateCourier:
    test_data = test_user_data

    @allure.title('Регистрация курьера и полная проверка ответов. Эндпойнт /api/v1/courier')
    def test_create_new_courier_success(self):
        try:
            with allure.step("Создаем тестового курьера"):
                response = Methods.create_courier(
                    login=self.test_data['login'],
                    password=self.test_data['password'],
                    first_name=self.test_data['firstName'])
            with allure.step("Проверка статус-кода ответа"):
                assert response.status_code == 201
            with allure.step("Проверка, что успешный запрос возвращает 'ok':true"):
                assert response.json()["ok"] is True

        except AssertionError as error:
            pytest.fail(f'Ошибка при создании нового курьера: {str(error)}')

        finally:
            _, courier_id = Methods.login_courier(
                login=self.test_data['login'],
                password=self.test_data['password'])
            Methods.delete_courier(courier_id=courier_id)

    @allure.title('Невозможность создать двух одинаковых курьеров. Эндпойнт /api/v1/courier')
    def test_impossible_create_two_identical_couriers_success(self, reg_and_auth):
        with allure.step("Создаем тестового курьера"):
            user_data = reg_and_auth
            response = Methods.create_courier(
                login=user_data[0],
                password=user_data[1],
                first_name=user_data[2])
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 409

    @allure.title('Проверка сообщения об ошибке при повторной регистрации с существующим логином.'
                  'Эндпойнт /api/v1/courier')
    def test_check_message_error_repeated_registration_success(self, reg_and_auth):
        with allure.step("Создаем тестового курьера"):
            user_data = reg_and_auth
            expected_answer = "Этот логин уже используется"
            response = Methods.create_courier(
                login=user_data[0],
                password=user_data[1],
                first_name=user_data[2])
        with allure.step("Получаем сообщение об ошибке"):
            actual_answer = response.json()["message"]
        with allure.step("Проверка ожидаемого текста сообщения об ошибке с фактическим"):
            assert actual_answer == expected_answer, f'Ожидалось {expected_answer}, но получено {actual_answer}'

    @allure.title('Проверка ответа сервера при регистрации без обязательных полей login или password.'
                  'Эндпойнт /api/v1/courier')
    @pytest.mark.parametrize('login, password, first_name', list_param_reg)
    def test_without_required_fields_success(self, login, password, first_name):
        with allure.step("Через параметризацию передаем тестовые наборы: один без пароля, второй без логина"):
            response = Methods.create_courier(login, password, first_name)
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400

    @allure.title('Проверка сообщения об ошибке при регистрации без обязательных полей login или password. '
                  'Эндпойнт /api/v1/courier')
    @pytest.mark.parametrize('login, password, first_name', list_param_reg)
    def test_message_without_required_fields_success(self, login, password, first_name):
        with allure.step("Через параметризацию передаем тестовые наборы: один без пароля, второй без логина"):
            expected_answer = "Недостаточно данных для создания учетной записи"
            response = Methods.create_courier(login, password, first_name)
        with allure.step("Получаем сообщение об ошибке"):
            actual_answer = response.json()["message"]
        with allure.step("Проверка ожидаемого текста сообщения об ошибке с фактическим"):
            assert expected_answer == actual_answer
