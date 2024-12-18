## Requirements

- Python 3.12.x
- Compatible with macOS

## Project Structure

```
root
└── src/
    ├── config/
    │   └── game_config.py              # Stores game constants and configuration settings
    │
    ├── core/
    │   ├── game_engine.py             # Main game loop and orchestrator
    │   └── game_state.py              # Manages game state, scoring, and element positions
    │
    ├── entities/
    │   └── game_element.py            # Defines game elements (Player, Exit, Trap, Treasure)
    │
    ├── ui/
    │   ├── input_handler.py           # Handles player input and movement validation
    │   └── renderer.py                # Manages game display and board rendering
    │
    ├── utils/
    │   └── position.py                # Position data structure for 2D coordinates
    │
    └── main.py                        # Entry point of the application
```
