import json

import razorpay
from flask import jsonify
from razorpay import errors

from razorpay_gpay.config import app_settings


class RazorpayIntegration:
    def __init__(self, api_key, api_secret):
        self.client = razorpay.Client(auth=(api_key, api_secret))

    def create_order(self, amount, currency="INR"):
        try:
            data = {
                "amount": amount * 100,  # Razorpay expects amount in paise
                "currency": currency,
                "payment_capture": 1  # Automatically capture the payment
            }
            order = self.client.order.create(data=data)
            return order
        except errors.BadRequestError as err:
            return jsonify({"error": err}), 400
        except (errors.ServerError, errors.GatewayError) as err:
            return jsonify({"error": err}), 500


class RazorpayWebhook:
    @staticmethod
    async def rzp_event_handler(event):
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


_razorpay_client = RazorpayIntegration(api_key=app_settings.RAZORPAY_CLIENT_KEY,
                                       api_secret=app_settings.RAZORPAY_CLIENT_SECRET)
_rzp_webhook = RazorpayWebhook()
