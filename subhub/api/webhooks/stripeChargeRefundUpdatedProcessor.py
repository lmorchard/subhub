from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeRefundUpdatedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
