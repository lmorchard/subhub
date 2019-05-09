import logging
import requests
from subhub.api.webhooks.routes.abstractRoute import AbstractRoute
from subhub.cfg import CFG
from subhub.secrets import get_secret
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class SalesforceRoute(AbstractRoute):

    def route(self):
        logger.info("\n sending to salesforce : \n" + str(self.payload))
        uri = self.get_salesforce_uri()
        requests.post(uri, json=self.payload)
        self.report_route(self.payload)
        print("\n sending to salesforce : \n" + str(self.payload))


    def get_salesforce_uri(self):
        if CFG("AWS_EXECUTION_ENV", None) is None:
            secret_values = CFG.SALESFORCE_URI
        else:  # pragma: no cover
            subhub_values = get_secret("dev/SUBHUB")
            secret_values = subhub_values["salesforce_uri"]
        return secret_values