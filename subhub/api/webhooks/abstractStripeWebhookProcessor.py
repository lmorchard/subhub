from abc import ABC, abstractmethod
import requests


class AbstractStripeWebhookProcessor(ABC):

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    def send_to_salesforce(self, payload):
        requests.post("", json=payload)
        print("\n sending to salesforce : \n" + str(payload))

    def unhandled_event(self, payload):
       print(f"Event not handled: {payload}")

    @abstractmethod
    def run(self):
        pass
