from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeSucceededProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        salesforce_payload = self.payload
        self.send_to_salesforce(salesforce_payload)