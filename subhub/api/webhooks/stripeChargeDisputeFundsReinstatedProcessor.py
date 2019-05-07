from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeDisputeFundsReinstatedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
