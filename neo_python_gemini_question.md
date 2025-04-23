Okay, here is a Python version of the problem set, maintaining the same themes and progression but using Python syntax and standard libraries, with variations in the specific examples.

**(Standard Imports often useful: `math`)**
_You may need to add `import <module_name>` at the top of your Python file._

---

**Problem 1: Introduction to Output and Simple Loops**

- **Objective:** Learn basic output and `for` loops.
- **Task:** Write Python code using a `for` loop to produce the following output:
  ```
  Python is fun!
  Python is fun!
  Python is fun!
  Python is fun!
  ```
- **Tips:** Use `print()` for output and a `for` loop with `range()` (e.g., `for i in range(4):`).

```python
for i in range(4):
    print("Python is fun!")
```

---

**Problem 2: Looping with Sequential Numbers**

- **Objective:** Use loops to generate number sequences.
- **Task:** Write Python code using a `for` loop to display numbers 10 down to 1, each on a new line.
  ```
  10
  9
  8
  7
  6
  5
  4
  3
  2
  1
  ```
- **Tips:** Use `range()` with three arguments: start, stop (exclusive), and step.

```python
listing = []
for i in range(1,11):
    listing.append(i)

inverted_list = listing[::-1]

for anjai in inverted_list:
    print(anjai)
```

---

**Problem 3: Introduction to Conditionals (`if`/`elif`/`else`) within a Loop**

- **Objective:** Combine loops and conditional statements.
- **Task:** Loop from -2 to 2 (inclusive). For each number, print whether it's "Positive", "Negative", or "Zero".
  ```
  Number -2 is Negative
  Number -1 is Negative
  Number 0 is Zero
  Number 1 is Positive
  Number 2 is Positive
  ```
- **Tips:** Use `if`/`elif`/`else` inside the loop. Use f-strings (e.g., `f"Number {i} is {status}"`) or string concatenation (`+`) for output.

```python
for i in range(-2,3):
    status = ""
    if i < 0:
        status = "Negative"
    elif i > 0:
        status = "Positive"
    else:
        status = "Zero"
    print(f"Number {i} is {status}")
```

---

**Problem 4: Using Modulo and Conditionals (Divisibility)**

- **Objective:** Use the modulo operator (`%`) for divisibility checks.
- **Task:** Loop from 0 to 10 (inclusive). For each number, print whether it is "divisible by 3" or "not divisible by 3".
  ```
  Number 0 is divisible by 3
  Number 1 is not divisible by 3
  Number 2 is not divisible by 3
  Number 3 is divisible by 3
  Number 4 is not divisible by 3
  Number 5 is not divisible by 3
  Number 6 is divisible by 3
  Number 7 is not divisible by 3
  Number 8 is not divisible by 3
  Number 9 is divisible by 3
  Number 10 is not divisible by 3
  ```
- **Tips:** The modulo operator in Python is `%`. Check if `i % 3 == 0`.

```python
for i in range(0,11):
    if i % 3 == 0:
        status = "divisible by 3"
    else:
        status = "not divisible by 3 "
    print(f"Number {i} is {status}")
```

---

**Problem 5: Controlling Loop Flow (`break`)**

- **Objective:** Learn how to exit a loop prematurely using `break`.
- **Task:** Loop from 1 up to 20 (inclusive). If the number is divisible by 7, print "Found a multiple of 7!" and immediately exit the loop. Otherwise, print "Checking [number]...".
  ```
  Checking 1...
  Checking 2...
  Checking 3...
  Checking 4...
  Checking 5...
  Checking 6...
  Found a multiple of 7!
  ```
- **Tips:** Use an `if` condition to check for divisibility (`i % 7 == 0`) and use `break` to exit the `for` loop.

```python
for i in range(1,21):
    if i % 7 == 0:
        print(f"Found a multiple of {i}")
        break
    else:
        print(f"Checking {i} . . . .")

```

---

**Problem 6: Nested Loops - Creating a Simple Pattern**

- **Objective:** Understand how nested loops work to create patterns.
- **Task:** Use nested `for` loops to generate an inverted right-angled triangle pattern of hashes (`#`).
  ```
  #####
  ####
  ###
  ##
  #
  ```
- **Tips:** The outer loop controls the rows. The inner loop controls the number of characters per row. You can repeat a character using the `*` operator (e.g., `"#" * count`).

```python
pagar = "#"

listing = []
for i in range(1,6):
    listing.append(i)

inverted_list = listing[::-1]

for j in inverted_list:
    print(j*pagar)
```

---

**Problem 7: Introduction to Functions**

- **Objective:** Define and call simple functions.
- **Task:** Create a Python function named `display_message` that accepts a message (string) as an argument and prints it to the console. Call this function with the messages "Learning Python Functions" and "Practice makes perfect!".
  ```
  Learning Python Functions
  Practice makes perfect!
  ```
- **Tips:** Define a function using `def display_message(message):`. Call it like `display_message("Your text")`.

```python
def display_message(x):
    print(x)

display_message("Learning Python Functions")
display_message("Practice makes perfect!")
```

---

**Problem 8: Functions with Return Values**

- **Objective:** Define functions that compute and return a value.
- **Task:** Create a Python function named `calculate_circle_area` that accepts the `radius` (float or int) as an argument and returns the area of the circle (float). Use `math.pi` for the value of Pi. Call the function with a radius of 5 and print the returned result.
  ```
  78.53981633974483  (or similar float value)
  ```
- **Tips:** Import the `math` module: `import math`. Define the function with a `return` statement: `return math.pi * radius * radius`.

```python
import math

def calculate_circle_area(radius):
    return math.pi * (radius**2)

print(round(calculate_circle_area(5),2))
```

---

**Problem 9: Introduction to Lists and Iteration**

- **Objective:** Create and iterate over lists.
- **Task:** Create a list named `colors` containing the strings "Red", "Green", "Blue", "Yellow". Then, iterate through the list and print each color name on a new line.
  ```
  Red
  Green
  Blue
  Yellow
  ```
- **Tips:** Initialize a list: `colors = ["Red", "Green", "Blue", "Yellow"]`. Iterate using `for color in colors:`.

```python
colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
    print(color)
```

---

**Problem 10: Functions Processing Lists**

- **Objective:** Write functions that take lists as input.
- **Task:** Create a Python function named `print_list_items` that accepts a list (`items`) and prints each element of the list on a new line, preceded by "Item: ". Test it by calling it with the `colors` list from Problem 9.
  ```
  Item: Red
  Item: Green
  Item: Blue
  Item: Yellow
  ```
- **Tips:** Define the function: `def print_list_items(items):`. Use a `for` loop inside.

```python
def print_list_items(daftar):
    for obj in daftar:
        print(f"Item: {obj}")

colors = ["Red", "Green", "Blue", "Yellow"]

print_list_items(colors)
```

---

**Problem 11: String Indexing and Slicing**

- **Objective:** Access individual characters and substrings within a string.
- **Task:** Given the string `text = "ProgrammingPython"`, print:
  1.  The first character.
  2.  The last character.
  3.  The substring "Python".
  ```
  P
  n
  Python
  ```
- **Tips:** Access characters using `text[index]` (0-based). Get length with `len(text)`. Access the last character with `text[-1]` or `text[len(text) - 1]`. Use slicing `text[start:end]` (exclusive end).

```python
text = "ProgrammingPython"

print(text[:1])
print(text[len(text)-1:len(text)])
print(text[len(text)-6:len(text)])
```

---

**Problem 12: Basic String Methods**

- **Objective:** Use common string manipulation methods.
- **Task:** Given the string `mixed_case = "pYtHoN ExAmPle"`, print:
  1.  The string converted to uppercase.
  2.  The string converted to lowercase.
  3.  Whether the string (case-insensitive) starts with "py". (Should print `True`).
  ```
  PYTHON EXAMPLE
  python example
  True
  ```
- **Tips:** Use `.upper()`, `.lower()`, and `.lower().startswith('py')`.

```python
mixed_case = "pYtHoN ExAmPle"

print(mixed_case.lower())
print(mixed_case.upper())
print(mixed_case.lower().startswith("py"))
```

---

**Problem 13: Looping Through String Characters**

- **Objective:** Iterate over the characters of a string.
- **Task:** Given the string `word = "PYTHON"`, print each character on a new line, separated by hyphens (`-`), like below (no hyphen after the last character).
  ```
  P-Y-T-H-O-N
  ```
- **Tips:** Use a `for` loop: `for char in word:`. You can build a list of characters and use `"-".join(list)` or manage printing with `end='-'` carefully.

```python
word = "PYTHON"

print("-".join(word))
```

---

**Problem 14: Accessing List Elements and Length**

- **Objective:** Get elements by index and find the size of a list.
- **Task:** Given the list `numbers = [10, 20, 30, 40, 50]`, print:
  1.  The second element (index 1).
  2.  The last element.
  3.  The total number of elements in the list.
  ```
  20
  50
  5
  ```
- **Tips:** Access elements using `numbers[index]` (0-based). Get the last element with `numbers[-1]`. Get the length with `len(numbers)`.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1])
print(numbers[len(numbers)-1])
print(len(numbers))
```

---

**Problem 15: Modifying Lists (`append`) and Checking Membership (`in`)**

- **Objective:** Add elements to lists and check if an element exists.
- **Task:** Create a list `languages` initialized with "Java", "C++". Append "Python" to the end of the list. Print the final list. 
Then, check if "Ruby" is in the list and print the boolean result. Finally, check if "Java" is in the list and print the boolean result.
  ```
  ['Java', 'C++', 'Python']
  False
  True
  ```
- **Tips:** Initialize with `languages = ["Java", "C++"]`. Add using `languages.append("Python")`. Check membership using the `in` operator: `"Ruby" in languages`.

```python
languages = ["Java", "C++"]

languages.append("Python")
print(languages)
print("Ruby" in languages)
print("Java" in languages)
```

---

**Problem 16: Introduction to `while` Loops**

- **Objective:** Use `while` loops for repetition based on a condition.
- **Task:** Use a `while` loop to print multiples of 5 starting from 5 up to and including 50.
  ```
  5
  10
  15
  20
  25
  30
  35
  40
  45
  50
  ```
- **Tips:** Initialize a counter variable (e.g., `num = 5`). Use `while num <= 50:`. Remember to increment the counter appropriately (`num += 5`) inside the loop.

```python
counter = 5

while counter <=50:
    print(counter)
    counter += 5
```

---

**Problem 17: `while` Loop with a Condition**

- **Objective:** Use `while` loops for iterative calculations until a condition is met.
- **Task:** Start with a variable `count = 100`. Use a `while` loop to repeatedly subtract 7 from `count` and 
print the _new_ value. Stop the loop _before_ the count becomes less than 50.
  ```
  93
  86
  79
  72
  65
  58
  51
  ```
- **Tips:** The loop condition could be `while count >= 50:`. Perform the subtraction _before_ checking the condition again, or check `count - 7 >= 50` within the loop. Print the value _after_ subtracting.

```python
angka_awal = 100

while angka_awal >=50:
    angka_awal -= 7
    print(angka_awal)
```

---

**Problem 18: Getting User Input**

- **Objective:** Read input from the user via the console.
- **Task:** Ask the user to enter their age and store it in a variable. Then, print a message like "You are [age] years old."
  ```
  Enter your age: 25
  You are 25 years old.
  ```
- **Tips:** Use `input("Enter your age: ")` to prompt and read the input. The result will be a string.

```python
age = (input("Enter your age: "))

print(f"You are {age} years old")
```

---

**Problem 19: Using `elif` for Multiple Conditions**

- **Objective:** Handle multiple exclusive conditions using `if`/`elif`/`else`.
- **Task:** Ask the user to enter a numerical score (0-100). Read the input, convert it to an integer, 
and then print the corresponding grade: "Grade A" (90-100), "Grade B" (80-89), "Grade C" (70-79), 
"Grade D" (below 70). Assume valid integer input between 0 and 100.
  ```
  Enter your score (0-100): 85
  Grade B
  Enter your score (0-100): 65
  Grade D
  ```
- **Tips:** Read input using `input()`. Convert to an integer using `int()`. Use `if score >= 90: ... elif score >= 80: ... elif score >= 70: ... else: ...`.

```python
try:
    score = int(input("Enter your score (0-100):"))
    if 90 <= score <= 100 :
        print("Grade A")
    elif 80 <= score <= 89 :
        print("Grade B")
    elif 70 <= score <= 79 :
        print("Grade C")
    elif 0 <= score < 70 :
        print("Grade D, gagal lo oon")
    else:
        print("Harus di atas 0 dong nilainya")


except:
    print("Error gan, try again, harus dari 0-100 dan harus integer")
```

---

**Problem 20: Controlling Loop Flow (`continue`)**

- **Objective:** Learn how to skip the current iteration of a loop using `continue`.
- **Task:** Loop through numbers from 1 to 15 (inclusive). 
Print only the numbers that are _not_ divisible by 3. Use the `continue` statement to skip the printing for multiples of 3.
  ```
  1
  2
  4
  5
  7
  8
  10
  11
  13
  14
  ```
- **Tips:** Inside the loop, use `if i % 3 == 0: continue`. The `print(i)` should come after this `if` statement.

```python
for i in range(1,16):
    if i % 3 == 0:
        continue
    print(i)
```

---

**Problem 21: Dictionaries - Creation and Access**

- **Objective:** Create and access key-value pairs using Dictionaries.
- **Task:** Create a dictionary named `capitals` to store the following key-value 
pairs: "USA" -> "Washington D.C.", "France" -> "Paris", "Japan" -> "Tokyo". Print the entire dictionary, 
then print the capital of "France", and finally print the capital of "Japan".
  ```
  {'USA': 'Washington D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}  (Order may vary in older Python versions)
  Paris
  Tokyo
  ```
- **Tips:** Initialize using `capitals = {"USA": "Washington D.C.", ...}`. Access values using `capitals["key"]`.

```python
capital_city = {
    "USA" : "Washington D.C.",
    "France" : "Paris",
    "Japan" : "Tokyo"
}

print(capital_city)
print(capital_city["France"])
print(capital_city["Japan"])

```

---

**Problem 22: Dictionaries - Iteration**

- **Objective:** Iterate over the keys, values, and key-value pairs of a dictionary.
- **Task:** Using the `capitals` dictionary from Problem 21, iterate and print:

  1.  All the keys (countries), each preceded by "Country: ".
  2.  All the values (capitals), each preceded by "Capital: ".
  3.  All key-value pairs in the format "Country: [country], Capital: [capital]".

  ```
  Countries:
  Country: USA
  Country: France
  Country: Japan
  (Order may vary in older Python versions)

  Capitals:
  Capital: Washington D.C.
  Capital: Paris
  Capital: Tokyo
  (Order may vary in older Python versions)

  Country-Capital Pairs:
  Country: USA, Capital: Washington D.C.
  Country: France, Capital: Paris
  Country: Japan, Capital: Tokyo
  (Order may vary in older Python versions)
  ```

- **Tips:** Use `for key in capitals:`, `for value in capitals.values():`, and `for key, value in capitals.items():`.

```python
capital_city = {
    "Country: USA" : "Capital: Washington D.C.",
    "Country: France" : "Capital: Paris",
    "Country: Japan" : "Capital: Tokyo"
}

print("Countries: ")
for key in capital_city.keys():
    print(key)
    
print("Capital: ")
for value in capital_city.values():
    print(value)
    
print("Countries capital pairs: ")
for key, value in capital_city.items():
    print(key, ",", value)

```

---

**Problem 23: Function Default Arguments**

- **Objective:** Define functions with optional parameters having default values.
- **Task:** Create a Python function named `greet` that takes two arguments: `name` (string) and `greeting` (string). 
The `greeting` parameter should have a default value of "Hello". The function should print the greeting followed by the name 
e.g., "Hello, Alice"). Call the function first with `name="Alice"` and `greeting="Hi"`, and then with just `name="Bob"` 
(using the default greeting).
  ```
  Hi, Alice
  Hello, Bob
  ```
- **Tips:** Define the function: `def greet(name, greeting="Hello"):`. Use f-strings or concatenation for printing.

```python

```

---

**Problem 24: Tuples (Immutable Sequences)**

- **Objective:** Use tuples for fixed-size, potentially heterogeneous, immutable sequences.
- **Task:** Create a tuple named `person` containing a name (string), age (int), and city (string): ("Alice", 30, "New York"). Print the tuple instance itself, and then print just the age (the element at index 1).
  ```
  ('Alice', 30, 'New York')
  30
  ```
- **Tips:** Create a tuple: `person = ("Alice", 30, "New York")`. Access elements using index: `person[1]`. Tuples are immutable after creation.

```python

```

---

**Problem 25: More List Methods (`insert`, `pop`, `remove`)**

- **Objective:** Modify lists by inserting and removing elements at specific positions or by value.
- **Task:** Start with a list `items = [10, 20, 40, 50]`.
  1.  Print the initial list.
  2.  Insert the number 30 at index 2. Print the list.
  3.  Remove the element at index 0. Print the list.
  4.  Remove the first occurrence of the value 40 from the list. Print the list.
  ```
  Initial list: [10, 20, 40, 50]
  After insert: [10, 20, 30, 40, 50]
  After remove index 0: [20, 30, 40, 50]
  After remove value 40: [20, 30, 50]
  ```
- **Tips:** Initialize: `items = [10, 20, 40, 50]`. Insert: `items.insert(2, 30)`. Remove by index: `items.pop(0)`. Remove by value: `items.remove(40)`.

```python

```

---

**Problem 26: Combining Input, Loop, List Building**

- **Objective:** Build a list dynamically based on user input within a loop.
- **Task:** Write a program that repeatedly asks the user to "Enter a favorite food (or 'stop' to finish):". If the user enters anything other than "stop" (case-insensitive), add it to a list of foods. If the user enters "stop", stop asking and print the final list of collected foods.
  ```
  Enter a favorite food (or 'stop' to finish): Pizza
  Enter a favorite food (or 'stop' to finish): Sushi
  Enter a favorite food (or 'stop' to finish): Tacos
  Enter a favorite food (or 'stop' to finish): STOP
  Final food list: ['Pizza', 'Sushi', 'Tacos']
  ```
- **Tips:** Use a `while True:` loop. Inside, read input using `input()`. Check if the input (converted to lowercase using `.lower()`) is equal to "stop". If it is, `break`. Otherwise, append the _original_ input string to your list (`foods = []`).

```python

```

---

**Problem 27: Function Returning a Modified List (Filtering)**

- **Objective:** Create functions that process a list and return a new, filtered list.
- **Task:** Create a Python function named `filter_positive_numbers` that takes a list of integers (`numbers`) as input. It should return a _new_ list containing only the positive numbers (> 0) from the input list. Test the function by calling it with the list `[1, -2, 3, 0, -5, 10]` and printing the result.
  ```
  [1, 3, 10]
  ```
- **Tips:** Define `def filter_positive_numbers(numbers):`. Inside, you can use a list comprehension: `return [num for num in numbers if num > 0]`. Alternatively, initialize an empty result list, loop through input `numbers`, and append positive numbers to the result list before returning it.

```python

```

---

**Problem 28: Checking Data Types**

- **Objective:** Determine the type of a variable at runtime.
- **Task:** Create variables of different types (e.g., an integer, a float, a string, a list, a dictionary, a tuple, a boolean). Use the built-in `type()` function to print the type of each variable.
  ```
  Type of var_int: <class 'int'>
  Type of var_float: <class 'float'>
  Type of var_str: <class 'str'>
  Type of var_list: <class 'list'>
  Type of var_dict: <class 'dict'>
  Type of var_tuple: <class 'tuple'>
  Type of var_bool: <class 'bool'>
  ```
- **Tips:** Define variables: `var_int = 100`, `var_float = 98.6`, `var_str = "Python"`, `var_list = [1, 2]`, `var_dict = {'a': 1}`, `var_tuple = (1, 2)`, `var_bool = False`. Print using `print(f"Type of var_int: {type(var_int)}")`.

```python

```

---

**Problem 29: Working with Dictionary Values**

- **Objective:** Perform calculations or operations on values stored within a dictionary.
- **Task:** Given the dictionary `product_prices = {"apple": 0.50, "banana": 0.25, "orange": 0.60, "milk": 3.50}`, write Python code to calculate and print the _total price_ of all items in the dictionary.
  ```
  Total price: 4.85
  ```
- **Tips:** Initialize the dictionary. Get the values using `product_prices.values()`. Calculate the sum using the built-in `sum()` function: `total = sum(product_prices.values())`. Print the total.

```python

```

---

**Problem 30: Putting It Together - Simple Data Processor**

- **Objective:** Combine functions, lists, classes (or dictionaries), and loops to process a small dataset.
- **Task:** You are given data representing books.
  1.  Define a simple class `Book` with attributes `title` (string) and `author` (string). Implement the `__init__` method to initialize these attributes.
  2.  Create a list named `library` containing several `Book` objects:
      - Book with title "The Hitchhiker's Guide to the Galaxy", author "Douglas Adams"
      - Book with title "Pride and Prejudice", author "Jane Austen"
      - Book with title "1984", author "George Orwell"
      - Book with title "Sense and Sensibility", author "Jane Austen"
  3.  Create a function `find_books_by_author(book_list, author_name)` that:
      - Accepts the list of `Book` objects and an author's name (string).
      - Finds all books in the list written by the given author.
      - Returns a _list_ containing the _titles_ of the books found. If no books are found, return an empty list.
  4.  Call the function with the `library` list and the author "Jane Austen", and print the resulting list of titles.
  ```
  ['Pride and Prejudice', 'Sense and Sensibility']
  ```
- **Tips:** Define the class: `class Book: def __init__(self, title, author): self.title = title; self.author = author`. Create the list: `library = [Book(...), Book(...)]`. In the function, initialize an empty list `found_titles = []`. Loop through the `book_list`. In each iteration, access `book.author`. If it matches `author_name`, append `book.title` to `found_titles`. Return `found_titles`.

```python

```
