from textual.app import ComposeResult
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import DataTable

from data import SEEDS


class SeedsTab(Widget):
    """Widget to manage seed collections."""

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*SEEDS[0])
        table.add_rows(SEEDS[1:])
