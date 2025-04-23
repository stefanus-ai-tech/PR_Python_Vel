---

**Project Title:** Command-Line Hangman Game in Java

**Objective:**
Develop a simple command-line based Hangman game in Java. The game should replicate the core logic and user experience of the provided Python example.

**Core Requirements:**

1.  **Word List & Selection:**

    - Define a list (e.g., `String[]` or `ArrayList<String>`) containing a few potential words for the game (e.g., "aardvark", "baboon", "camel").
    - At the start of each game, randomly select one word from this list to be the hidden word.

2.  **Game Initialization:**

    - Display a welcoming message to the player.
    - Initialize the number of lives the player has (e.g., 10).
    - Create a display representation of the hidden word using underscores (`_`) for each letter (e.g., `_ _ _ _ _`).
    - Keep track of letters the player has already guessed (e.g., using an `ArrayList<Character>` or `HashSet<Character>`).

3.  **Game Loop:**

    - The game should continue as long as the player has lives remaining and hasn't guessed the word.
    - In each turn:
      - Display the current number of lives remaining.
      - Display the current state of the hidden word (e.g., `_ a _ _ _ _ k`).
      - Prompt the user to guess a letter.

4.  **Input Handling:**

    - Read the user's input (e.g., using `java.util.Scanner`).
    - Convert the input to lowercase for case-insensitive comparison.
    - **Validation:** Ensure the input is a single alphabetical character. If not, display an error message and prompt again without penalty.
    - **Check Previous Guesses:** If the letter has already been guessed, inform the player and prompt again without penalty. Add the valid, new guess to the list of guessed letters.

5.  **Guess Evaluation:**

    - Check if the guessed letter exists in the chosen hidden word.
    - **Correct Guess:**
      - Inform the player they guessed correctly.
      - Update the display representation by revealing the guessed letter in all its correct positions.
    - **Incorrect Guess:**
      - Inform the player the guess was wrong.
      - Decrement the player's remaining lives.

6.  **Win/Loss Conditions:**

    - **Win:** If the display representation no longer contains any underscores (`_`), the player has guessed the word. Set the game over flag, congratulate the player, and reveal the full word.
    - **Loss:** If the player's lives reach 0, the game is over. Set the game over flag, inform the player they lost, and reveal the full word.

7.  **Code Structure:**
    - Use appropriate Java classes and methods. Consider creating helper methods (like `findCharIndices` in the Python example) to keep the main game loop clean.

**Example Interaction Flow:**

```
Welcome to the hangman game! choose a letter from the chosen word until complete,choose wrong letter then the Man will be hanged
Your current lives is 10
_ _ _ _ _ _
Guess a letter that is correct to the word: a
Right
====================
Your current lives is 10
_ a _ _ _ _
Guess a letter that is correct to the word: e
Wrong
====================
Your current lives is 9
_ a _ _ _ _
Guess a letter that is correct to the word: a
The letter a has been guessed, try again!
Your current lives is 9
_ a _ _ _ _
Guess a letter that is correct to the word: 1
Invalid input!, only input 1 character only
Your current lives is 9
_ a _ _ _ _
Guess a letter that is correct to the word: ... [Game continues] ...

// End Game Scenarios
====================
Congrats, you win!
The word was: [chosen_word]
====================

// OR

====================
Damn, you lose!
The word was: [chosen_word]
====================
```
