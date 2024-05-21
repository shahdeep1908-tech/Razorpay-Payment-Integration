from pydantic import BaseModel


class GetOrderAmount(BaseModel):
    amount: float

    class Config:
        extra = "forbid"
