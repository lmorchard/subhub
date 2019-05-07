from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeExpiredProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
