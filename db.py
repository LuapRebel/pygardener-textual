## ONLY UNCOMMENT AND RUN TO CREATE THE DATABASE
# from conn import CONN
from schemas import Seed


def seed_row_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return Seed(**{k: v for k, v in zip(fields, row)})


CREATE_SEEDS = """
CREATE TABLE IF NOT EXISTS seeds(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    common_name TEXT,
    species TEXT,
    brand TEXT,
    vendor TEXT,
    quantity INTEGER,
    days_to_germination TEXT,
    days_to_harvest TEXT,
    purchase_date DATE,
    expiration_date DATE,
    description TEXT
)
"""
# CONN.execute(CREATE_SEEDS)
# CONN.close()
