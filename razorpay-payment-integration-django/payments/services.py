import json

import razorpay
from django.conf import settings
from django.http import HttpResponse
from razorpay import errors


class RazorpayIntegration:
    def __init__(self, api_key, api_secret):
        self.client = razorpay.Client(auth=(api_key, api_secret))

    def create_order(self, amount, currency="INR"):
        try:
            data = {
                "amount": amount * 100,  # Razorpay expects amount in paise
                "currency": currency,
                "payment_capture": 0
            }
            order = self.client.order.create(data=data)
            return order
        except errors.BadRequestError as err:
            return HttpResponse(f"{err}", status=400)
        except (errors.ServerError, errors.GatewayError) as err:
            return HttpResponse(f"{err}", status=500)


class RazorpayWebhook:
    @staticmethod
    def rzp_event_handler(event):
        event_data = json.loads(event)
        try:
            print(f"event ::: {event_data['event']} ::: ---------->")
            print(f"paymentID ::: {event_data['payload']['payment']['entity']['id']} ::: ---------->")
            print(f"amount ::: {event_data['payload']['payment']['entity']['amount'] / 100} ::: ---------->")
            print(f"status ::: {event_data['payload']['payment']['entity']['status']} ::: ---------->")
            print(f"orderID ::: {event_data['payload']['payment']['entity']['order_id']} ::: ---------->")
            print(f"cardDetail ::: {event_data['payload']['payment']['entity']['acquirer_data']} ::: ---------->")
            print(f"emailID ::: {event_data['payload']['payment']['entity']['email']} ::: ---------->")
            print(f"contactNumber ::: {event_data['payload']['payment']['entity']['contact']} ::: ---------->")
            print(":::" * 20)
        except Exception as err:
            print(f"WEBHOOK ERROR ::: {err}")


_razorpay_client = RazorpayIntegration(settings.RAZORPAY_CLIENT_KEY, settings.RAZORPAY_CLIENT_SECRET)
_rzp_webhook = RazorpayWebhook()
