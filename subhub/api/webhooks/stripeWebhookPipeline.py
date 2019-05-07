from subhub.api.webhooks.stripeChargeCapturedProcessor import StripeChargeCapturedProcessor
from subhub.api.webhooks.stripeChargeDisputeClosedProcessor import StripeChargeDisputeClosedProcessor
from subhub.api.webhooks.stripeChargeDisputeCreatedProcessor import StripeChargeDisputeCreatedProcessor
from subhub.api.webhooks.stripeChargeDisputeFundsReinstatedProcessor import StripeChargeDisputeFundsReinstatedProcessor
from subhub.api.webhooks.stripeChargeDisputeFundsWithdrawnProcessor import StripeChargeDisputeFundsWithdrawnProcessor
from subhub.api.webhooks.stripeChargeDisputeUpdatedProcessor import StripeChargeDisputeUpdatedProcessor
from subhub.api.webhooks.stripeChargeExpiredProcessor import StripeChargeExpiredProcessor
from subhub.api.webhooks.stripeChargeFailedProcessor import StripeChargeFailedProcessor
from subhub.api.webhooks.stripeChargePendingProcessor import StripeChargePendingProcessor
from subhub.api.webhooks.stripeChargeRefundUpdatedProcessor import StripeChargeRefundUpdatedProcessor
from subhub.api.webhooks.stripeChargeRefundedProcessor import StripeChargeRefundedProcessor
from subhub.api.webhooks.stripeChargeSucceededProcessor import StripeChargeSucceededProcessor
from subhub.api.webhooks.stripeChargeUpdatedProcessor import StripeChargeUpdatedProcessor


class StripeWebhookPipeline :

    def __init__(self, payload):
        assert isinstance(payload, object)
        self.payload = payload

    def run(self):
        type = self.payload["type"]
        if type == "charge.captured":
            StripeChargeCapturedProcessor(self.payload).run()
        elif type == "charge.updated":
            StripeChargeUpdatedProcessor(self.payload).run()
        elif type == "charge.succeeded":
            StripeChargeSucceededProcessor(self.payload).run()
        elif type == "charge.refunded":
            StripeChargeRefundedProcessor(self.payload).run()
        elif type == "charge.refund.updated":
            StripeChargeRefundUpdatedProcessor(self.payload).run()
        elif type == "charge.pending":
            StripeChargePendingProcessor(self.payload).run()
        elif type == "charge.failed":
            StripeChargeFailedProcessor(self.payload).run()
        elif type == "charge.dispute.updated":
            StripeChargeDisputeUpdatedProcessor(self.payload).run()
        elif type == "charge.dispute.funds_withdrawn":
            StripeChargeDisputeFundsWithdrawnProcessor(self.payload).run()
        elif type == "charge.dispute.funds_reinstated":
            StripeChargeDisputeFundsReinstatedProcessor(self.payload).run()
        elif type == "charge.dispute.created":
            StripeChargeDisputeCreatedProcessor(self.payload).run()
        elif type == "charge.dispute.closed":
            StripeChargeDisputeClosedProcessor(self.payload).run()
        elif type == "charge.expired":
            StripeChargeExpiredProcessor(self.payload).run()
        else:
            raise ValueError(str(type) + " is not yet supported.")

