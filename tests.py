import sqlite3

import pytest

from db import CREATE_SEEDS, INSERT_SEEDS
from db import seed_row_factory
from models import Seed


@pytest.fixture
def create_test_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(CREATE_SEEDS)
    yield conn


def test_insert_seed(create_test_db):
    cur = create_test_db
    cur.row_factory = seed_row_factory

    with cur:
        cur.execute(INSERT_SEEDS)

    with cur:
        res = cur.execute("SELECT * FROM seeds WHERE id = 1").fetchone()
        print(res)
        print(type(res))
        assert res == Seed(
            id=1,
            species="Zea mays",
            brand="Jerky Seed Co.",
            vendor="Encinal",
            quantity=100,
            purchase_date="2024-01-01",
            expiration_date="2025-01-01",
            description="Awesome",
        )
    assert len(list(cur.execute("SELECT * FROM seeds"))) == 2
    cur.close()
