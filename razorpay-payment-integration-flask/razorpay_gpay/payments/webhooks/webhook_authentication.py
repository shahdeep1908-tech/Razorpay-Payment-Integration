import razorpay

from razorpay_gpay.config import app_settings

client = razorpay.Client(auth=(app_settings.RAZORPAY_CLIENT_KEY, app_settings.RAZORPAY_CLIENT_SECRET))


def verify_razorpay_webhook_signature(payload, rzp_signature):
    return client.utility.verify_webhook_signature(body=payload, signature=rzp_signature,
                                                   secret=app_settings.RAZORPAY_WEBHOOK_KEY)
