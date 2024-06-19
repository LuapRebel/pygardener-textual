import sqlite3

import pytest


@pytest.fixture
def create_test_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        """
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
    )
    yield conn


def test_insert_seed(create_test_db):
    cur = create_test_db

    seeds = [
        (
            1,
            "Species1",
            "Brand1",
            "Vendor1",
            100,
            "1990-01-01",
            "1999-12-31",
            "Testing1",
        ),
        (
            2,
            "Species2",
            "Brand2",
            "Vendor2",
            200,
            "2000-01-01",
            "2002-12-31",
            "Testing2",
        ),
    ]

    with cur:
        cur.executemany(
            "INSERT INTO seeds(species, brand, vendor, quantity, purchase_date, expiration_date, description) VALUES(?, ?, ?, ?, ?, ?, ?)",
            [seed[1:] for seed in seeds],
        )
    with cur:
        res = cur.execute("SELECT * FROM seeds WHERE id = 1").fetchone()
        print(res)
        print(seeds[0][1:])
        assert res == seeds[0]
    assert len(list(cur.execute("SELECT * FROM seeds"))) == 2
    cur.close()
