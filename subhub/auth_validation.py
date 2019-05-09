import logging

from subhub.cfg import CFG
from subhub.secrets import get_secret

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def payment_auth(api_token, required_scopes=None):
    secrets = get_secret_values()
    if api_token in secrets:
        return {"value": True}
    return None


def get_secret_values():
    if CFG("AWS_EXECUTION_ENV", None) is None:
        secret_values = CFG.PAYMENT_API_KEY
    else:  # pragma: no cover
        subhub_values = get_secret("dev/SUBHUB")
        secret_values = subhub_values["payment_api_key"]
    return secret_values


def support_auth(api_token, required_scopes=None):
    secrets = get_support_values()
    if api_token in secrets:
        return {"value": True}
    return None


def get_support_values():
    if CFG("AWS_EXECUTION_ENV", None) is None:
        secret_values = CFG.SUPPORT_API_KEY
    else:  # pragma: no cover
        subhub_values = get_secret("dev/SUBHUB")
        secret_values = subhub_values["support_api_key"]
    return secret_values


def webhook_auth(api_token, required_scopes=None):
    logger.info(f"api token {api_token}")
    secrets = get_webhook_values()
    if api_token in secrets:
        return {"value": True}
    return None


def get_webhook_values():
    if CFG('AWS_EXECUTION_ENV', None) is None:
        secret_values = CFG.WEBHOOK_API_KEY
    else:  # pragma: no cover
        subhub_values = get_secret('dev/SUBHUB')
        secret_values = subhub_values['webhook_api_key']
    return secret_values
