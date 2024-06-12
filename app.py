from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from seeds import SeedsTab


class PyGardener(App):

    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield SeedsTab()

    def action_quit(self) -> None:
        self.exit()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


if __name__ == "__main__":
    app = PyGardener()
    app.run()
