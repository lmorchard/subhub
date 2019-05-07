from abc import ABC, abstractmethod


class AbstractStripeWebhookProcessor(ABC):

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    @abstractmethod
    def run(self):
        pass