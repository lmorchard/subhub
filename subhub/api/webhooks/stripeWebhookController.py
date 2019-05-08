import json
from flask import request, Response
import sys
import logging

from subhub.api.webhooks.stripeWebhookPipeline import StripeWebhookPipeline

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def webhook_view() -> tuple:
    try:
        event_json = json.loads(request.data)
        p = StripeWebhookPipeline(event_json)
        p.run()
    except:
        error = sys.exc_info()[0]
        logger.error("Oops!", error, "occured.")
        return Response(error, status=500)

    return Response("Success", status=200)
