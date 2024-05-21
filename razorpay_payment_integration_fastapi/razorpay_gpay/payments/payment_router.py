import json

from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

from config import app_settings, templates
from .payment_schema import GetOrderAmount
from .payment_service import _razorpay_client, _rzp_webhook
from .webhooks.webhook_authentication import verify_razorpay_webhook_signature

from razorpay import errors

router = APIRouter(
    tags=["payment"],
)


@router.get("/pay", response_class=HTMLResponse)
async def get_payment_page(request: Request):
    merchant_key = app_settings.RAZORPAY_CLIENT_KEY
    return templates.TemplateResponse("payment.html", {"request": request, 'merchant_key': merchant_key})


@router.get("/success", response_class=HTMLResponse)
async def redirect_to_success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


@router.get("/cancel", response_class=HTMLResponse)
async def redirect_to_cancel(request: Request):
    return templates.TemplateResponse("cancel.html", {"request": request})


@router.post("/create-order")
async def create_order(request: GetOrderAmount):
    return _razorpay_client.create_order(request.amount)


@router.post("/webhook/razorpay")
async def api_razorpay_webhook(request: Request):
    rzp_signature = request.headers['x-razorpay-signature']
    body = await request.body()
    json_body = json.loads(body)
    payload = json.dumps(json_body, separators=(',', ':'))
    try:
        if verify_razorpay_webhook_signature(payload=payload, rzp_signature=rzp_signature):
            return await(_rzp_webhook.rzp_event_handler(event=payload))
    except (ValueError, errors.SignatureVerificationError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
