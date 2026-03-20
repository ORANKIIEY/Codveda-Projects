# Codveda-Projects
# Number Guessing Game 🎯

A simple command-line game where the player tries to guess a randomly generated number between 1 and 100, with feedback after each guess.

---

## How It Works

The program generates a random number between **1 and 100**. The player has **7 attempts** to guess the correct number. After each guess, the program tells the player whether their guess was too high, too low, or correct. The game ends when the player guesses correctly or runs out of attempts.

---

## Features

- Random number generation using Python's `random` module
- Up to 7 attempts per game
- Feedback on every guess: **Too high**, **Too low**, or **Correct**
- Input validation (handles non-numeric entries and out-of-range guesses)
- Clear end-game message showing the secret number if the player loses

---

## Requirements

- Python 3.x (no external libraries needed)

---

## Getting Started

**Clone or download the project:**

```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
```

**Run the game:**

```bash
python guessing_game.py
```

---

## Example Gameplay

```
Welcome! I'm thinking of a number between 1 and 100.
You have 7 attempts.

Attempt 1/7 — Your guess: 50
Too low! 6 attempts remaining.

Attempt 2/7 — Your guess: 75
Too high! 5 attempts remaining.

Attempt 3/7 — Your guess: 63
Too low! 4 attempts remaining.

Attempt 4/7 — Your guess: 69

🎉 Correct! The number was 69.
You got it in 4 attempts!
```

---

## Project Structure

```
number-guessing-game/
│
└── guessing_game.py   # Main game script
```

---

## Game Rules

| Rule | Detail |
|------|--------|
| Number range | 1 to 100 (inclusive) |
| Maximum attempts | 7 |
| Feedback | Too high / Too low / Correct |
| Invalid input | Skipped — attempt count not penalised |

---

## How to Play

1. Run the script
2. Enter a number between 1 and 100 when prompted
3. Use the **Too high** / **Too low** hints to narrow down your guess
4. Try to guess the number within 7 attempts

---

## Difficulty Tips

- Start with **50** to split the range in half
- Each guess should eliminate half the remaining possibilities
- With perfect play (binary search), you can always win within 7 attempts

---
