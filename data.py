from datetime import date

COLUMNS = [
    ("id", int),
    ("species", str),
    ("brand", str),
    ("vendor", str),
    ("quantity", int),
    ("purchase_date", date),
    ("expiration_date", date),
    ("description", str),
]

SEEDS = [
    (c[0] for c in COLUMNS),
    (
        1,
        "Zea mays",
        "Jerky Seed Co.",
        "Encinal",
        100,
        date(2024, 1, 1),
        date(2025, 1, 1),
        "Awesome",
    ),
    (
        2,
        "Phaesoleus vulgaris",
        "Super Seed Co.",
        "Amazon",
        200,
        date(2024, 3, 12),
        date(2026, 1, 1),
        "Sweet!",
    ),
]
