import os

from config.game_config import GameConfig
from utils.position import Position


class GameRenderer:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self, game_state):
        self.clear_screen()
        self._render_header(game_state)
        self._render_board(game_state)
        self._render_footer()

    def _render_header(self, game_state):
        print(f"\nMoves: {game_state.moves} | Score: {game_state.score}")
        print("\n" + "=" * (GameConfig.BOARD_WIDTH + 2))

    def _render_board(self, game_state):
        for y in range(GameConfig.BOARD_HEIGHT):
            print("|", end="")
            for x in range(GameConfig.BOARD_WIDTH):
                current_pos = Position(x, y)
                print(self._get_symbol_at_position(current_pos, game_state), end="")
            print("|")

    def _get_symbol_at_position(self, pos: Position, game_state) -> str:
        if game_state.player.position == pos:
            return game_state.player.symbol
        if game_state.exit.position == pos:
            return game_state.exit.symbol
        for trap in game_state.traps:
            if trap.position == pos:
                return trap.symbol
        for treasure in game_state.treasures:
            if treasure.position == pos and not treasure.collected:
                return treasure.symbol
        if (pos.x == 0 or pos.x == GameConfig.BOARD_WIDTH-1 or
            pos.y == 0 or pos.y == GameConfig.BOARD_HEIGHT-1):
            return GameConfig.WALL_SYMBOL
        return GameConfig.EMPTY_SYMBOL

    def _render_footer(self):
        print("=" * (GameConfig.BOARD_WIDTH + 2))
        print("\nControls: WASD to move, Q to quit")
        print("Legend: @ = You, E = Exit, * = Treasure, ^ = Trap")
