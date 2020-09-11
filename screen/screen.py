from screens.call_screen import CallScreen
from screens.inital_call_screen import InitialCallScreen
from screens.middle_screen import MiddleScreen


class Screen(object):
    """Class that represents the screen itself and instantiates all subscreens"""

    def __init__(self):
        self.initial_call_screen = InitialCallScreen(self)
        self.call_screen = CallScreen(self)
        self.middle_screen = MiddleScreen(self)
        self.state = self.initial_call_screen

    def change_state(self, action):
        """Return the next screen initials or a error message"""

        return self.state.change_state(action)
