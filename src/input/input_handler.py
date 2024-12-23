from utils.position import Position
from config.game_config import GameConfig
from readchar import readchar

class InputHandler:
    @staticmethod
    def get_move(current_position: Position) -> Position:
        while True:
            key = readchar()
            new_pos = current_position.copy()

            if key == 'q':
                raise Exception("Not implemented yet")
            elif key == 'w' and new_pos.y > 1:
                new_pos.y -= 1
            elif key == 's' and new_pos.y < GameConfig.BOARD_HEIGHT-2:
                new_pos.y += 1
            elif key == 'a' and new_pos.x > 1:
                new_pos.x -= 1
            elif key == 'd' and new_pos.x < GameConfig.BOARD_WIDTH-2:
                new_pos.x += 1

            return new_pos
