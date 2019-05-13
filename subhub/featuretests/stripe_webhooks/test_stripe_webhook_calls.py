from subhub.api.webhooks import stripeWebhookPipeline
import json
import os
from mockito import when, mock
import requests
from subhub.cfg import CFG
from subhub.secrets import get_secret
import boto3

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
    data = '{"charge.amount": "2000", "charge.created": "1326853478", "charge.currency": "usd", ' \
           '"invoice.charge.id": "evt_00000000000000", "charge.customer": "None", "charge.card.last4": "4444", "charge.card.brand": ' \
           '"mastercard", "charge.card.exp_month": "8", "charge.card.exp_year": "2019", "invoice.id": "None", "charge.order.order_id": "6735", ' \
           '"charge.balance_transaction.application_fee": "None"}'
    when(requests).post(get_salesforce_uri(), json=data).thenReturn(response)
    when(boto3).client('sqs', region_name=get_aws_region()).thenReturn(MockSqsClient)
    runTest("charge.succeeded.json")

class MockSqsClient:
    def send_message(self, QueueUrl={},  MessageBody={}):
        return "200"

def test_stripe_webhook_updated():
    runTest("charge.updated.json")


def test_stripe_webhook_badpayload():
    try:
        runTest("badpayload.json")
    except ValueError as e:
        assert "this.will.break is not supported" == str(e)


def get_awssql_uri():
    if CFG("AWS_EXECUTION_ENV", None) is None:
        secret_values = CFG.AWSSQS_URI
    else:  # pragma: no cover
        subhub_values = get_secret("dev/SUBHUB")
        secret_values = subhub_values["awssqs_uri"]
    return secret_values


def get_aws_region():
    if CFG("AWS_EXECUTION_ENV", None) is None:
        secret_values = CFG.AWS_REGION
    else:  # pragma: no cover
        subhub_values = get_secret("dev/SUBHUB")
        secret_values = subhub_values["aws_region"]
    return secret_values


def get_salesforce_uri():
    if CFG("AWS_EXECUTION_ENV", None) is None:
        secret_values = CFG.SALESFORCE_URI
    else:  # pragma: no cover
        subhub_values = get_secret("dev/SUBHUB")
        secret_values = subhub_values["salesforce_uri"]
    return secret_values


def runTest(file_name):
    pipeline = stripeWebhookPipeline.StripeWebhookPipeline(read_json(file_name))
    pipeline.run()


def read_json(file_name):
    f = open(os.path.join(__location__, file_name))

    with f:
        return json.load(f)
