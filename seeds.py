from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer, Header

from data import SEEDS


class SeedsApp(App):
    """App to manage seed collections."""

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode"), ("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*SEEDS[0])
        table.add_rows(SEEDS[1:])

    def action_quit(self) -> None:
        self.exit()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


app = SeedsApp()
if __name__ == "__main__":
    app.run()
