import json

from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from razorpay import errors

from .services import _razorpay_client, _rzp_webhook
from .webhooks.webhook_authentication import verify_razorpay_webhook_signature


def home(request):
    merchant_key = settings.RAZORPAY_CLIENT_KEY
    return render(request, 'payment.html', context={'merchant_key': merchant_key})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def create_order(request):
    merchant_key = settings.RAZORPAY_CLIENT_KEY
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode('utf-8'))
            amount = float(body.get('amount'))
            response = _razorpay_client.create_order(amount=amount)
            return JsonResponse(response)
        except Exception as err:
            return HttpResponse(f"{err}", status=500)
    return render(request, 'payment.html', context={'merchant_key': merchant_key})


@csrf_exempt
def api_razorpay_webhook(request):
    if request.method == 'POST':
        rzp_signature = request.headers['x-razorpay-signature']
        body = request.body
        json_body = json.loads(body)
        payload = json.dumps(json_body, separators=(',', ':'))
        try:
            if verify_razorpay_webhook_signature(payload=payload, rzp_signature=rzp_signature):
                _rzp_webhook.rzp_event_handler(event=payload)
            return HttpResponse({"message": "Webhook processed successfully"}, status=200)
        except (ValueError, errors.SignatureVerificationError) as err:
            return HttpResponse(f"{err}", status=500)
    return HttpResponse({"message": "Webhook processed failure"}, status=400)
