from subhub.api.webhooks import stripe_webhook_event_pipeline
import json
import os
from subhub.cfg import CFG
from subhub.secrets import get_secret

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

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
    pipeline = stripe_webhook_event_pipeline.StripeWebhookEventPipeline(read_json(file_name))
    pipeline.run()


def read_json(file_name):
    f = open(os.path.join(__location__, file_name))

    with f:
        return json.load(f)


class MockSqsClient:
    def send_message(self, QueueUrl={},  MessageBody={}):
        return "200"