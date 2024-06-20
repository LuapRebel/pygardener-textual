from datetime import date
from pydantic import BaseModel


class Seed(BaseModel):
    id: int
    species: str | None
    common_name: str | None
    brand: str | None
    vendor: str | None
    quantity: int | None
    days_to_germination: str | None
    days_to_harvest: str | None
    purchase_date: date | None
    expiration_date: date | None
    description: str | None
