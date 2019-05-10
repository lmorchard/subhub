from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor

import json
import requests

from subhub.api.webhooks.routes.staticRoutes import StaticRoutes


class StripeChargeSucceededProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        d = self.payload

        sfd = {}

        sfd["charge.amount"] = str(d["data"]["object"]["amount"])
        sfd["charge.created"] = str(d["created"])
        sfd["charge.currency"] = str(d["data"]["object"]["currency"])
        sfd["invoice.charge.id"] = str(d["id"])
        #sfd["invoice.subscription.id"] = str(d["data"])
        sfd["charge.customer"] = str(d["data"]["object"]["customer"])
        sfd["charge.card.last4"] = str(d["data"]["object"]["payment_method_details"]["card"]["last4"])
        sfd["charge.card.brand"] = str(d["data"]["object"]["payment_method_details"]["card"]["brand"])
        sfd["charge.card.exp_month"] = str(d["data"]["object"]["payment_method_details"]["card"]["exp_month"])
        sfd["charge.card.exp_year"] = str(d["data"]["object"]["payment_method_details"]["card"]["exp_year"])
        sfd["invoice.id"] = str(d["data"]["object"]["invoice"])
        order_id = d["data"]["object"]["metadata"].get("order_id")
        sfd["charge.order.order_id"] = order_id
        #sfd["invoice.period_start"] = str(d["data"])
        #sfd["invoice.period_end"] = str(d["data"])
        sfd["charge.balance_transaction.application_fee"] = str(d["data"]["object"]["application_fee"])
        #sfd["charge.balance_transaction.net"] = str(d["data"])
        #sfd["charge.balance_transaction.exchange_rate"] = str(d["data"])

        routes = [StaticRoutes.FIREFOX_ROUTE, StaticRoutes.SALESFORCE_ROUTE]
        self.send_to_routes(routes, json.dumps(sfd))
