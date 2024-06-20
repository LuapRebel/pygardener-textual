import sqlite3

import pytest

from db import CREATE_SEEDS
from db import seed_row_factory
from models import Seed


@pytest.fixture
def create_test_db():
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute(CREATE_SEEDS)
    yield conn


def test_insert_seed(create_test_db):
    conn = create_test_db
    conn.row_factory = seed_row_factory

    with conn:
        conn.execute(
            """
            INSERT INTO seeds(species, common_name, brand, vendor, quantity, days_to_germination, days_to_harvest, purchase_date, expiration_date, description) VALUES
            ("Zea mays", "Corn", "Jerky Seed Co.", "Encinal", 100, "10-12", "100-110", "2024-01-01", "2025-01-01", "Awesome"),
            ("Phaesoleus vulgaris", "Beans", "Super Seed Co.", "Amazon", 200, "10-14", "75-80", "2024-03-12", "2026-01-01", "Sweet!");
            """
        )

    with conn:
        res = conn.execute("SELECT * FROM seeds WHERE id = 1").fetchone()
        assert res == Seed(
            id=1,
            species="Zea mays",
            common_name="Corn",
            brand="Jerky Seed Co.",
            vendor="Encinal",
            quantity=100,
            days_to_germination="10-12",
            days_to_harvest="100-110",
            purchase_date="2024-01-01",
            expiration_date="2025-01-01",
            description="Awesome",
        )
    assert len(list(conn.execute("SELECT * FROM seeds"))) == 2
    conn.close()
