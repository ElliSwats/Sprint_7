import allure

from utils.send_methods import Methods


class TestLoginCourier:
    @allure.title('Успешная авторизация зарегестрированного курьера и проверка ответа сервера. '
                  'Эндпойнт /api/v1/courier/login')
    def test_answers_and_login_created_courier_success(self, reg_and_auth):
        user_data = reg_and_auth
        with allure.step("Авторизация и получение courier id"):
            response, courier_id = Methods.login_courier(
                login=user_data[0],
                password=user_data[1])
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка, что courier id не пустой"):
            assert courier_id is not None and courier_id != ""

    @allure.title('Проверка ответа сервера при логине без пароля. Эндпойнт /api/v1/courier/login')
    def test_answers_without_password_success(self, reg_and_auth):
        user_data = reg_and_auth
        with allure.step("Попытка авторизации с пустым паролем"):
            response, _ = Methods.login_courier(login=user_data[0], password='')
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400
        with allure.step("Проверка ожидаемого текста сообщения об ошибке с фактическим"):
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка ответа сервера без логина c паролем. Эндпойнт /api/v1/courier/login')
    def test_answers_without_login_success(self, reg_and_auth):
        user_data = reg_and_auth
        with allure.step("Попытка авторизации с пустым login"):
            response, _ = Methods.login_courier(
                login='',
                password=user_data[1])
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 400
        with allure.step("Проверка ожидаемого текста сообщения об ошибке с фактическим"):
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка сообщения об ошибке при неверных логине и пароле. Эндпойнт /api/v1/courier/login')
    def test_check_message_error_mistake_login_and_password(self, reg_and_auth):
        user_data = reg_and_auth
        with allure.step("Попытка авторизации с неверными логином и паролем"):
            response, _ = Methods.login_courier(login=user_data[0]+'334', password=user_data[0]+'567f')
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 404
        with allure.step("Проверка ожидаемого текста сообщения об ошибке с фактическим"):
            assert response.json()["message"] == "Учетная запись не найдена"
