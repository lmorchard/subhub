from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeFailedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
