from subhub.api.webhooks import stripeWebhookPipeline
import json
import os
from mockito import when, mock
import requests

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def test_stripe_webhook_charge_captured():
    runTest("charge.captured.json")


def test_stripe_webhook_charge_expired():
    runTest("charge.expired.json")


def test_stripe_webhook_disputeClosed():
    runTest("charge.dispute.closed.json")


def test_stripe_webhook_disputeCreated():
    runTest("charge.dispute.created.json")


def test_stripe_webhook_disputeFundsReinstated():
    runTest("charge.dispute.funds_reinstated.json")


def test_stripe_webhook_disputeFundsWithdrawn():
    runTest("charge.dispute.funds_withdrawn.json")


def test_stripe_webhook_disputeUpdated():
    runTest("charge.dispute.updated.json")


def test_stripe_webhook_failed():
    runTest("charge.failed.json")


def test_stripe_webhook_pending():
    runTest("charge.pending.json")


def test_stripe_webhook_refundUpdated():
    runTest("charge.refund.updated.json")


def test_stripe_webhook_refunded():
    runTest("charge.refunded.json")


def test_stripe_webhook_succeeded():
    response = mock({
        'status_code': 200,
        'text': 'Ok'
    }, spec=requests.Response)
    when(requests, strict=False).post("", json="sdfsdf").thenReturn(response)
    runTest("charge.succeeded.json")


def test_stripe_webhook_updated():
    runTest("charge.updated.json")


def test_stripe_webhook_badpayload():
    try:
        runTest("badpayload.json")
    except ValueError as e:
        assert "this.will.break is not supported" == str(e)


def runTest(fileName):
    f = open(os.path.join(__location__, fileName));

    with f:
        data = json.load(f)

    pipeline = stripeWebhookPipeline.StripeWebhookPipeline(data)
    pipeline.run()
