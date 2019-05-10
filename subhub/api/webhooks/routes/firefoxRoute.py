import logging
from subhub.cfg import CFG
from subhub.secrets import get_secret
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import boto3
from botocore.exceptions import ClientError

from subhub.api.webhooks.routes.abstractRoute import AbstractRoute

class FirefoxRoute(AbstractRoute):

    def route(self):
        sqs_client = boto3.client("sqs", region_name=self.__get_aws_region())
        try:
            msg = sqs_client.send_message(QueueUrl=self.__get_awssql_uri(), MessageBody=self.payload)
        except ClientError as e:
            logging.error(e)
            self.report_route_error(self.payload)

        if msg == "200":
            self.report_route(self.payload);
        else:
            self.report_route_error(self.payload)

    def __get_awssql_uri(self):
        if CFG("AWS_EXECUTION_ENV", None) is None:
            secret_values = CFG.AWSSQS_URI
        else:  # pragma: no cover
            subhub_values = get_secret("dev/SUBHUB")
            secret_values = subhub_values["awssqs_uri"]
        return secret_values

    def __get_aws_region(self):
        if CFG("AWS_EXECUTION_ENV", None) is None:
            secret_values = CFG.AWS_REGION
        else:  # pragma: no cover
            subhub_values = get_secret("dev/SUBHUB")
            secret_values = subhub_values["aws_region"]
        return secret_values
