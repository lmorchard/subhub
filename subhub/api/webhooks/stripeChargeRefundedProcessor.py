from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeRefundedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
