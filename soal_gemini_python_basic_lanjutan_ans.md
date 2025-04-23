
---

**Problem 11: String Indexing and Slicing**

* **Objective:** Understand how to access individual characters and subsequences (slices) within a string.
* **Task:** Given the string `message = "Hello Python World"`, write Python code to:
    1.  Print the first character.
    2.  Print the last character.
    3.  Print the substring "Python".
* **Expected Output:**
    ```
    H
    d
    Python
    ```
* **Tips:** Remember that Python uses zero-based indexing (the first character is at index 0). Negative indices count from the end (`-1` is the last character). Slicing uses the syntax `[start:stop]` (the `stop` index is *exclusive*).

---

**Answer**


```python
message = "Hello Python World"

# 1. Print the first character
print(message[0])

# 2. Print the last character
print(message[-1])

# 3. Print the substring "Python"
# Index of 'P' is 6, index of 'n' is 11. We need index 12 for the stop.
print(message[6:12])
```

---

**Problem 12: Basic String Methods**

* **Objective:** Learn to use built-in string methods for common transformations.
* **Task:** Given the string `mixed_case = "PyThOn PrOgRaMmInG"`, write Python code to:
    1.  Print the string entirely in uppercase.
    2.  Print the string entirely in lowercase.
    3.  Find the starting index of the substring "PrOg".
* **Expected Output:**
    ```
    PYTHON PROGRAMMING
    python programming
    7
    ```
* **Tips:** Use the string methods `.upper()`, `.lower()`, and `.find()`. The `.find()` method returns the starting index of the first occurrence or `-1` if not found.

---

**Answer**


```python
mixed_case = "PyThOn PrOgRaMmInG"

# 1. Uppercase
print(mixed_case.upper())

# 2. Lowercase
print(mixed_case.lower())

# 3. Find substring index
print(mixed_case.find("PrOg"))
```

---

**Problem 13: Looping Through String Characters**

* **Objective:** Iterate over each character within a string using a loop.
* **Task:** Write Python code using a `for` loop to print each character of the string `word = "LOOP"` on a new line.
* **Expected Output:**
    ```
    L
    O
    O
    P
    ```
* **Tips:** Strings are sequence types, just like lists. You can iterate directly over their elements (characters) using a `for` loop.

---

**Answer**


```python
word = "LOOP"
for character in word:
    print(character)
```

---

**Problem 14: Accessing List Elements and Length**

* **Objective:** Retrieve specific elements from a list using their index and determine the list's size.
* **Task:** Given the list `colors = ["Red", "Green", "Blue", "Yellow", "Purple"]`, write Python code to:
    1.  Print the first color in the list.
    2.  Print the last color in the list.
    3.  Print the total number of colors in the list.
* **Expected Output:**
    ```
    Red
    Purple
    5
    ```
* **Tips:** Use index `[0]` for the first element, `[-1]` for the last element, and the `len()` function to get the total number of items.

---

**Answer**        


```python
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]

# 1. First color
print(colors[0])

# 2. Last color
print(colors[-1])

# 3. Total number of colors
print(len(colors))
```

---

**Problem 15: Modifying Lists (`append`) and Checking Membership (`in`)**

* **Objective:** Learn how to add items to the end of a list and how to check if an item exists within a list.
* **Task:**
    1.  Create a list named `planets` containing "Mercury", "Venus", "Earth".
    2.  Add "Mars" to the end of the `planets` list.
    3.  Print the updated list.
    4.  Check if "Jupiter" is in the `planets` list and print the result (True/False).
    5.  Check if "Earth" is in the `planets` list and print the result (True/False).
* **Expected Output:**
    ```
    ['Mercury', 'Venus', 'Earth', 'Mars']
    False
    True
    ```
* **Tips:** Use the `.append()` method to add an item to the end of a list. Use the `in` operator to check for membership, which returns a Boolean value.

---

**Answer**


```python
# 1. Create the list
planets = ["Mercury", "Venus", "Earth"]

# 2. Add "Mars"
planets.append("Mars")

# 3. Print the updated list
print(planets)

# 4. Check for "Jupiter"
print("Jupiter" in planets)

# 5. Check for "Earth"
print("Earth" in planets)
```

---

**Problem 16: Introduction to `while` Loops**

* **Objective:** Understand the basic structure and execution flow of a `while` loop.
* **Task:** Write Python code using a `while` loop to print the numbers 0, 1, 2, 3, 4, each on a new line.
* **Expected Output:**
    ```
    0
    1
    2
    3
    4
    ```
* **Tips:** A `while` loop continues executing as long as its condition remains `True`. You typically need:
    * An initialization step (e.g., `count = 0`).
    * A condition (`while count < 5:`).
    * An update step inside the loop (`count = count + 1` or `count += 1`) to eventually make the condition `False`.

---

**Answer**


```python
count = 0
while count < 5:
    print(count)
    count += 1 # Increment the counter
```

---

**Problem 17: `while` Loop with a Condition**

* **Objective:** Use a `while` loop based on a condition other than simple counting.
* **Task:** Write Python code that starts with `number = 1`. Use a `while` loop to repeatedly double the `number` and print it, stopping *before* the number exceeds 50.
* **Expected Output:**
    ```
    1
    2
    4
    8
    16
    32
    ```
* **Tips:** The loop condition should check if the `number` is less than or equal to a certain threshold (or simply less than the point where it would exceed 50 after doubling). Make sure to print the number *before* doubling it for the next potential iteration, or adjust the starting value and condition accordingly.

---

**Answer**


```python
number = 1
while number <= 50: # Condition to check before the next print/double
    print(number)
    number *= 2 # Double the number for the next iteration
```
*(Alternative Logic: Stop *when* doubling would exceed 50)*
```python
number = 1
while True: # Loop potentially forever
    print(number)
    if number * 2 > 50: # Check if the *next* value would be too large
        break # Exit loop
    number *= 2 # Double only if the next value is okay
```
*(Note: The first answer is generally simpler for this specific requirement)*

---

**Problem 18: Getting User Input**

* **Objective:** Learn how to prompt the user for input and use that input in the program.
* **Task:** Write Python code that:
    1.  Asks the user for their name using the prompt "Enter your name: ".
    2.  Stores the input in a variable.
    3.  Prints a personalized greeting, e.g., "Hello, [User's Name]!".
* **Example Interaction:**
    ```
    Enter your name: Alice
    Hello, Alice!
    ```
* **Tips:** Use the `input()` function. Remember that `input()` always returns the user's input as a *string*. Use f-strings for easy formatting.

---

**Answer**


```python
# 1. Ask for name and store it
user_name = input("Enter your name: ")

# 3. Print the greeting
print(f"Hello, {user_name}!")
```

---

**Problem 19: Using `elif` for Multiple Conditions**

* **Objective:** Handle scenarios with more than two possible outcomes using `if...elif...else`.
* **Task:** Write Python code that:
    1.  Asks the user to enter an integer number.
    2.  Converts the input string to an integer.
    3.  Prints "Positive" if the number is greater than 0.
    4.  Prints "Negative" if the number is less than 0.
    5.  Prints "Zero" if the number is exactly 0.
* **Example Interactions:**
    ```
    Enter an integer: 10
    Positive
    ```
    ```
    Enter an integer: -5
    Negative
    ```
    ```
    Enter an integer: 0
    Zero
    ```
* **Tips:** Use `int()` to convert the string from `input()` to an integer. Structure your conditions using `if`, `elif` (else if), and `else`.

---

**Answer**


```python
# 1. Ask for input
user_input = input("Enter an integer: ")

# 2. Convert to integer
try:
    number = int(user_input)

    # 3, 4, 5. Check the number and print the result
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input. Please enter an integer.") # Basic error handling

```

---

**Problem 20: Controlling Loop Flow (`continue`)**

* **Objective:** Understand how to use the `continue` statement to skip the rest of the current loop iteration and proceed to the next one.
* **Task:** Write Python code using a `for` loop to iterate through numbers from 1 to 10. Print only the *odd* numbers. Use the `continue` statement to skip printing the even numbers.
* **Expected Output:**
    ```
    1
    3
    5
    7
    9
    ```
* **Tips:** Inside the loop, check if the number is even (`number % 2 == 0`). If it is, use `continue` to skip the `print()` statement for that iteration.

---

**Answer**


```python
for number in range(1, 11): # range(1, 11) gives numbers 1 through 10
    if number % 2 == 0: # Check if the number is even
        continue # Skip the rest of this iteration if it's even
    print(number) # This line only runs if continue was not executed (i.e., for odd numbers)
```

---

**Problem 21: Dictionaries - Creation and Access**

* **Objective:** Understand how to create dictionaries (key-value pairs) and access values using their keys.
* **Task:**
    1.  Create a dictionary named `student_info` where the keys are "name", "major", "id" and the values are "Budi", "Computer Science", 12345 respectively.
    2.  Print the student's name using the dictionary.
    3.  Print the student's ID using the dictionary.
* **Expected Output:**
    ```
    Budi
    12345
    ```
* **Tips:** Dictionaries are created using curly braces `{}` with `key: value` pairs separated by commas. Access values using square brackets `[]` with the key inside (e.g., `dictionary[key]`).

---

**Answer**


```python
# 1. Create the dictionary
student_info = {
    "name": "Budi",
    "major": "Computer Science",
    "id": 12345
}

# 2. Print the name
print(student_info["name"])

# 3. Print the ID
print(student_info["id"])
```

---

**Problem 22: Dictionaries - Iteration**

* **Objective:** Learn how to loop through the keys, values, or key-value pairs of a dictionary.
* **Task:** Using the `student_info` dictionary from Problem 21, write Python code to:
    1.  Print each key on a new line.
    2.  Print each value on a new line.
    3.  Print each key-value pair in the format "Key: Value" on a new line.
* **Expected Output (order might vary slightly):**
    ```
    Keys:
    name
    major
    id

    Values:
    Budi
    Computer Science
    12345

    Key-Value Pairs:
    name: Budi
    major: Computer Science
    id: 12345
    ```
* **Tips:**
    * Iterating directly over a dictionary (`for k in my_dict:`) loops through its keys.
    * Use `.values()` to get an iterable of values (`for v in my_dict.values():`).
    * Use `.items()` to get an iterable of key-value tuples (`for k, v in my_dict.items():`).

---

**Answer**


```python
student_info = {
    "name": "Budi",
    "major": "Computer Science",
    "id": 12345
}

# 1. Print keys
print("Keys:")
for key in student_info:
    print(key)

print("\nValues:")
# 2. Print values
for value in student_info.values():
    print(value)

print("\nKey-Value Pairs:")
# 3. Print key-value pairs
for key, value in student_info.items():
    print(f"{key}: {value}")
```

---

**Problem 23: Function Default Arguments**

* **Objective:** Understand how to define functions with parameters that have default values if no argument is provided during the function call.
* **Task:** Create a function `power(base, exponent=2)` that calculates `base` raised to the power of `exponent`. The `exponent` should default to 2 if not provided.
    * Call the function with `power(5, 3)` and print the result.
    * Call the function with `power(7)` (using the default exponent) and print the result.
* **Expected Output:**
    ```
    125
    49
    ```
* **Tips:** Define the default value in the function signature using `=`. The exponentiation operator in Python is `**`.

---

**Answer**


```python
def power(base, exponent=2):
  """Calculates base raised to the power of exponent."""
  return base ** exponent

# Call with both arguments
result1 = power(5, 3)
print(result1)

# Call with only the base (using default exponent)
result2 = power(7)
print(result2)
```

---

**Problem 24: Tuples - Basics**

* **Objective:** Understand tuples as ordered, *immutable* sequences.
* **Task:**
    1.  Create a tuple named `point` representing (x, y) coordinates `(10, 20)`.
    2.  Print the tuple.
    3.  Print the first element (x-coordinate).
    4.  Try to change the first element to `15` (this should cause an error, demonstrating immutability). Comment out the line that causes the error after observing it.
* **Expected Output (without the error line):**
    ```
    (10, 20)
    10
    ```
* **Tips:** Tuples are created using parentheses `()`. Access elements using index `[]` like lists. Immutability means you cannot change elements after creation.

---

**Answer**


```python
# 1. Create the tuple
point = (10, 20)

# 2. Print the tuple
print(point)

# 3. Print the first element
print(point[0])

# 4. Try to change the element (causes TypeError)
# point[0] = 15 # Uncomment this line to see the TypeError
# print(point)  # This line would not be reached if the error occurs

print("\nAttempting to modify a tuple raises a TypeError because tuples are immutable.")
```

---

**Problem 25: More List Methods (`insert`, `pop`, `remove`)**

* **Objective:** Learn additional ways to modify lists: inserting at specific positions, removing by index, and removing by value.
* **Task:**
    1.  Start with the list `letters = ['a', 'b', 'd', 'e']`.
    2.  Insert the letter 'c' at the correct position (index 2). Print the list.
    3.  Remove the last element ('e') using its index. Print the list.
    4.  Remove the element 'a' by its value. Print the list.
* **Expected Output:**
    ```
    ['a', 'b', 'c', 'd', 'e']
    ['a', 'b', 'c', 'd']
    ['b', 'c', 'd']
    ```
* **Tips:**
    * `.insert(index, value)` inserts `value` *before* the given `index`.
    * `.pop(index)` removes and returns the item at `index`. If no index is specified, `.pop()` removes and returns the *last* item.
    * `.remove(value)` removes the *first* occurrence of the specified `value`.

---

**Answer**


```python
# 1. Start with the list
letters = ['a', 'b', 'd', 'e']
print(f"Initial list: {letters}")

# 2. Insert 'c' at index 2
letters.insert(2, 'c')
print(f"After insert: {letters}")

# 3. Remove the last element (index -1 or len(letters)-1)
removed_element = letters.pop() # Removes and returns the last element
# Alternatively: letters.pop(len(letters) - 1) or letters.pop(4) in this specific case
print(f"After pop: {letters} (Removed '{removed_element}')")

# 4. Remove 'a' by value
letters.remove('a')
print(f"After remove 'a': {letters}")
```

---

**Problem 26: Combining Input, Loop, List**

* **Objective:** Integrate getting user input within a loop to populate a list dynamically.
* **Task:** Write Python code that repeatedly asks the user to "Enter a number (or 'done' to finish): ".
    * If the user enters a number, convert it to an integer and add it to a list called `numbers`.
    * If the user enters "done" (case-insensitive), stop asking and print the final list of numbers.
* **Example Interaction:**
    ```
    Enter a number (or 'done' to finish): 10
    Enter a number (or 'done' to finish): 25
    Enter a number (or 'done' to finish): 8
    Enter a number (or 'done' to finish): DoNe
    Final list: [10, 25, 8]
    ```
* **Tips:** Use an infinite `while True:` loop combined with a `break` statement. Use `.lower()` or `.upper()` to handle case-insensitive input for "done". Use `try-except` block to handle cases where the user enters something that's not a number or "done".

---

**Answer**


```python
numbers = []
while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == 'done':
        break # Exit the loop if user types 'done'

    try:
        # Try converting the input to an integer
        num = int(user_input)
        numbers.append(num) # Add the number to the list
    except ValueError:
        # Handle cases where input is not a valid number (and not 'done')
        print("Invalid input. Please enter an integer or 'done'.")

print(f"Final list: {numbers}")
```

---

**Problem 27: Function Returning a Modified List**

* **Objective:** Create a function that takes a list, processes it, and returns a *new* list based on some criteria.
* **Task:** Create a function `get_even_numbers(input_list)` that:
    1.  Accepts a list of integers (`input_list`).
    2.  Creates a *new* empty list called `even_numbers`.
    3.  Iterates through `input_list`. If a number is even, add it to the `even_numbers` list.
    4.  Returns the `even_numbers` list.
    * Test the function with `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and print the result.
* **Expected Output:**
    ```
    [2, 4, 6, 8, 10]
    ```
* **Tips:** This practices creating a function, list iteration, conditional logic (`% 2 == 0`), appending to a new list, and returning a value (the new list). Avoid modifying the original list directly unless intended.

---

**Answer**


```python
def get_even_numbers(input_list):
  """
  Filters a list of integers and returns a new list containing only the even numbers.
  """
  even_numbers = [] # 2. Create a new list
  for number in input_list: # 3. Iterate through the input list
    if number % 2 == 0: # Check if the number is even
      even_numbers.append(number) # Add even number to the new list
  return even_numbers # 4. Return the new list

# Test the function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_even_numbers(my_list)
print(result)
```
*(Self-correction: Added docstring to the function)*

---

**Problem 28: Checking Data Types**

* **Objective:** Learn how to determine the data type of a variable.
* **Task:** Given the following variables:
    ```python
    a = 10
    b = 3.14
    c = "Hello"
    d = [1, 2, 3]
    e = {"key": "value"}
    f = (1, 2)
    g = True
    ```
    Write Python code to print the data type of each variable using the `type()` function.
* **Expected Output (exact formatting might vary slightly):**
    ```
    Type of a: <class 'int'>
    Type of b: <class 'float'>
    Type of c: <class 'str'>
    Type of d: <class 'list'>
    Type of e: <class 'dict'>
    Type of f: <class 'tuple'>
    Type of g: <class 'bool'>
    ```
* **Tips:** The `type()` function directly returns the type object of its argument. Use f-strings or `print()` with multiple arguments for clear output.

---

**Answer**


```python
a = 10
b = 3.14
c = "Hello"
d = [1, 2, 3]
e = {"key": "value"}
f = (1, 2)
g = True

print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")
print(f"Type of c: {type(c)}")
print(f"Type of d: {type(d)}")
print(f"Type of e: {type(e)}")
print(f"Type of f: {type(f)}")
print(f"Type of g: {type(g)}")
```

---

**Problem 29: Working with Dictionary Values**

* **Objective:** Perform calculations or operations on values stored within a dictionary.
* **Task:** Given the dictionary `scores = {"Math": 85, "Science": 92, "History": 78, "English": 88}`, write Python code to calculate and print the *average* score.
* **Expected Output (or close due to float precision):**
    ```
    Average score: 85.75
    ```
* **Tips:**
    1.  Get all the values from the dictionary using `.values()`.
    2.  Calculate the sum of these values (you can use the `sum()` function).
    3.  Calculate the number of values (you can use `len()` on the dictionary or the values view).
    4.  Divide the sum by the count to get the average.

---

**Answer**


```python
scores = {"Math": 85, "Science": 92, "History": 78, "English": 88}

# 1. Get the values
score_values = scores.values()

# 2. Calculate the sum
total_score = sum(score_values)

# 3. Get the count
num_scores = len(score_values) # or len(scores)

# 4. Calculate the average
if num_scores > 0: # Avoid division by zero if the dictionary is empty
  average_score = total_score / num_scores
  print(f"Average score: {average_score}")
else:
  print("Cannot calculate average of empty scores.")

```
*(Self-correction: Added check for empty dictionary to prevent division by zero)*

---

**Problem 30: Putting It Together - Simple Data Processor**

* **Objective:** Combine functions, lists, dictionaries, and loops to process a small dataset.
* **Task:** You are given a list of dictionaries, where each dictionary represents a product with its name and price:
    ```python
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 75},
        {"name": "Monitor", "price": 300}
    ]
    ```
    Create a function `find_most_expensive_product(product_list)` that:
    1.  Accepts the list of product dictionaries.
    2.  Finds the product with the highest price.
    3.  Returns the *name* of the most expensive product.
    * Call the function with the `products` list and print the result.
* **Expected Output:**
    ```
    The most expensive product is: Laptop
    ```
* **Tips:**
    * Initialize variables to keep track of the highest price found so far (e.g., `max_price = -1` or price of the first item) and the name of that product (`most_expensive_name = ""`).
    * Loop through the `product_list`. In each iteration, access the price from the current product dictionary.
    * Compare the current product's price with `max_price`. If it's higher, update `max_price` and `most_expensive_name`.
    * Return the `most_expensive_name` after the loop finishes. Handle the case of an empty input list if necessary.

---

**Answer**


```python
def find_most_expensive_product(product_list):
  """
  Finds the name of the product with the highest price in a list of product dictionaries.
  """
  if not product_list: # Handle empty list case
    return None # Or raise an error, or return a specific message

  max_price = -1 # Initialize with a value lower than any possible price
  most_expensive_name = ""

  for product in product_list:
    current_price = product["price"] # Access the price
    if current_price > max_price:
      max_price = current_price # Update max price found
      most_expensive_name = product["name"] # Update the name

  return most_expensive_name

# The list of products
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300}
]

# Call the function and print the result
expensive_product_name = find_most_expensive_product(products)

if expensive_product_name:
  print(f"The most expensive product is: {expensive_product_name}")
else:
  print("The product list is empty.")
```
*(Self-correction: Added handling for an empty input list and improved initialization of max_price)*

---

This set of 30 problems covers a significant portion of Python's fundamental syntax and data structures, providing a good base for learners.
