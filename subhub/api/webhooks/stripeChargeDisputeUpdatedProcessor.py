from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeDisputeUpdatedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
