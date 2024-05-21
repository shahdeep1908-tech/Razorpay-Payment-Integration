import json

from flask import request, render_template, jsonify
from razorpay import errors

from app import app

from .services import _razorpay_client, _rzp_webhook
from ..config import app_settings
from .webhooks.webhook_authentication import verify_razorpay_webhook_signature


@app.route('/')
def index():
    merchant_key = app_settings.RAZORPAY_CLIENT_KEY
    return render_template('payment.html', merchant_key=merchant_key)


@app.route('/success')
async def redirect_to_success():
    return render_template('success.html')


@app.route('/cancel')
async def redirect_to_cancel():
    return render_template('cancel.html')


@app.route('/create-order', methods=['POST'])
def create_order():
    data = request.json
    return _razorpay_client.create_order(float(data['amount']))


@app.route("/webhook/razorpay", methods=['POST'])
async def api_razorpay_webhook():
    rzp_signature = request.headers['x-razorpay-signature']
    data = request.json
    payload = json.dumps(data, separators=(',', ':'))
    try:
        if verify_razorpay_webhook_signature(payload=payload, rzp_signature=rzp_signature):
            await(_rzp_webhook.rzp_event_handler(event=payload))
        return jsonify({"message": "Webhook processed successfully"}), 200
    except (ValueError, errors.SignatureVerificationError) as err:
        return jsonify({"error": err}), 400
