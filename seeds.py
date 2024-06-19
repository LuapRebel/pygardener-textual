import sqlite3

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Footer, Header


class SeedsScreen(Screen):
    """Widget to manage seed collections."""

    BINDINGS = [("a", "add_seed", "Add Seed")]

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

    def action_add_seed(self) -> None:
        pass
