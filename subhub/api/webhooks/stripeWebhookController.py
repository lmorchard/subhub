import json
from flask import g, app
import sys

from subhub.api.webhooks.stripeWebhookPipeline import StripeWebhookPipeline


@app.route("/stripe/webhook")
def webhookView(request):
   try:
      event_json = json.loads(request.body)
      p = StripeWebhookPipeline(event_json)
      p.run()
   except:
      print("Oops! ", sys.exc_info()[0], " occurred.")
      return "Error"

   return "success"
