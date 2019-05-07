from subhub.api.webhooks.abstractStripeWebhookProcessor import AbstractStripeWebhookProcessor


class StripeChargeDisputeClosedProcessor(AbstractStripeWebhookProcessor):

    def run(self):
        print(self.payload)
