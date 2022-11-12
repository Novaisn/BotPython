from src.games.DayAndNight.action import DayAndNightAction
from src.games.DayAndNight.player import DayAndNightPlayer
from src.games.DayAndNight.state import DayAndNightState


class HumanDayAndNightPlayer(DayAndNightPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DayAndNightState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                state.get_acting_player()
                return DayAndNightAction(int(input(f"Player {state.get_acting_player()}, choose a column and row: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: DayAndNightState):
        # ignore
        pass

    def event_end_game(self, final_state: DayAndNightState):
        # ignore
        pass
