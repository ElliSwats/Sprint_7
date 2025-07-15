import pytest

from utils.generate_courier import register_new_courier_and_return_login_password as reg
from utils.send_methods import Methods
from utils.data import test_user_data


@pytest.fixture(scope='function')
def reg_and_auth():
    user_data = reg()

    yield user_data

    _, courier_id = Methods.login_courier(login=user_data[0], password=user_data[1])
    Methods.delete_courier(courier_id=courier_id)


@pytest.fixture(scope='function')
def delete_courier():
    test_data = test_user_data

    yield test_data

    _, courier_id = Methods.login_courier(
        login=test_data["login"],
        password=test_data["password"])
    Methods.delete_courier(courier_id=courier_id)
