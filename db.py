from datetime import date

import sqlite3


con = sqlite3.connect("data.db")
cur = con.cursor()

create_seeds = """
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
cur.execute(create_seeds)

insert_seeds = """
    INSERT INTO seeds(species, brand, vendor, quantity, purchase_date, expiration_date, description) VALUES
    ("Zea mays", "Jerky Seed Co.", "Encinal", 100, "2024-01-01", "2025-01-01", "Awesome"),
    ("Phaesoleus vulgaris", "Super Seed Co.", "Amazon", 200, "2024-03-12", "2026-01-01", "Sweet!");
"""

cur.execute(insert_seeds)
con.commit()
con.close()
