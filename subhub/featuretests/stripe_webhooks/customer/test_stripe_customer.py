import mockito
import requests
import boto3
import flask

from subhub.featuretests.stripe_webhooks.utils import get_salesforce_uri, get_aws_region, runTest, MockSqsClient


def run_cutomer(mocker, data, file_name):
    response = mockito.mock({
        'status_code': 200,
        'text': 'Ok'
    }, spec=requests.Response)

    #using mockito
    mockito.when(requests).post(get_salesforce_uri(), json=data).thenReturn(response)
    mockito.when(boto3).client('sqs', region_name=get_aws_region()).thenReturn(MockSqsClient)

    #using pytest mock
    mocker.patch.object(flask, "g")
    flask.g.return_value = ""

    runTest(file_name)

def test_stripe_webhook_customer_updated(mocker):
    data = {'event_id': 'evt_00000000000000', 'event_type': 'customer.updated', 'email': 'jon@tester.com', 'stripe_id': 'cus_00000000000000', 'name': 'Jon Tester', 'user_id': None}
    file_name = "customer/customer.updated.json"
    run_cutomer(mocker, data, file_name)

def test_stripe_webhook_customer_deleted(mocker):
    data = {'event_id': 'evt_00000000000000', 'event_type': 'customer.deleted', 'email': 'jon@tester.com', 'stripe_id': 'cus_00000000000000', 'name': 'Jon Tester', 'user_id': None}
    file_name = "customer/customer.deleted.json"
    run_cutomer(mocker, data, file_name)


def test_stripe_webhook_customer_subscription_created(mocker):
    data = {'event_id': 'evt_00000000000000', 'event_type': 'customer.subscription.created', 'stripe_id': 'sub_00000000000000', 'customer_id': 'cus_00000000000000',
            'current_period_start': 1519435009, 'current_period_end': 1521854209, 'canceled_at': 1519680008, 'days_until_due': None, 'default_payment_method': None,
            'plan_id': 'subhub-plan-api_00000000000000', 'plan_amount': 500, 'plan_currency': 'usd', 'plan_interval': 'month', 'status': 'canceled', 'trial_start': None,
            'trial_end': None, 'tax_percent': None, 'application_fee_percent': None, 'user_id': None}
    file_name = "customer/customer.subscription.created.json"
    run_cutomer(mocker, data, file_name)
