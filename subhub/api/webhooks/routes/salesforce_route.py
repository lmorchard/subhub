import logging
import json
import requests
from subhub.api.webhooks.routes.abstract_route import AbstractRoute
from subhub.cfg import CFG
from subhub.secrets import get_secret


logger = logging.getLogger('salesforce_route')
log_handle = logging.StreamHandler()
log_handle.setLevel(logging.INFO)
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handle.setFormatter(logformat)
logger.addHandler(log_handle)


class SalesforceRoute(AbstractRoute):

    def route(self):
        route_payload = json.loads(self.payload) 
        logger.info(f"salesforce route: {type(route_payload)}")
        uri = self.get_salesforce_uri()
        requests.post(uri, json=route_payload)
        logger.info('start report')
        self.report_route(route_payload, "salesforce")
        logger.info(f"sending to salesforce : {self.payload}")


    def get_salesforce_uri(self):
        if CFG("AWS_EXECUTION_ENV", None) is None:
            secret_values = CFG.BASKET_URI
        else:  # pragma: no cover
            subhub_values = get_secret("dev/SUBHUB")
            secret_values = subhub_values["basket_uri"]
        return secret_values