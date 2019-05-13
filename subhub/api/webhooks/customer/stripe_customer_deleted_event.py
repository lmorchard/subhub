import logging
import json

from subhub.api.webhooks.abstract_stripe_webhook_event import AbstractStripeWebhookEvent
from subhub.api.webhooks.routes.static_routes import StaticRoutes

logger = logging.getLogger('customer.created')
log_handle = logging.StreamHandler()
log_handle.setLevel(logging.INFO)
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handle.setFormatter(logformat)
logger.addHandler(log_handle)

class StripeCustomerDeleted(AbstractStripeWebhookEvent):

    def run(self):
        d = self.payload
        sfd = {}

        sfd["event_id"] = d["id"]
        sfd["event_type"] = d["type"]
        sfd["email"] = d["data"]["object"]["email"]
        sfd["stripe_id"] = d["data"]["object"]["id"]
        sfd["name"] = d["data"]["object"]["name"]
        user_id = d["data"]["object"]["metadata"].get("userid")
        sfd["user_id"] = user_id

        routes = [StaticRoutes.SALESFORCE_ROUTE]  #setup not complete StaticRoutes.FIREFOX_ROUTE, 
        self.send_to_routes(routes, json.dumps(sfd))