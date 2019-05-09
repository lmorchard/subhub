from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeUnhandledEvent(AbstractStripeWebhookProcessor):

    def run(self):
        salesforce_payload = self.payload
        self.unhandled_event(salesforce_payload)
