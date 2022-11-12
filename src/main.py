from src.games.DayAndNight.players.human import HumanDayAndNightPlayer
from src.games.game_simulator import GameSimulator
from src.games.DayAndNight.simulator import DayAndNightSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1

    day_and_night_simulations = [
        {
        "name": "DayAndNight - Human VS Human",
        "player1": HumanDayAndNightPlayer("Human1"),
        "player2": HumanDayAndNightPlayer("Human2")
        }
    ]

    for sim in day_and_night_simulations:
        run_simulation(sim["name"], DayAndNightSimulator(sim["player1"], sim["player2"]), num_iterations)

if __name__ == "__main__":
    main()
