import mockito
import requests
import boto3
import flask

from subhub.featuretests.stripe_webhooks.utils import get_salesforce_uri, get_aws_region, runTest


def test_stripe_webhook_succeeded(mocker):
    response = mockito.mock({
        'status_code': 200,
        'text': 'Ok'
    }, spec=requests.Response)
    data = {'event_id': 'evt_00000000000000', 'event_type': 'charge_succeeded', 'charge.amount': '2000', 'charge.created': '1326853478',
            'charge.currency': 'usd', 'invoice.charge.id': 'evt_00000000000000', 'charge.customer': 'None', 'charge.card.last4': '4444',
            'charge.card.brand': 'mastercard', 'charge.card.exp_month': '8', 'charge.card.exp_year': '2019', 'invoice.id': 'None', 'charge.order.order_id':
                '6735', 'charge.balance_transaction.application_fee': 'None'}

    #using mockito
    mockito.when(requests).post(get_salesforce_uri(), json=data).thenReturn(response)
    mockito.when(boto3).client('sqs', region_name=get_aws_region()).thenReturn(MockSqsClient)

    #using pytest mock
    mocker.patch.object(flask, "g")
    flask.g.return_value = ""

    #run the test
    runTest("charge/charge.succeeded.json")


def test_stripe_webhook_badpayload():
    try:
        runTest("charge/badpayload.json")
    except ValueError as e:
        assert "this.will.break is not supported" == str(e)


class MockSqsClient:
    def send_message(self, QueueUrl={},  MessageBody={}):
        return "200"
