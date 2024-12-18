# Dungeon Explorer

A simple text-based dungeon exploration game where players navigate through a maze while collecting treasures and avoiding traps.

## Description

Dungeon Explorer is a command-line game built in Python where players control a character (@) trying to reach the exit (E) while collecting treasures (*) and avoiding traps (^). The game features a scoring system based on treasures collected and traps triggered.

## Features

- Text-based dungeon visualization
- Random generation of traps and treasures
- Score tracking system
- Move counter
- Simple WASD controls
- Cross-platform compatibility

## How to Play

### Running the Game

```bash
python src/main.py
```

### Controls
- W - Move up
- A - Move left
- S - Move down
- D - Move right
- Q - Quit game

### Game Objectives
- Reach the exit (E)
- Collect treasures (*) to increase score (+20 points)
- Avoid traps (^) to prevent score reduction (-10 points)
- Achieve the highest possible score

## Requirements

- Python 3.12.x
- Compatible with macOS

## Project Structure

```
/
├── src/
│   ├── main.py
│   └── helpers/
│       └── (helper components)
├── prompts/
│   └── (prompt examples)
└── README.md
```

## Author

**Łukasz Boruń**
- Email: lukasz@holistyczny.dev

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.