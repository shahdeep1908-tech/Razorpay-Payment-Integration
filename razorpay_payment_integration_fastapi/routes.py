from fastapi import APIRouter
from razorpay_gpay.payments import payment_router

router = APIRouter()


@router.get('/')
def initialization():
    """
    Initialization Endpoint.
    """
    return "The server is running."


"""Authentication route"""
router.include_router(payment_router.router)
