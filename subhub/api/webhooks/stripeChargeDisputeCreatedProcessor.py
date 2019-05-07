from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeDisputeCreatedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
