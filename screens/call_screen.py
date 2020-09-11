from screen_state.screen_state import ScreenState


class CallScreen(ScreenState):
    """Class that represents the State associated with the Call Screen."""

    def __init__(self, screen):
        self.screen = screen
        self.initials = "TL"
        self.buttons = ["BD"]
        self.popups = ["PQR", "PNA", "PFC"]

    def next_screen(self, next_screen):
        """Set the screen state to the screen received as parameter"""

        self.screen.state = next_screen
