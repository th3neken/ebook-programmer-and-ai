from utils.position import Position
from config.game_config import GameConfig

class InputHandler:
    @staticmethod
    def get_move(current_position: Position) -> Position:
        while True:
            move = input("\nEnter your move: ").lower()
            new_pos = current_position.copy()

            if move == 'q':
                raise Exception("Not implemented yet")
            elif move == 'w' and new_pos.y > 1:
                new_pos.y -= 1
            elif move == 's' and new_pos.y < GameConfig.BOARD_HEIGHT-2:
                new_pos.y += 1
            elif move == 'a' and new_pos.x > 1:
                new_pos.x -= 1
            elif move == 'd' and new_pos.x < GameConfig.BOARD_WIDTH-2:
                new_pos.x += 1

            return new_pos
