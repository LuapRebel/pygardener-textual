from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Footer, Header

from data import SEEDS


class SeedsScreen(Screen):
    """Widget to manage seed collections."""

    BINDINGS = [("a", "add_seed", "Add Seed")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="seed-table")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*SEEDS[0])
        table.add_rows(SEEDS[1:])

    def action_add_seed(self) -> None:
        pass
