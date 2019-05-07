import json
from django.http import HttpResponse

from subhub.api.webhooks.stripeWebhookPipeline import StripeWebhookPipeline


def webhookView(request):
   event_json = json.loads(request.body)
   p = StripeWebhookPipeline(event_json)
   p.run()
   return HttpResponse(status=200)