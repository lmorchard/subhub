import os

os.environ["PAYMENT_API_KEY"] = "sh_payment_api_key"
os.environ["SUPPORT_API_KEY"] = "sh_support_api_key"

from subhub import auth_validation
from subhub.cfg import CFG


def test_payment_auth():
    api_token = "sh_payment_api_key"
    payments_auth = auth_validation.payment_auth(api_token, required_scopes=None)
    assert payments_auth["value"] is True


def test_payment_auth_bad_token():
    api_token = "sh_payment_api_key_bad"
    payments_auth = auth_validation.payment_auth(api_token, required_scopes=None)
    assert payments_auth is None


def test_support_auth():
    api_token = "sh_support_api_key"
    support_auth = auth_validation.support_auth(api_token, None)
    assert support_auth["value"] is True


def test_support_auth_bad_token():
    api_token = "sh_support_api_key_bad"
    support_auth = auth_validation.support_auth(api_token, None)
    assert support_auth is None
