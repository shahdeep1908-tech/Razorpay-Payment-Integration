from pydantic.v1 import BaseSettings
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


class Setting(BaseSettings):
    RAZORPAY_CLIENT_KEY: str
    RAZORPAY_CLIENT_SECRET: str
    RAZORPAY_WEBHOOK_KEY: str

    class Config:
        env_nested_delimiter = '__'
        env_file = ".env"
        env_file_encoding = "utf-8"


app_settings = Setting()
