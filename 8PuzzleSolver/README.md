# 8-Puzzle Solver (Python 3)

## Language & Requirements

* **Python**: version 3.x (does not matter even version 2 works)
* No external dependencies; uses only the Python standard library.

---

## 📂 Code Structure

* **Functions (11 total)**

  * **Search Algorithms (4)**

    * `bfs(...)`
    * `ucs(...)`
    * `greedy(...)`
    * `a_star(...)`
  * **Output Formatting (3)**

    * `dump_path(...)`
    * `print_solution(...)`
    * `format_stats(...)`
  * **File Handling (2)**

    * `read_puzzle(file_path)`
    * `write_output(file_path, data)`
  * **User Input (1)**

    * `get_user_choice()`
  * **Heuristic (1)**

    * `compute_heuristic(state)`
* **Class (1)**

  * `Puzzle` — encapsulates the game mechanics (moves, state transitions).
* **Main Function (1)**

  * Parses command-line arguments, initializes settings, and invokes the chosen algorithm.
* **Global Variables (2)**

  * `VERBOSE` — flag indicating whether to log intermediate steps.
  * `OUTPUT_FILENAME` — single output file path, opened once to prevent duplication.

---

## 🚀 Usage (Ubuntu / Linux / macOS)

```bash
python3 expense_8_puzzle.py <start_file> <goal_file> <algorithm> <verbose_flag>
```

| Argument         | Description                                                        |
| ---------------- | ------------------------------------------------------------------ |
| `<start_file>`   | Path to the initial puzzle state (e.g., `start.txt`)               |
| `<goal_file>`    | Path to the goal state (e.g., `goal.txt`)                          |
| `<algorithm>`    | One of: `bfs`, `ucs`, `greedy`, `a*`                               |
| `<verbose_flag>` | `0` (disabled) or `1` (enabled). **Do not** use `True` or `False`. |

**Example**

```bash
$ python3 expense_8_puzzle.py start.txt goal.txt bfs 1
```

> **Note:** Running `bfs` or `ucs` with verbose output (`1`) may produce large logs and take longer to complete.

---

## ⚠️ Performance Considerations

* **Breadth-First Search (BFS)** and **Uniform-Cost Search (UCS)** will explore many states; enabling verbose mode can significantly slow execution.
* **Heuristic-based algorithms** (`greedy`, `a*`) generally perform better for larger puzzles.

---
