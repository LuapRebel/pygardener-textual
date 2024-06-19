import sqlite3

from textual.app import ComposeResult
from textual.screen import ModalScreen, Screen
from textual.widget import Widget
from textual.widgets import Button, DataTable, Footer, Header, Input


class SeedInputScreen(ModalScreen):
    """Modal screen to provide inputs to create a Seed"""

    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Species (e.g. Zea mays)")
        yield Input(placeholder="Brand")
        yield Input(placeholder="Vendor")
        yield Input(placeholder="Quantity", type="integer")
        yield Input(placeholder="Purchase Date")
        yield Input(placeholder="Expiration Date")
        yield Input(placeholder="Description")
        yield Button("Submit", id="button-input-seed")


class SeedsScreen(Screen):
    """Widget to manage seed collections."""

    BINDINGS = [("a", "app.add_seed", "Add Seed")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="seed-table")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM seeds").fetchall()
        columns = [description[0] for description in cur.description]
        table.add_columns(*columns)
        table.add_rows(data)
