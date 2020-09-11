from screen_state.screen_state import ScreenState


class InitialCallScreen(ScreenState):
    """Class that represents the State associated with the Initial Call Screen."""

    def __init__(self, screen):
        self.screen = screen
        self.initials = "TIL"
        self.buttons = ["BL"]
        self.popups = []

    def next_screen(self, next_screen):
        """Set the screen state to the screen received as parameter"""

        self.screen.state = next_screen
