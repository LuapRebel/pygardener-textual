from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Markdown

from seeds import SeedInputScreen, SeedsScreen


with open("README.md") as file:
    MARKDOWN = file.read()


class HomeScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Markdown(markdown=MARKDOWN)
        yield Footer()


class PyGardener(App):

    CSS_PATH = "app.tcss"
    SCREENS = {
        "home": HomeScreen(),
        "seeds": SeedsScreen(),
        "seed_input": SeedInputScreen(),
    }
    BINDINGS = [
        ("h", "push_screen('home')", "Home"),
        ("s", "push_screen('seeds')", "View Seeds"),
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.push_screen(HomeScreen())

    def action_quit(self) -> None:
        self.exit()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_add_seed(self) -> None:
        self.push_screen("seed_input")


if __name__ == "__main__":
    app = PyGardener()
    app.run()
