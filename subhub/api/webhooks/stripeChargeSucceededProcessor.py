from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeSucceededProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
