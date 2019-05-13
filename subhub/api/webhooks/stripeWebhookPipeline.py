from subhub.api.webhooks.stripe_customer_created import StripeCustomerCreated
from subhub.api.webhooks.stripeChargeSucceededProcessor import StripeChargeSucceededProcessor
from subhub.api.webhooks.stripe_unhandled_event import StripeUnhandledEvent


class StripeWebhookPipeline :

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    def run(self):
        event_type = self.payload["type"]
        if event_type == "customer.created":
            StripeCustomerCreated(self.payload).run()
        elif event_type == "charge.succeeded":
            StripeChargeSucceededProcessor(self.payload).run()
        else:
            StripeUnhandledEvent(self.payload).run()
