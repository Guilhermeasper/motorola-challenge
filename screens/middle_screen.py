from screen_state.screen_state import ScreenState


class MiddleScreen(ScreenState):
    """Class that represents the State associated with the Middle Screen."""

    def __init__(self, screen):
        self.screen = screen
        self.initials = "TI"
        self.buttons = ["BD"]
        self.popups = ["AD", "PQR", "PNA"]

    def next_screen(self, next_screen):
        """Set the screen state to the screen received as parameter"""

        self.screen.state = next_screen
