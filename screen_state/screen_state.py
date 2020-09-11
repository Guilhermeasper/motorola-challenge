class ScreenState(object):
    """Base state class that implements the behavior shared between screens"""

    valid_actions = ["BL", "BD", "AD", "PQR", "PNA", "PFC"]  # Actions valid to all screens states

    def change_state(self, action):
        """Check received action to change the screen state and return the screen initials or a error message"""

        if action not in self.valid_actions:
            response = "Invalid input"
        elif action not in self.buttons and action not in self.popups:
            response = f'Wrong action for {self.initials} screen'
        elif action == "BL":
            response = self.screen.middle_screen.initials
            self.next_screen(self.screen.middle_screen)
        elif action == "AD":
            response = self.screen.call_screen.initials
            self.next_screen(self.screen.call_screen)
        else:
            response = self.screen.initial_call_screen.initials
            self.next_screen(self.screen.initial_call_screen)

        return response
