import logging

from abc import ABC, abstractmethod
import requests
from subhub.cfg import CFG
from subhub.secrets import get_secret

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class AbstractStripeWebhookProcessor(ABC):

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload


    def get_salesforce_uri(self):
        if CFG("AWS_EXECUTION_ENV", None) is None:
            secret_values = CFG.SALESFORCE_URI
        else:  # pragma: no cover
            subhub_values = get_secret("dev/SUBHUB")
            secret_values = subhub_values["salesforce_uri"]
        return secret_values

    def send_to_salesforce(self, payload):
        logger.info("\n sending to salesforce : \n" + str(payload))
        uri = self.get_salesforce_uri()
        requests.post(uri, json=payload)
        print("\n sending to salesforce : \n" + str(payload))

    def unhandled_event(self, payload):
       logging.info(f"Event not handled: {payload}")

    @abstractmethod
    def run(self):
        pass



