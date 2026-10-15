# Rock, Paper, Scissors (Python)

A simple command-line Rock, Paper, Scissors game played against the computer. The match lasts exactly **3 rounds**, and whoever wins more rounds wins the match. Each round has a countdown and a short time limit for your input.

## Features

- Play against the computer, which picks randomly
- Simple number input: `1` = rock, `2` = paper, `3` = scissors
- Fixed match of 3 rounds with a running score
- "Rock... Paper... Scissors... SHOOT!" countdown so both sides play together
- 5-second time limit to enter your choice (too slow or invalid input = round lost)
- Final result: win, loss or draw

## Requirements

- Python 3.6 or later
- No external libraries (uses only the built-in `random` and `time` modules)

## How to Run

```bash
python rock_paper_scissors.py
```

## How to Play

1. Run the program.
2. Wait for the countdown to reach **SHOOT!**
3. Type `1`, `2` or `3` and press Enter within 5 seconds.
4. The round result and score are shown.
5. After round 3, the final winner is announced.

## Rules

| You | Beats |
|----------|----------|
| Rock | Scissors |
| Paper | Rock |
| Scissors | Paper |

- Same choice by both players = tie (no points)
- Slow or invalid input = computer gets the point
- Most round wins after 3 rounds wins the match; equal wins = draw

## Sample Output

```
--- Round 1 of 3 ---
Rock...
Paper...
Scissors...
SHOOT!
Your choice (1=rock, 2=paper, 3=scissors): 2
You: paper | Computer: rock
You win this round!
Score -> You: 1 | Computer: 0
```

## Configuration

To change the input time limit, edit this line at the top of the file:

```python
TIME_LIMIT = 5  # seconds
```

## Project Structure

```
.
├── rock_paper_scissors.py   # game source code
└── README.md                # this file
```

## Author

Anamika Tiwari (26BAI10028)
