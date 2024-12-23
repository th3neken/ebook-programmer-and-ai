from abc import ABC, abstractmethod
from utils.position import Position
from config.game_config import GameConfig

class GameElement(ABC):
    """
    Abstract base class representing a game element with position and interaction capabilities.

    Attributes:
        position (Position): The position of the game element on the game board.
    """

    def __init__(self, position: Position):
        """
        Initialize a game element with a position.

        Args:
            position (Position): The position where this element will be placed.
        """
        self.position = position

    @property
    @abstractmethod
    def symbol(self) -> str:
        """
        Get the display symbol for this game element.

        Returns:
            str: A single character representing this element on the game board.
        """
        pass

    @abstractmethod
    def interact(self, game_state) -> int:
        """
        Define interaction behavior when player encounters this element.

        Args:
            game_state: The current state of the game.

        Returns:
            int: Score or penalty points from interacting with this element.
        """
        pass

    @abstractmethod
    def interact_message(self) -> str:
        """
        Get the message to display when interacting with this element.

        Returns:
            str: The message to display during interaction.
        """
        pass

class Player(GameElement):
    @property
    def symbol(self) -> str:
        return GameConfig.PLAYER_SYMBOL

    def interact(self, game_state) -> int:
        return 0

    def interact_message(self) -> str:
        return "You can't interact with yourself!"

class Exit(GameElement):
    @property
    def symbol(self) -> str:
        return GameConfig.EXIT_SYMBOL

    def interact(self, game_state) -> int:
        game_state.game_completed = True
        return 0

    def interact_message(self) -> str:
        return "You found the exit! Game complete!"

class Trap(GameElement):
    @property
    def symbol(self) -> str:
        return GameConfig.TRAP_SYMBOL

    def interact(self, game_state) -> int:
        return GameConfig.TRAP_PENALTY

    def interact_message(self) -> str:
        return f"Ouch! You hit a trap and lost {abs(GameConfig.TRAP_PENALTY)} points!"

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

    def interact_message(self) -> str:
        if not self.collected:
            return f"You found treasure worth {GameConfig.TREASURE_REWARD} points!"
        return "This treasure has already been collected."
