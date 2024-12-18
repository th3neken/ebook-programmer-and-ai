from abc import ABC, abstractmethod
from utils.position import Position
from config.game_config import GameConfig

class GameElement(ABC):
    def __init__(self, position: Position):
        self.position = position

    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    @abstractmethod
    def interact(self, game_state) -> int:
        pass

class Player(GameElement):
    @property
    def symbol(self) -> str:
        return GameConfig.PLAYER_SYMBOL

    def interact(self, game_state) -> int:
        return 0

class Exit(GameElement):
    @property
    def symbol(self) -> str:
        return GameConfig.EXIT_SYMBOL

    def interact(self, game_state) -> int:
        game_state.game_completed = True
        return 0

class Trap(GameElement):
    @property
    def symbol(self) -> str:
        return GameConfig.TRAP_SYMBOL

    def interact(self, game_state) -> int:
        return GameConfig.TRAP_PENALTY

class Treasure(GameElement):
    def __init__(self, position: Position, collected: bool = False):
        super().__init__(position)
        self.collected = collected

    @property
    def symbol(self) -> str:
        return GameConfig.TREASURE_SYMBOL

    def interact(self, game_state) -> int:
        if not self.collected:
            self.collected = True
            return GameConfig.TREASURE_REWARD
        return 0
