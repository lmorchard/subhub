import mockito
import requests
import boto3
import flask

from subhub.featuretests.stripe_webhooks.utils import get_salesforce_uri, get_aws_region, runTest, MockSqsClient


def test_stripe_webhook_customer_updated(mocker):
    response = mockito.mock({
        'status_code': 200,
        'text': 'Ok'
    }, spec=requests.Response)
    data = {'event_id': 'evt_00000000000000', 'event_type': 'customer.updated', 'email': 'jon@tester.com', 'stripe_id': 'cus_00000000000000', 'name': 'Jon Tester', 'user_id': None}

    #using mockito
    mockito.when(requests).post(get_salesforce_uri(), json=data).thenReturn(response)
    mockito.when(boto3).client('sqs', region_name=get_aws_region()).thenReturn(MockSqsClient)

    #using pytest mock
    mocker.patch.object(flask, "g")
    flask.g.return_value = ""

    runTest("customer/customer.updated.json")


def test_stripe_webhook_customer_deleted(mocker):
    response = mockito.mock({
        'status_code': 200,
        'text': 'Ok'
    }, spec=requests.Response)
    data = {'event_id': 'evt_00000000000000', 'event_type': 'customer.deleted', 'email': 'jon@tester.com', 'stripe_id': 'cus_00000000000000', 'name': 'Jon Tester', 'user_id': None}

    #using mockito
    mockito.when(requests).post(get_salesforce_uri(), json=data).thenReturn(response)
    mockito.when(boto3).client('sqs', region_name=get_aws_region()).thenReturn(MockSqsClient)

    #using pytest mock
    mocker.patch.object(flask, "g")
    flask.g.return_value = ""

    runTest("customer/customer.deleted.json")