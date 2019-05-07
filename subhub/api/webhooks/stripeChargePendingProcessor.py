from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargePendingProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
