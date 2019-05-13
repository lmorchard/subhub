import mockito
import requests
import boto3
import flask

from subhub.featuretests.stripe_webhooks.utils import get_salesforce_uri, get_aws_region, runTest, MockSqsClient


def test_stripe_webhook_succeeded(mocker):
    response = mockito.mock({
        'status_code': 200,
        'text': 'Ok'
    }, spec=requests.Response)
    data = {'event_id': 'evt_00000000000000', 'event_type': 'charge.succeeded', 'transaction_amount': 2000, 'created_date': 1326853478,
            'transaction_currency': 'usd', 'charge_id': 'evt_00000000000000', 'customer_id': None, 'card_last4': '4444', 'card_brand': 'mastercard',
            'card_exp_month': 8, 'card_exp_year': 2019, 'invoice_id': None, 'order_id': '6735', 'application_fee': None}

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
