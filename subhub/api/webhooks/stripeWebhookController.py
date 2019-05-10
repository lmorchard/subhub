import json
from flask import request, Response
import sys
import logging

import stripe
from subhub.auth_validation import get_webhook_values
from subhub.api.webhooks.stripeWebhookPipeline import StripeWebhookPipeline


logger = logging.getLogger('webhook_controller')
log_handle = logging.StreamHandler()
log_handle.setLevel(logging.INFO)
logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handle.setFormatter(logformat)
logger.addHandler(log_handle)

def webhook_view() -> tuple:
    logger.info(f"meta {request}")
    try:
        payload = request.data
        sig_header = request.headers['Stripe-Signature']
        endpoint_secret = get_webhook_values()
        logger.info(f'sig header {sig_header}')
        event = stripe.Webhook.construct_event(
          payload, sig_header, endpoint_secret
        )
        p = StripeWebhookPipeline(event)
        logger.info(f"webhook {p}")
        p.run()
    except ValueError as e:
        # Invalid payload
        logger.error(f"ValueError: {e}")
        return Response(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.error(f"SignatureVerificationError {e}")
        return Response(status=400)
    except Exception as e:
        logger.error(f"Oops! {e}")
        return Response(e, status=500)
    
    return Response("Success", status=200)
