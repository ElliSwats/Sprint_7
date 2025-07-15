import allure
import requests
from faker import Faker

from utils.data import (
    BASE_URL,
    ENDPOINT_COURIER,
    ENDPOINT_LOGIN,
    ENDPOINT_ORDER)


fake = Faker(locale="ru_RU")


class Methods:
    @staticmethod
    @allure.step("Отправляем post запрос на эндпойнт /api/v1/courier")
    def create_courier(login=None, password=None, first_name=None):
        body = {}
        if login is not None:
            body['login'] = login
        if password is not None:
            body['password'] = password
        if first_name is not None:
            body['first_name'] = first_name
        response = requests.post(url=BASE_URL + ENDPOINT_COURIER, data=body)

        return response

    @staticmethod
    @allure.step("Отправляем post запрос на эндпойнт /api/v1/courier/login")
    def login_courier(login, password):
        body = {"login": login, "password": password}
        response = requests.post(url=BASE_URL + ENDPOINT_LOGIN, data=body)

        try:
            courier_id = response.json()['id']
        except KeyError:
            courier_id = None

        return response, courier_id

    @staticmethod
    @allure.step("Отправляем post запрос на эндпойнт /api/v1/orders")
    def create_orders(list_colors):
        body = {"firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "address": fake.address(),
                "metroStation": str(fake.random_int(min=1, max=110)),
                "phone": fake.phone_number(),
                "rentTime": str(fake.random_int(min=1, max=7)),
                "deliveryDate": fake.date_between(start_date='today', end_date='+10d').isoformat(),
                "comment": fake.words(nb=1, unique=True),
                "color": list_colors}
        response = requests.post(url=BASE_URL + ENDPOINT_ORDER, data=body)

        try:
            track_id = response.json()['track']
        except KeyError:
            track_id = None

        return response, track_id

    @staticmethod
    @allure.step("Отправляем get запрос на эндпойнт /api/v1/orders")
    def get_orders():
        response = requests.get(url=BASE_URL + ENDPOINT_ORDER)

        return response

    @staticmethod
    @allure.step("Отправляем delete запрос на эндпойнт /api/v1/courier/")
    def delete_courier(courier_id):
        body = {"id": courier_id}
        response = requests.delete(url=BASE_URL + ENDPOINT_COURIER + str(courier_id), data=body)

        return response
