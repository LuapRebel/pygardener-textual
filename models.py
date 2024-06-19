from datetime import date
from pydantic import BaseModel


class Seed(BaseModel):
    id: int
    species: str
    brand: str
    vendor: str
    quantity: int
    purchase_date: date
    expiration_date: date
    description: str
