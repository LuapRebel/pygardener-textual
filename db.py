from datetime import date

import sqlite3

from models import Seed

con = sqlite3.connect("data.db")
cur = con.cursor()


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
cur.execute(CREATE_SEEDS)

INSERT_SEEDS = """
    INSERT INTO seeds(species, brand, vendor, quantity, purchase_date, expiration_date, description) VALUES
    ("Zea mays", "Jerky Seed Co.", "Encinal", 100, "2024-01-01", "2025-01-01", "Awesome"),
    ("Phaesoleus vulgaris", "Super Seed Co.", "Amazon", 200, "2024-03-12", "2026-01-01", "Sweet!");
"""

cur.execute(INSERT_SEEDS)
con.commit()
con.close()
