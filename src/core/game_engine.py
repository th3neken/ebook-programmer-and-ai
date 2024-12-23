from core.game_state import GameState
from ui.renderer import GameRenderer
from input.input_handler import InputHandler

class GameEngine:
    def __init__(self):
        self.state = GameState()
        self.renderer = GameRenderer()
        self.input_handler = InputHandler()

    def run(self):
        print("\nWelcome to Dungeon Explorer!")
        print("Find treasures and reach the exit while avoiding traps.")
        input("Press Enter to start...")

        while not self.state.game_completed:
            self.renderer.render(self.state)
            new_position = self.input_handler.get_move(self.state.player.position)

            if new_position is None:  # Player quit
                break

            self.state.update(new_position)

        if self.state.game_completed:
            self.renderer.render(self.state)
            print("\nCongratulations! You escaped the dungeon!")
            print(f"Final Score: {self.state.score} in {self.state.moves} moves")
