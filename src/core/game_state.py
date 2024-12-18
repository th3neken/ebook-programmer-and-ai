from typing import List
from utils.position import Position
from entities.game_element import GameElement, Player, Exit, Trap, Treasure
from config.game_config import GameConfig

import random

class GameState:
    def __init__(self):
        self.score = 0
        self.moves = 0
        self.game_completed = False
        self.traps = []
        self.treasures = []
        self.initialize_game()

    def initialize_game(self):
        self.player = Player(Position(1, 1))
        self.exit = Exit(Position(GameConfig.BOARD_WIDTH-2, GameConfig.BOARD_HEIGHT-2))
        self.traps = self._generate_elements(Trap, GameConfig.TRAP_COUNT)
        self.treasures = self._generate_elements(Treasure, GameConfig.TREASURE_COUNT)

    def _generate_elements(self, element_class, count) -> List[GameElement]:
        elements = []
        while len(elements) < count:
            pos = Position(
                random.randint(1, GameConfig.BOARD_WIDTH-2),
                random.randint(1, GameConfig.BOARD_HEIGHT-2)
            )
            if not self._is_position_occupied(pos):
                elements.append(element_class(pos))
        return elements

    def _is_position_occupied(self, pos: Position) -> bool:
        if pos == self.player.position or pos == self.exit.position:
            return True
        return any(element.position == pos for element in self.traps + self.treasures)

    def update(self, new_position: Position):
        self.moves += 1
        self.player.position = new_position

        # Check interactions
        if self.player.position == self.exit.position:
            self.exit.interact(self)
            return

        for trap in self.traps:
            if self.player.position == trap.position:
                self.score += trap.interact(self)

        for treasure in self.treasures:
            if self.player.position == treasure.position:
                self.score += treasure.interact(self)
