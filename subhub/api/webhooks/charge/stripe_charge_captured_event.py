from subhub.api.webhooks.abstract_stripe_webhook_event import AbstractStripeWebhookEvent


class StripeChargeCapturedEvent(AbstractStripeWebhookEvent):

    def run(self):
        print(self.payload)

