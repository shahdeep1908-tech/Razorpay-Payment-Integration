import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    RAZORPAY_CLIENT_KEY = os.environ.get('RAZORPAY_CLIENT_KEY')
    RAZORPAY_CLIENT_SECRET = os.environ.get('RAZORPAY_CLIENT_SECRET')
    RAZORPAY_WEBHOOK_KEY = os.environ.get('RAZORPAY_WEBHOOK_KEY')


app_settings = Config()
