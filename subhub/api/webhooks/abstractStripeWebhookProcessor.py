from abc import ABC, abstractmethod
import requests


class AbstractStripeWebhookProcessor(ABC):

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    def send_to_salesforce(self, payload):
        requests.post("", json=payload)
        print("\n sending to salesforce : \n" + str(payload))

    @abstractmethod
    def run(self):
        pass
