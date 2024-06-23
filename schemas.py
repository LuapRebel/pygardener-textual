from datetime import date
from pydantic import BaseModel


class Seed(BaseModel):
    id: int
    common_name: str | None
    species: str | None = None
    brand: str | None = None
    vendor: str | None = None
    quantity: int | None = None
    days_to_germination: str | None = None
    days_to_harvest: str | None = None
    purchase_date: date | None = None
    expiration_date: date | None = None
    description: str | None = None
