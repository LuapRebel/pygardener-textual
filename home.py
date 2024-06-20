from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header, Markdown


MARKDOWN = """
A Python (Textual) TUI to manage garden projects, including the following:

- Seeds
- Plants
- Containers/Locations
- **Garden Events**:
    * Planting
    * Fertilizing
    * Harvesting
"""


class HomeScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Markdown(MARKDOWN)
        yield Footer()
