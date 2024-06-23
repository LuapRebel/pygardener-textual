import sqlite3

from textual.app import ComposeResult
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, DataTable, Footer, Header, Input

from conn import CONN


class SeedInputScreen(ModalScreen):
    """Modal screen to provide inputs to create a Seed"""

    BINDINGS = [
        ("escape", "app.pop_screen", "Pop screen"),
    ]

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Common Name", id="seed-common-name")
        yield Input(placeholder="Species (e.g. Zea mays)", id="seed-species")
        yield Input(placeholder="Brand", id="seed-brand")
        yield Input(placeholder="Vendor", id="seed-vendor")
        yield Input(placeholder="Quantity", type="integer", id="seed-quantity")
        yield Input(placeholder="Days to Germination", id="seed-days-to-germination")
        yield Input(placeholder="Days to Harvest", id="seed-days-to-harvest")
        yield Input(placeholder="Purchase Date", id="seed-purchase-date")
        yield Input(placeholder="Expiration Date", id="seed-expiration-date")
        yield Input(placeholder="Description", id="seed-description")
        yield Button("Submit", id="seed-input-button")

    def on_button_pressed(self, event: Button.Pressed):
        inputs = self.query(Input)
        seed_data = tuple(i.value for i in inputs)
        cur = CONN.cursor()
        cur.execute(
            """INSERT INTO seeds(common_name, species, brand, vendor, quantity, days_to_germation, days_to_harvest, purchase_date, expiration_date, description) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            seed_data,
        )
        CONN.commit()
        for i in inputs:
            i.clear()
        self.app.push_screen("seeds")


class SeedsScreen(Screen):
    """Widget to manage seed collections."""

    BINDINGS = [("a", "add_seed", "Add Seed")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="seed-table")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        cur = CONN.cursor()
        data = cur.execute("SELECT * FROM seeds").fetchall()
        columns = [description[0] for description in cur.description]
        table.add_columns(*columns)
        table.add_rows(data)

    def _on_screen_resume(self) -> None:
        table = self.query_one(DataTable)
        table.clear()
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM seeds").fetchall()
        table.add_rows(data)

    def action_add_seed(self) -> None:
        self.app.push_screen("seed_input")
