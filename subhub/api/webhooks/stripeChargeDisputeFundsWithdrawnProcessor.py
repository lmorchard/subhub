from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeDisputeFundsWithdrawnProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
