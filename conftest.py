import pytest

from utils.generate_courier import register_new_courier_and_return_login_password as reg
from utils.send_methods import Methods


@pytest.fixture(scope='function')
def reg_and_auth():
    user_data = reg()

    yield user_data

    _, courier_id = Methods.login_courier(login=user_data[0], password=user_data[1])
    Methods.delete_courier(courier_id=courier_id)
