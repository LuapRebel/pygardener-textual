## ONLY UNCOMMENT AND RUN TO CREATE THE DATABASE
# from conn import CONN
from models import Seed

# cur = CONN.cursor()


def seed_row_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return Seed(**{k: v for k, v in zip(fields, row)})


CREATE_SEEDS = """
CREATE TABLE IF NOT EXISTS seeds(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    species TEXT,
    brand TEXT,
    vendor TEXT,
    quantity INTEGER,
    purchase_date DATE,
    expiration_date DATE,
    description TEXT
)
"""
# cur.execute(CREATE_SEEDS)
# CONN.close()
