BASE_URL = 'https://qa-scooter.praktikum-services.ru'
ENDPOINT_COURIER = '/api/v1/courier/'
ENDPOINT_LOGIN = '/api/v1/courier/login/'
ENDPOINT_ORDER = '/api/v1/orders/'

test_user_data = {
    "login": "simple_Antoshka",
    "password": "34563eee",
    "firstName": "Antoshka"
}

list_param_reg = [
    (None, 'some99password56', 'some465first55Name89'),
    ('some1login367', None, 'some465first55Name89')]

list_param_color = [("BLACK"), ("GREY"), ("BLACK", "GREY"), ("")]
