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

    def row_factory(self, cursor, row):
        fields = [column[0] for column in cursor.description]
        return Seed(**{k: v for k, v in zip(fields, row)})
