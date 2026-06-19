# 🤖 Tic-Tac-Toe AI

A beginner-friendly Streamlit project that lets a human play Tic-Tac-Toe against an unbeatable AI powered by the Minimax algorithm.

## Project Description

This application implements the classic 3×3 Tic-Tac-Toe game with a clean Streamlit interface. The human plays as X and the AI plays as O. The AI evaluates every possible outcome using Minimax and always selects the optimal move.

## Features

- Human vs AI gameplay.
- Human plays as X.
- AI plays as O.
- Standard 3×3 board.
- Win detection.
- Draw detection.
- Game-over protection.
- Restart option.
- Clean dark-themed UI.
- Separate game logic and AI logic modules.

## Technologies Used

- Python
- Streamlit
- Minimax algorithm

## Project Structure

```text
Task2_TicTacToe_AI/
├── app.py
├── game_logic.py
├── minimax.py
├── requirements.txt
├── README.md
└── screenshots/
```

## How to Run

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Launch the app:

```bash
streamlit run app.py
```

## Minimax Algorithm Explanation

Minimax is a recursive decision-making algorithm used in two-player zero-sum games.

- The AI treats itself as the maximizing player.
- The human is treated as the minimizing player.
- Every possible move is simulated until the game ends.
- Terminal outcomes are scored as:
  - AI win = +1
  - Human win = -1
  - Draw = 0

The AI chooses the move that produces the best guaranteed result, which makes it unbeatable when the algorithm is implemented correctly.

## Screenshots

Add screenshots of the application in this folder:

- `screenshots/`

Suggested screenshots:
- Home screen
- Human turn
- AI winning state
- Draw state

## Notes

- The UI is intentionally kept separate from the game logic.
- No machine learning, databases, APIs, or external AI services are used.
