# Red-Blue Nim Game Solver (Python 3.10.12)

An interactive command‑line implementation of the Red‑Blue Nim game featuring Minimax with Alpha‑Beta pruning. The program supports both **standard** and **misère** versions and allows either the **human** or **computer** to move first.

---

## 🐍 Requirements

* **Python 3.x (or even version 2.x works fine)
* No external dependencies (uses only the **`sys`** module for argument parsing)

---

## ⚙️ Code Structure

The code is organized into globals, helper functions, game‑mechanics functions, and the main entry point. It assumes the user provides valid arguments and move choices.

1. **Imports & Globals**

   * `import sys` — handle command‑line arguments.
   * `MAX`, `MIN` — representations of infinity for Minimax evaluation.

2. **Core Functions (7)**

   * **`settingUp(red, blue, version, first_player)`**
     Display initial settings and launch the game loop.
   * **`nim_game(red, blue, version, first_player)`**
     Main game loop: alternates turns until one pile is empty.
   * **`humanTurn(red, blue)`**
     Prompt the player to remove 1 or 2 marbles of a chosen color.
   * **`possibleMoves(red, blue)`**
     Generate up to four valid successor states: remove 1 or 2 marbles from red or blue.
   * **`computerTurn(red, blue, version)`**
     Evaluate all possible moves via Minimax + Alpha‑Beta, pick the best, and return it.
   * **`MinMax_AlphaBeta(red, blue, version, is_max_turn, alpha, beta)`**
     Recursive Minimax with Alpha‑Beta pruning and terminal‑state scoring (differs for standard vs misère).
   * **`endGame(red, blue, version)`**
     Announce the winner, apply scoring rules for standard or misère play.

3. **Main Entry Point**

   * Parses and validates `sys.argv`:

     ```text
     <num-red> <num-blue> <version> <first-player>
     ```
   * Defaults:

     * `version`: `standard` (or `misere`),
     * `first-player`: `human` (or `computer`).
   * Calls `settingUp(...)` to start.

---

## 🚀 Running the Game

1. **Navigate** to the script directory:

   ```bash
   cd path/to/directory
   ```

2. **Run** on Linux/macOS/Omega Server:

   ```bash
   python3 red_blue_nim.py <num-red> <num-blue> [version] [first-player]
   ```

3. **Run** on Windows:

   ```powershell
   python red_blue_nim.py <num-red> <num-blue> [version] [first-player]
   ```

| Argument         | Description                      |
| ---------------- | -------------------------------- |
| `<num-red>`      | Initial red marbles (integer)    |
| `<num-blue>`     | Initial blue marbles (integer)   |
| `[version]`      | `standard` (default) or `misere` |
| `[first-player]` | `human` (default) or `computer`  |

> **Example** (using defaults for `version` and `first-player`):
>
> ```bash
> python3 red_blue_nim.py 10 8
> ```

---

## ❗ Usage Notes

* **Input Validation**: The program assumes correct arguments and move choices. If invalid input is detected, please restart and try again.
* **Move Rules**: On your turn, you may remove **1** or **2** marbles of **one** color (`red` or `blue`).
* **Performance**: Minimax with Alpha‑Beta pruning explores the full game tree—game sizes beyond \~15 marbles per pile may be slow.

---

Enjoy the game! 🎮
