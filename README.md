# Word Guessing Game (Python)

## Overview

This is a simple **command-line word guessing game** written in Python. The player must guess the hidden word one character at a time within a limited number of attempts. The game randomly selects a word from a predefined list and displays progress after each guess.

This project is suitable for **Python beginners** and helps practice:

* Loops
* Conditionals
* Strings
* User input
* Basic game logic

---

## How the Game Works

1. The user enters their name.
2. The program randomly selects a word from a list.
3. The word is hidden using underscores (`_`).
4. The player guesses one character at a time.
5. Correct guesses reveal characters in the word.
6. Incorrect guesses reduce the remaining attempts.
7. The player wins if all characters are guessed before attempts run out.

---

## Rules

* You have **10 total guesses**.
* Only **single characters** should be entered.
* Repeated guesses are allowed but still count.
* The game ends when:

  * All characters are guessed (Win), or
  * Attempts reach zero (Lose).

---

## Requirements

* Python 3.x
* No external libraries required (uses Python's built-in `random` module)

---

## How to Run

1. Save the script as `word_guessing_game.py`
2. Open a terminal or command prompt
3. Run the following command:

```bash
python word_guessing_game.py
```

---

## Sample Output

```
Enter your name: Alex
Good Luck, Alex!
Guess the characters
_ _ _ _ _ _
guess a character: p
Wrong
You have 9 more guesses
```

---

## File Structure

```
word_guessing_game.py
README.md
```

---

## Possible Improvements

* Prevent duplicate guesses
* Validate single-character input
* Add difficulty levels
* Display guessed letters
* Convert to a Hangman-style game

---

## Author

Created as a beginner Python practice project.

---

## License

This project is open-source and free to use for learning purposes.
