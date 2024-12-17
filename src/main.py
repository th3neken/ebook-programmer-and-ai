import random
import os
import time

class DungeonExplorer:
    def __init__(self):
        self.width = 20
        self.height = 10
        self.player_pos = [1, 1]
        self.exit_pos = [self.width-2, self.height-2]
        self.traps = []
        self.treasures = []
        self.score = 0
        self.moves = 0
        self.generate_elements()


    def generate_elements(self):

        for _ in range(5):
            while True:
                x = random.randint(1, self.width-2)
                y = random.randint(1, self.height-2)
                pos = [x, y]
                if (pos != self.player_pos and pos != self.exit_pos and
                    pos not in self.traps and pos not in self.treasures):
                    self.traps.append(pos)
                    break

        for _ in range(3):
            while True:
                x = random.randint(1, self.width-2)
                y = random.randint(1, self.height-2)
                pos = [x, y]
                if (pos != self.player_pos and pos != self.exit_pos and
                    pos not in self.traps and pos not in self.treasures):
                    self.treasures.append(pos)
                    break

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_game(self):
        self.clear_screen()
        print(f"\nMoves: {self.moves} | Score: {self.score}")
        print("\n" + "=" * (self.width + 2))

        for y in range(self.height):
            print("|", end="")
            for x in range(self.width):
                pos = [x, y]
                if pos == self.player_pos:
                    print("@", end="")
                elif pos == self.exit_pos:
                    print("E", end="")
                elif pos in self.traps:
                    print("^", end="")
                elif pos in self.treasures:
                    print("*", end="")
                elif x == 0 or x == self.width-1 or y == 0 or y == self.height-1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("|")

        print("=" * (self.width + 2))
        print("\nControls: WASD to move, Q to quit")
        print("Legend: @ = You, E = Exit, * = Treasure, ^ = Trap")

    def play(self):
        while True:
            self.draw_game()

            move = input("\nEnter your move: ").lower()
            self.moves += 1

            if move == 'q':
                print("\nThanks for playing!")
                break

            new_pos = self.player_pos.copy()

            if move == 'w' and new_pos[1] > 1:
                new_pos[1] -= 1
            elif move == 's' and new_pos[1] < self.height-2:
                new_pos[1] += 1
            elif move == 'a' and new_pos[0] > 1:
                new_pos[0] -= 1
            elif move == 'd' and new_pos[0] < self.width-2:
                new_pos[0] += 1

            if new_pos in self.traps:
                print("\nOh no! You hit a trap!")
                self.score -= 10
                time.sleep(1)

            if new_pos in self.treasures:
                print("\nYou found a treasure!")
                self.score += 20
                self.treasures.remove(new_pos)
                time.sleep(1)

            self.player_pos = new_pos

            if self.player_pos == self.exit_pos:
                self.draw_game()
                print(f"\nCongratulations! You escaped the dungeon!")
                print(f"Final Score: {self.score} in {self.moves} moves")
                break

if __name__ == "__main__":
    print("\nWelcome to Dungeon Explorer!")
    print("Find treasures and reach the exit while avoiding traps.")
    input("Press Enter to start...")

    game = DungeonExplorer()
    game.play()
