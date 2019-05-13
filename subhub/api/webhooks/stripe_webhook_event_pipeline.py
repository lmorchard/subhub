from subhub.api.webhooks.customer.stripe_customer_created_event import StripeCustomerCreated
from subhub.api.webhooks.charge.stripe_charge_succeeded_event import StripeChargeSucceededEvent
from subhub.api.webhooks.customer.stripe_customer_deleted_event import StripeCustomerDeleted
from subhub.api.webhooks.customer.stripe_customer_updated_event import StripeCustomerUpdated
from subhub.api.webhooks.stripe_unhandled_event import StripeUnhandledEvent


class StripeWebhookEventPipeline :

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    def run(self):
        event_type = self.payload["type"]
        if event_type == "customer.created":
            StripeCustomerCreated(self.payload).run()
        elif event_type == "customer.updated":
            StripeCustomerUpdated(self.payload).run()
        elif event_type == "customer.deleted":
            StripeCustomerDeleted(self.payload).run()
        elif event_type == "charge.succeeded":
            StripeChargeSucceededEvent(self.payload).run()
        else:
            StripeUnhandledEvent(self.payload).run()
