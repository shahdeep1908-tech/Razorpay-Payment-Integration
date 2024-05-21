import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_CLIENT_KEY, settings.RAZORPAY_CLIENT_SECRET))


def verify_razorpay_webhook_signature(payload, rzp_signature):
    return client.utility.verify_webhook_signature(body=payload, signature=rzp_signature,
                                                   secret=settings.RAZORPAY_WEBHOOK_KEY)
