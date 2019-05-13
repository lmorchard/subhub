from subhub.api.webhooks.abstract_stripe_webhook_event import AbstractStripeWebhookEvent


class StripeUnhandledEvent(AbstractStripeWebhookEvent):

    def run(self):
        salesforce_payload = self.payload
        self.unhandled_event(salesforce_payload)
