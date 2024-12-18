from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Position(self.x, self.y)
