from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeUpdatedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
