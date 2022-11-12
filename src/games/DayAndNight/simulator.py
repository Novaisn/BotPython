from src.games.DayAndNight.player import DayAndNightPlayer
from src.games.DayAndNight.state import DayAndNightState
from src.games.game_simulator import GameSimulator


class DayAndNightSimulator(GameSimulator):

    def __init__(self, player1: DayAndNightPlayer, player2: DayAndNightPlayer):
        super(DayAndNightSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """


    def init_game(self):
        return DayAndNightState()

    def before_end_game(self, state: DayAndNightState):
        # ignored for this simulator
        pass

    def end_game(self, state: DayAndNightState):
        # ignored for this simulator
        pass