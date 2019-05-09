import logging
from abc import ABC, abstractmethod

from subhub.api.webhooks.routes.routesPipeline import RoutesPipeline

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class AbstractStripeWebhookProcessor(ABC):

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    @staticmethod
    def send_to_routes(report_routes, messageToRoute):
        RoutesPipeline(report_routes, messageToRoute).run()

    @staticmethod
    def unhandled_event(payload):
        logger.info(f"Event not handled: {payload}")

    @abstractmethod
    def run(self):
        pass
