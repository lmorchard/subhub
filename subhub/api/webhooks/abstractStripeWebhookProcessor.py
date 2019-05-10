import logging
from abc import ABC, abstractmethod

import requests
from subhub.api.webhooks.routes.routesPipeline import RoutesPipeline
from subhub.cfg import CFG
from subhub.secrets import get_secret

logger = logging.getLogger('webhook_abstract')
log_handle = logging.StreamHandler()
log_handle.setLevel(logging.INFO)
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handle.setFormatter(logformat)
logger.addHandler(log_handle)


class AbstractStripeWebhookProcessor(ABC):

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload


    @staticmethod
    def send_to_routes(report_routes, messageToRoute):
        logger.info(f"report routes {report_routes} message {messageToRoute}")
        RoutesPipeline(report_routes, messageToRoute).run()


    def get_salesforce_uri(self):
        if CFG("AWS_EXECUTION_ENV", None) is None:
            secret_values = CFG.BASKET_URI
        else:  # pragma: no cover
            subhub_values = get_secret("dev/SUBHUB")
            secret_values = subhub_values["basket_uri"]
        return secret_values


    def send_to_salesforce(self, payload):
        logger.info(f"sending to salesforce : {payload}")
        uri = self.get_salesforce_uri()
        requests.post(uri, json=payload)
        # print("\n sending to salesforce : \n" + str(payload))


    @staticmethod
    def unhandled_event(payload):
        logger.info(f"Event not handled: {payload}")


    @abstractmethod
    def run(self):
        pass
