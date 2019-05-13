import logging
import json
import requests

from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor
from subhub.api.webhooks.routes.staticRoutes import StaticRoutes

logger = logging.getLogger('charge_succeeded')
log_handle = logging.StreamHandler()
log_handle.setLevel(logging.INFO)
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handle.setFormatter(logformat)
logger.addHandler(log_handle)

class StripeChargeSucceeded(AbstractStripeWebhookProcessor):

    def run(self):
        d = self.payload

        sfd = {}
        sfd["event_id"] = d["id"]
        sfd["event_type"] = "charge_succeeded"
        sfd["transaction_amount"] = str(d["data"]["object"]["amount"])
        sfd["created_date"] = d["created"]
        sfd["transaction_currency"] = str(d["data"]["object"]["currency"])
        sfd["charge_id"] = str(d["id"])
        sfd["customer_id"] = str(d["data"]["object"]["customer"])
        sfd["card_last4"] = str(d["data"]["object"]["payment_method_details"]["card"]["last4"])
        sfd["card_brand"] = str(d["data"]["object"]["payment_method_details"]["card"]["brand"])
        sfd["card_exp_month"] = str(d["data"]["object"]["payment_method_details"]["card"]["exp_month"])
        sfd["card_exp_year"] = str(d["data"]["object"]["payment_method_details"]["card"]["exp_year"])
        sfd["invoice_id"] = str(d["data"]["object"]["invoice"])
        order_id = d["data"]["object"]["metadata"].get("order_id")
        sfd["order_id"] = order_id
        sfd["application_fee"] = str(d["data"]["object"]["application_fee"])

        routes = [StaticRoutes.SALESFORCE_ROUTE]  #setup not complete StaticRoutes.FIREFOX_ROUTE, 
        self.send_to_routes(routes, json.dumps(sfd))
