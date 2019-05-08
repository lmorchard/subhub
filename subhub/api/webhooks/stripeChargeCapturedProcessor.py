from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeCapturedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)

