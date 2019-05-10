import json
from flask import request, Response
import sys
import logging

import stripe
from subhub.auth_validation import get_webhook_values
from subhub.api.webhooks.stripeWebhookPipeline import StripeWebhookPipeline

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def webhook_view() -> tuple:
    logger.info(f"meta {request}")
    try:
        payload = request.data
        sig_header = request.headers['Stripe-Signature']
        endpoint_secret = get_webhook_values()
        logging.info(f'sig header {sig_header}')
        event = stripe.Webhook.construct_event(
          payload, sig_header, endpoint_secret
        )
        p = StripeWebhookPipeline(event)
        logging.info(f"webhok {p}")
        p.run()
    except ValueError as e:
        # Invalid payload
        logging.error(f"ValueError: {e}")
        return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logging.error(f"SignatureVerificationError {e}")
        return Response(status=400)
    except Exception as e:
        logging.error(f"Oops! {e}")
        return Response(e, status=500)
    logging.info(f'event {event}')


    return Response("Success", status=200)
