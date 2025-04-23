import random
import string

print("Welcome to the hangman game! choose a letter from the chosen word until complete,choose wrong letter then the Man will be hanged")
word_list = ["aardvark", "baboon", "camel"]
choosen_word = random.choice(word_list)
choosen_word_split = choosen_word.split()
placeholder_string = ["_"] * len(choosen_word)
lives = 10
game_over = False
guessed = []

def findCharIndices(search_char, word):
  indices = []
  for i, letter in enumerate(word):
    if letter == search_char:
      indices.append(i)
  return indices
  
while not game_over:
  print(f"Your current lives is {lives}")
  print(' '.join(placeholder_string))
  while True: 
    user_choice = (input("Guess a letter that is correct to the word: ").lower())
    if len(user_choice) == 1 and user_choice in string.ascii_letters:
      break
    print("Invalid input!, only input 1 character only")
  if user_choice in guessed:
    print(f"The letter {user_choice} has been guessed, try again!")
  guessed.append(user_choice)

  
  if user_choice in choosen_word:
    print("Right")
    found_at = findCharIndices(user_choice, choosen_word)
    if found_at:
      for i in found_at:
        placeholder_string[i] = user_choice
    print("="*20)
    if "_" not in placeholder_string:
      game_over = True
      print("="*20)
      print("Congrats, you win!")
      print(f"The word was: {choosen_word}")
      print("="*20)
  else:
    print("Wrong")
    lives -= 1
    print("="*20)

  if lives == 0:
      game_over = True
      print("="*20)
      print("Damn, you lose!")
      print(f"The word was: {choosen_word}")
      print("="*20)
    

  


"""
Based on your Python Hangman game code, here are some of the Python techniques you are using:

1.  **Importing Modules:**
    * You are using the `import` statement to bring in functionality from the `random` and `string` modules.
    * `random` is used for selecting a random word from the `word_list`.
    * `string` is used to access a collection of letters (`string.ascii_letters`) for input validation.

2.  **Lists:**
    * You are using lists to store the `word_list`, the split version of the chosen word 
    (though this isn't strictly necessary as strings are iterable), the `placeholder_string` 
    representing the unguessed letters, and the `guessed` letters.

3.  **Strings:**
    * You are working with strings for the words in the `word_list`, 
    the `choosen_word`, and the user's `user_choice`.

4.  **Variables:**
    * You are using variables to store different aspects of the game state, such as `lives`, `game_over`, and the chosen word.

5.  **Functions:**
    * You have defined a function called `findCharIndices` to find all the 
    indices of a specific character within a word. This demonstrates code modularity and reusability.

6.  **Loops:**
    * You are using a `while` loop (`while not game_over:`) to control 
    the main game flow, continuing as long as the game is not over.
    * You have another `while True:` loop for input validation, ensuring 
    the user enters a single letter.
    * Inside the `findCharIndices` function, you use a `for` loop to 
    iterate through the letters of the word.

7.  **Conditional Statements:**
    * You are using `if`, `elif`, and `else` statements to handle different 
    scenarios, such as checking if the user's guess is correct, if they have 
    already guessed the letter, or if they have run out of lives.

8.  **String Methods:**
    * `.choice()` from the `random` module is used to select a random element from the `word_list`.
    * `.split()` is used (though it's called on the `choosen_word` which is 
    already a string, so it doesn't actually split it further). You could directly iterate or index the `choosen_word` string.
    * `.lower()` is used to convert the user's input to lowercase for case-insensitive comparison.
    * `.join()` is used to convert the `placeholder_string` list into a string with spaces in between for printing.

9.  **List Operations:**
    * You are creating the `placeholder_string` using list multiplication (`["_"] * len(choosen_word)`).
    * You are accessing and modifying elements within the `placeholder_string` using indexing 
    (e.g., `placeholder_string[i] = user_choice`).
    * You are using the `.append()` method to add the user's guess to the `guessed` list.

10. **Input and Output:**
    * You are using the `print()` function to display messages to the user 
    and the `input()` function to get input from the user.

11. **String Formatting (f-strings):**
    * You are using f-strings (e.g., `print(f"Your current lives is {lives}")`) 
    to embed variable values directly into strings for cleaner output.

12. **Membership Operators:**
    * You are using the `in` operator to check if the `user_choice` is present in the `choosen_word` or the `guessed` list.

13. **Boolean Variables:**
    * You are using the boolean variable `game_over` to control the main game loop.

In summary, your code demonstrates several fundamental Python programming techniques 
commonly used in creating interactive text-based games.

"""
