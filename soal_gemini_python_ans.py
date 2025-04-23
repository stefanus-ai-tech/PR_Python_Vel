Okay, here is the JavaScript exercise series converted into a Python questionnaire format. I've translated the concepts, syntax, and standard practices to their Python equivalents.

---

**Python Basic Training Series - Building the Foundation**

The goal of this training is to familiarize you with basic Python syntax, loops (`for`, `while`), conditionals (`if/elif/else`), functions, and basic data manipulation like strings and lists. Please work through these problems sequentially.

---

**Problem 1: Introduction to Output and Simple Loops**

*   **Objective:** Understand how to display output and create the most basic loops.
*   **Task:** Write Python code using a `for` loop to produce the following output in the console:
    ```
    Hello Python!
    Hello Python!
    Hello Python!
    Hello Python!
    Hello Python!
    ```
*   **Tips:** Use the `print()` function to display text. Use the `range()` function in your `for` loop to determine how many times the loop needs to run.

---

**Answer**

```python
# Your code here
for _ in range(5):
    print("Hello Python!")

```

---

**Problem 2: Looping with Sequential Numbers**

*   **Objective:** Understand how to use a counter variable within a loop.
*   **Task:** Write Python code using a `for` loop to display numbers 1 through 5 in the console, each on a new line:
    ```
    1
    2
    3
    4
    5
    ```
*   **Tips:** Pay attention to the start value, stop value (exclusive), and step in the `range()` function used with the `for` loop.

---

**Answer**

```python
# Your code here
for i in range(1, 6):
    print(i)

```

---

**Problem 3: Introduction to Conditionals (if/else) within a Loop**

*   **Objective:** Combine loops with simple conditional logic.
*   **Task:** Write Python code using a `for` loop that iterates through numbers from 1 to 5. For each number, print whether the number is "Small" (if less than or equal to 3) or "Large" (if greater than 3). The expected output is:
    ```
    Number 1 is Small
    Number 2 is Small
    Number 3 is Small
    Number 4 is Large
    Number 5 is Large
    ```
*   **Tips:** Use an `if...else` statement inside the `loop` to check the value of the number in each iteration. Use f-strings (e.g., `f"Number {variable} is ..."`) to create the output string easily.

---

**Answer**

```python
# Your code here
for number in range(1, 6):
    if number <= 3:
        category = "Small"
    else:
        category = "Large"
    print(f"Number {number} is {category}")

```

---

**Problem 4: Using Modulo and Conditionals (Even/Odd)**

*   **Objective:** Introduce the modulo operator (`%`) for common logic like checking for even/odd numbers.
*   **Task:** Write Python code using a `for` loop for numbers from 0 to 5. For each number, determine and print whether the number is even or odd. The expected output is:
    ```
    Number 0 is even
    Number 1 is odd
    Number 2 is even
    Number 3 is odd
    Number 4 is even
    Number 5 is odd
    ```
*   **Tips:** Remember, an even number is a number that is perfectly divisible by 2 (the remainder of the division is 0). Use the modulo operator (`%`).

---

**Answer**

```python
# Your code here
for number in range(6):
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"Number {number} is {parity}")

```

---

**Problem 5: Controlling Loop Flow (break)**

*   **Objective:** Understand how to stop a loop prematurely using `break`.
*   **Task:** Write Python code using a `for` loop for numbers from 0 to 9. Check each number. If the number is odd, print a message that the program is stopping and exit the loop. If it's even, print that the number is even. The expected output is:
    ```
    Number 0 is even
    Number 1 is odd, stopping the program.
    ```
*   **Tips:** Use an `if` statement to check the odd condition (`number % 2 != 0`). If true, print the message and use the `break` statement to exit the loop. Place the check for even numbers such that it only runs if the `break` condition wasn't met (or use an `else` block with the `if`).

---

**Answer**

```python
# Your code here
for number in range(10):
    if number % 2 != 0:
        print(f"Number {number} is odd, stopping the program.")
        break
    else:
        print(f"Number {number} is even")

```

---

**Problem 6: Nested Loops - Creating a Simple Pattern**

*   **Objective:** Understand how loops inside loops work to create more complex structures like patterns or grids.
*   **Task:** Write Python code using *nested loops* (a loop inside another loop) to generate a right-angled triangle pattern of stars like this:
    ```
    *
    **
    ***
    ****
    *****
    ```
*   **Tips:** The outer loop will control the number of rows. The inner loop will control the number of stars printed per row. Use `print()` with the `end=''` argument in the inner loop to print stars on the same line, and a `print()` with no arguments after the inner loop finishes to move to the next line. Alternatively, Python's string multiplication (`'*' * count`) can simplify this.

---

**Answer**

```python
# Your code here (Method 1: Nested Loops)
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print() # Move to the next line

# Your code here (Method 2: String Multiplication)
# for i in range(1, 6):
#    print("*" * i)

```

---

**Problem 7: Introduction to Functions**

*   **Objective:** Understand how to create and call simple functions to perform specific tasks.
*   **Task:** Create a Python *function* named `greet_user` that accepts one argument (parameter) called `name` (a string). This function should print a greeting message to the console.
    Example calls and output:
    ```python
    greet_user("Budi") # Output: Hello, Budi! Welcome!
    greet_user("Ani")  # Output: Hello, Ani! Welcome!
    ```
*   **Tips:** Use the `def` keyword to define a function. Use the parameter within the function body. Call the function by its name, providing the required argument.

---

**Answer**

```python
# Your code here
def greet_user(name):
    print(f"Hello, {name}! Welcome!")

# Example calls:
greet_user("Budi")
greet_user("Ani")

```

---

**Problem 8: Functions with Return Values**

*   **Objective:** Understand functions that not only perform actions but also return a value resulting from calculation or processing.
*   **Task:** Create a Python function named `calculate_rectangle_area` that accepts two arguments: `length` and `width`. This function must *return* the calculated area.
    Example calls and usage:
    ```python
    plot_length = 10
    plot_width = 5
    plot_area = calculate_rectangle_area(plot_length, plot_width)
    print(f"The area of the plot is: {plot_area}") # Output: The area of the plot is: 50

    print(calculate_rectangle_area(8, 3)) # Output: 24
    ```
*   **Tips:** Use the `return` keyword inside the function to send the result back to the code that called it.

---

**Answer**

```python
# Your code here
def calculate_rectangle_area(length, width):
    return length * width

# Example calls:
plot_length = 10
plot_width = 5
plot_area = calculate_rectangle_area(plot_length, plot_width)
print(f"The area of the plot is: {plot_area}")

print(calculate_rectangle_area(8, 3))

```

---

**Problem 9: Introduction to Lists and List Iteration**

*   **Objective:** Understand how to create lists (ordered collections of items) and how to access each element within them using loops.
*   **Task:**
    1.  Create a list named `fruit_list` containing the following fruit names: "Apple", "Orange", "Mango", "Banana".
    2.  Use a `for` loop to print each fruit name from the list to the console, one per line.
    Expected output:
    ```
    Apple
    Orange
    Mango
    Banana
    ```
*   **Tips:** Lists in Python are created using square brackets `[]`. You can iterate directly over the elements of a list using a `for` loop (e.g., `for fruit in fruit_list:`).

---

**Answer**

```python
# Your code here
fruit_list = ["Apple", "Orange", "Mango", "Banana"]

for fruit in fruit_list:
    print(fruit)

```

---

**Problem 10: Functions Processing Lists**

*   **Objective:** Combine functions and lists. Create a function that accepts a list as input and performs an action on it.
*   **Task:** Create a function named `print_all_elements` that accepts one argument, a `list_data`. This function should print all elements in the given list to the console, just like in Problem 9.
    Example calls:
    ```python
    numbers = [10, 20, 30]
    names = ["Adi", "Bima", "Citra"]

    print_all_elements(numbers)
    # Output:
    # 10
    # 20
    # 30

    print_all_elements(names)
    # Output:
    # Adi
    # Bima
    # Citra
    ```
*   **Tips:** This combines concepts from Problem 7 (functions) and Problem 9 (list iteration).

---

**Answer**

```python
# Your code here
def print_all_elements(list_data):
    for element in list_data:
        print(element)

# Example calls:
numbers = [10, 20, 30]
names = ["Adi", "Bima", "Citra"]

print("--- Numbers ---")
print_all_elements(numbers)
print("\n--- Names ---")
print_all_elements(names)

```

---

**Best Practices to Remember (Python):**

1.  **Clear Variable and Function Names:** Use descriptive names (e.g., `calculate_area` is better than `ca`, `user_name` is better than `un`). Use `snake_case` for variables and functions (words separated by underscores). Use `PascalCase` (or `CapWords`) for class names. (PEP 8 Style Guide).
2.  **Comments:** Add comments (`#` for single-line) to explain non-obvious parts of your code or the purpose of functions/classes. Use docstrings (`"""Docstring goes here"""`) to document functions, classes, and modules.
3.  **Code Consistency:** Maintain a consistent coding style (e.g., indentation using 4 spaces, placement of operators, blank lines). Tools like `black` or `flake8` can help enforce this.
4.  **Functions Should Do One Thing:** Aim for functions that have a single, clear responsibility.
5.  **Readability Counts:** Write code that is easy for others (and your future self) to read and understand. Python emphasizes readability.
6.  **Use List Comprehensions:** Often provide a more concise and readable way to create lists based on existing iterables compared to traditional loops with `.append()`.
7.  **Avoid Modifying Lists While Iterating (Carefully):** Modifying a list while iterating over it can lead to unexpected behavior. Often it's better to create a new list or iterate over a copy.

---

---

**Python Intermediate to Advanced Training Series - Software Developer Preparation**

The goal of this training is to deepen understanding of advanced Python concepts, data structures, common design patterns, handling asynchronous operations (where applicable), and writing clean, modular, and efficient code.

---

**Problem 11: Advanced List/Iterable Processing (Comprehensions, map, filter, reduce)**

*   **Objective:** Master list comprehensions and functional tools like `map`, `filter`, and `functools.reduce` for efficient and declarative data processing.
*   **Task:** Given a list of dictionaries representing a product catalog:
    ```python
    products = [
      {"id": 1, "name": "Gaming Laptop", "category": "Electronics", "price": 15000000, "stock": 5},
      {"id": 2, "name": "Mechanical Keyboard", "category": "Computer Accessories", "price": 1200000, "stock": 15},
      {"id": 3, "name": "Ultrawide Monitor", "category": "Electronics", "price": 8500000, "stock": 3},
      {"id": 4, "name": "Wireless Mouse", "category": "Computer Accessories", "price": 350000, "stock": 25},
      {"id": 5, "name": "Flagship Smartphone", "category": "Electronics", "price": 12000000, "stock": 8},
    ]
    ```
    Create a function `analyze_products(product_data)` that:
    1.  Uses a list comprehension or `filter` to get products in the "Electronics" category.
    2.  Uses a list comprehension or `map` on the filtered result to create a new list containing only the name and price of these electronic products (as dictionaries).
    3.  Uses `sum()` with a generator expression (or `functools.reduce`) on the filtered electronic products (from step 1) to calculate the total inventory value (price * stock) of all electronic products.
    4.  The function should return a dictionary containing:
        *   `electronic_names_prices`: The list generated in step 2.
        *   `total_electronic_value`: The number calculated in step 3.
*   **Example Output (based on the data above):**
    ```python
    {
      "electronic_names_prices": [
        {"name": "Gaming Laptop", "price": 15000000},
        {"name": "Ultrawide Monitor", "price": 8500000},
        {"name": "Flagship Smartphone", "price": 12000000}
      ],
      "total_electronic_value": 197500000 # (15M*5) + (8.5M*3) + (12M*8)
    }
    ```
*   **Tips:** List comprehensions are often the most Pythonic way for steps 1 and 2. `sum()` is usually preferred over `reduce` for simple summation. Remember to import `reduce` from `functools` if you choose to use it.

---

**Answer**

```python
# Your code here
import functools # Needed only if using reduce

products = [
  {"id": 1, "name": "Gaming Laptop", "category": "Electronics", "price": 15000000, "stock": 5},
  {"id": 2, "name": "Mechanical Keyboard", "category": "Computer Accessories", "price": 1200000, "stock": 15},
  {"id": 3, "name": "Ultrawide Monitor", "category": "Electronics", "price": 8500000, "stock": 3},
  {"id": 4, "name": "Wireless Mouse", "category": "Computer Accessories", "price": 350000, "stock": 25},
  {"id": 5, "name": "Flagship Smartphone", "category": "Electronics", "price": 12000000, "stock": 8},
]

def analyze_products(product_data):
    # 1. Filter Electronics using list comprehension
    electronics = [p for p in product_data if p["category"] == "Electronics"]

    # 2. Map to name and price using list comprehension
    names_prices = [{"name": p["name"], "price": p["price"]} for p in electronics]

    # 3. Calculate total value using sum() and generator expression
    total_value = sum(p["price"] * p["stock"] for p in electronics)

    # Alternative for step 3 using functools.reduce
    # total_value = functools.reduce(lambda acc, p: acc + (p["price"] * p["stock"]), electronics, 0)

    # 4. Return results
    return {
        "electronic_names_prices": names_prices,
        "total_electronic_value": total_value
    }

# Example call
analysis_result = analyze_products(products)
print(analysis_result)

# Pretty print for better readability (optional)
# import json
# print(json.dumps(analysis_result, indent=2))

```

---

**Problem 12: Working with Complex Dictionaries and Unpacking**

*   **Objective:** Understand how to access and manipulate properties within nested dictionaries and use assignment/unpacking techniques for cleaner code.
*   **Task:** Given the following configuration dictionary:
    ```python
    app_config = {
      "appName": "Super App",
      "version": "1.2.0",
      "settings": {
        "theme": "dark",
        "language": "id",
        "notifications": {
          "email": True,
          "push": False,
          "soundLevel": 8
        }
      },
      "activeUser": {
        "id": "usr001",
        "name": "Citra Kirana",
        "preferences": {
          "ads": False,
          "newsletter": True
        }
      }
    }
    ```
    Create a function `get_user_and_notif_info(config)` that accepts the configuration dictionary. This function should use dictionary access (and potentially tuple unpacking if extracting multiple items) to extract the following information and return it in a descriptive f-string:
    "User '[User Name]' (ID: [User ID]) uses theme '[Theme]' with email notifications [active/inactive] and push notifications [active/inactive]."
*   **Example Output (based on the data above):**
    ```
    "User 'Citra Kirana' (ID: usr001) uses theme 'dark' with email notifications active and push notifications inactive."
    ```
*   **Tips:** Access nested dictionary values using multiple square brackets (e.g., `config['settings']['theme']`). Use Python's conditional expression (`value_if_true if condition else value_if_false`) to convert the boolean `True`/`False` values for notifications into "active"/"inactive" strings.

---

**Answer**

```python
# Your code here
app_config = {
  "appName": "Super App",
  "version": "1.2.0",
  "settings": {
    "theme": "dark",
    "language": "id",
    "notifications": {
      "email": True,
      "push": False,
      "soundLevel": 8
    }
  },
  "activeUser": {
    "id": "usr001",
    "name": "Citra Kirana",
    "preferences": {
      "ads": False,
      "newsletter": True
    }
  }
}

def get_user_and_notif_info(config):
    user_name = config['activeUser']['name']
    user_id = config['activeUser']['id']
    theme = config['settings']['theme']
    email_notif_status = "active" if config['settings']['notifications']['email'] else "inactive"
    push_notif_status = "active" if config['settings']['notifications']['push'] else "inactive"

    return (f"User '{user_name}' (ID: {user_id}) uses theme '{theme}' "
            f"with email notifications {email_notif_status} and "
            f"push notifications {push_notif_status}.")


# Example call
info_string = get_user_and_notif_info(app_config)
print(info_string)

```

---

**Problem 13: Asynchronous Programming with `asyncio` (Conceptual Simulation)**

*   **Objective:** Understand the basic concepts of asynchronous operations and how to handle them using Python's `asyncio` library (simulating delay).
*   **Task:** Create an *async* function `fetch_user_data(user_id)` that *simulates* fetching user data from an API.
    1.  The function must be defined using `async def`.
    2.  Inside the function, use `await asyncio.sleep(1)` to simulate a 1-second network delay.
    3.  After the delay:
        *   If `user_id` is a positive integer, return a dictionary representing the user (e.g., `{"id": user_id, "name": f"User {user_id}"}`).
        *   If `user_id` is not a positive integer (e.g., 0, negative, or another type), raise a `ValueError` with the message "Invalid User ID".
    4.  Write code *outside* the function to run this async function using `asyncio.run()`. Call `fetch_user_data` with a valid ID (e.g., 123) and use a `try...except ValueError` block to print the user data if successful or the error message if it fails.
    5.  Call it again with an invalid ID (e.g., -5) and handle the result similarly.
*   **Tips:** Remember to `import asyncio`. Use `async def` for the function and `await` for `asyncio.sleep`. Use a standard `try...except` block to handle the potential `ValueError` when calling the function via `asyncio.run()`.

---

**Answer**

```python
# Your code here
import asyncio
import time # Only needed for the second call example delay

async def fetch_user_data(user_id):
    """Simulates fetching user data asynchronously."""
    print(f"Fetching data for user {user_id}...")
    await asyncio.sleep(1) # Simulate network delay
    if isinstance(user_id, int) and user_id > 0:
        print(f"Data received for user {user_id}.")
        return {"id": user_id, "name": f"User {user_id}"}
    else:
        raise ValueError("Invalid User ID")

async def main():
    # --- Call with valid ID ---
    print("--- Attempt 1: Valid ID (123) ---")
    try:
        user_data = await fetch_user_data(123)
        print("Success:", user_data)
    except ValueError as e:
        print("Error:", e)

    print("\nWaiting a bit before next call...\n")
    # time.sleep(2) # Optional delay between calls for clarity in output

    # --- Call with invalid ID ---
    print("--- Attempt 2: Invalid ID (-5) ---")
    try:
        user_data = await fetch_user_data(-5)
        print("Success:", user_data)
    except ValueError as e:
        print("Error:", e)

# To run the async code:
if __name__ == "__main__":
    asyncio.run(main())

```

---

**Problem 14: Asynchronous Programming with async/await (Alternative Structure)**

*   **Objective:** Reinforce the use of `async/await` syntax for writing asynchronous code that looks synchronous, making it easier to read and manage.
*   **Task:**
    1.  Use the same `fetch_user_data(user_id)` async function from Problem 13.
    2.  Create a *separate* async function named `display_user_info(user_id)`.
    3.  Inside `display_user_info`, use `await` to call `fetch_user_data(user_id)`.
    4.  Use a `try...except ValueError` block *within* `display_user_info` to handle potential errors from the fetch operation.
    5.  If successful (inside `try`), print the user data received.
    6.  If it fails (inside `except`), print the error message received.
    7.  Modify the `main` async function (or create a new one) to call `display_user_info` with a valid ID (e.g., 456) and an invalid ID (e.g., 0). Run `main` using `asyncio.run()`.
*   **Tips:** This pattern encapsulates the fetching and handling logic within `display_user_info`, making the calling code (`main`) simpler. `async def`, `await`, and `try...except` remain the core tools.

---

**Answer**

```python
# Your code here
import asyncio

# Re-use the function from Problem 13
async def fetch_user_data(user_id):
    """Simulates fetching user data asynchronously."""
    print(f"Fetching data for user {user_id}...")
    await asyncio.sleep(1) # Simulate network delay
    if isinstance(user_id, int) and user_id > 0:
        print(f"Data received for user {user_id}.")
        return {"id": user_id, "name": f"User {user_id}"}
    else:
        raise ValueError("Invalid User ID")

async def display_user_info(user_id):
    """Fetches and displays user info, handling errors internally."""
    print(f"\n--- Processing display for ID: {user_id} ---")
    try:
        user_data = await fetch_user_data(user_id)
        print(f"User Info ({user_id}): {user_data}")
    except ValueError as e:
        print(f"Failed to get info for ID {user_id}: {e}")

async def main():
    # Call display_user_info for different IDs
    await display_user_info(456) # Valid ID
    await display_user_info(0)   # Invalid ID

# To run the async code:
if __name__ == "__main__":
    asyncio.run(main())

```

---

**Problem 15: Introduction to Classes and OOP (Object-Oriented Programming)**

*   **Objective:** Understand the basic concepts of OOP including Class, constructor (`__init__`), attributes (properties), and methods.
*   **Task:**
    1.  Create a `class` named `Car`.
    2.  Define the `__init__` method (constructor) for `Car` that accepts `make`, `color`, and `year`. This constructor should initialize instance attributes `self.make`, `self.color`, `self.year`, and also an attribute `self.speed` with an initial value of 0.
    3.  Add a *method* named `get_info()` that returns a string describing the car (e.g., "[Year] [Make] ([Color])").
    4.  Add a *method* named `accelerate(speed_increase)` that increases `self.speed` by `speed_increase` and prints the new speed to the console (e.g., "Current speed: [Speed] km/h").
    5.  Create two *instances* (objects) of the `Car` class with different data.
    6.  Call the `get_info()` and `accelerate()` methods on both instances.
*   **Tips:** Use the `class` keyword. The first parameter of instance methods (including `__init__`) is conventionally named `self`, which refers to the instance itself.

---

**Answer**

```python
# Your code here
class Car:
    def __init__(self, make, color, year):
        self.make = make
        self.color = color
        self.year = year
        self.speed = 0 # Initial speed

    def get_info(self):
        return f"{self.year} {self.make} ({self.color})"

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"Current speed: {self.speed} km/h")

# Create instances
car1 = Car("Toyota", "Red", 2021)
car2 = Car("Honda", "Blue", 2020)

# Use methods on car1
print(car1.get_info())
car1.accelerate(50)
car1.accelerate(30)

print("---") # Separator

# Use methods on car2
print(car2.get_info())
car2.accelerate(60)

```

---

**Problem 16: Inheritance in OOP**

*   **Objective:** Understand how to create subclasses that inherit attributes and methods from a superclass (parent class) and add specific functionality.
*   **Task:**
    1.  Use the `Car` class from Problem 15 as the parent class.
    2.  Create a new `class` named `Truck` that *inherits* from `Car`.
    3.  Define the `__init__` method for `Truck` that accepts `make`, `color`, `year`, and `payload_capacity`. This constructor must call the parent class's (`Car`) constructor using `super().__init__()` to initialize the inherited attributes, and then initialize its own specific attribute `self.payload_capacity`.
    4.  Add a new *method* to `Truck` named `load_cargo(cargo_weight)` that prints a message about loading cargo and the truck's capacity (e.g., "Loading cargo weighing [cargo_weight] kg. Max capacity: [payload_capacity] kg.").
    5.  *Override* the `get_info()` method in the `Truck` class to include the payload capacity information in addition to the basic car info. Use `super().get_info()` inside the overridden method to reuse the parent's implementation.
    6.  Create an *instance* of `Truck`.
    7.  Call the `get_info()`, `accelerate()`, and `load_cargo()` methods on the Truck instance.
*   **Tips:** Use `class ChildClass(ParentClass):` for inheritance. Use `super()` to call methods/constructor of the parent class. Overriding means defining a method in the child class with the same name as a method in the parent class.

---

**Answer**

```python
# Your code here

# Assuming Car class from Problem 15 is defined above or here:
class Car:
    def __init__(self, make, color, year):
        self.make = make
        self.color = color
        self.year = year
        self.speed = 0 # Initial speed

    def get_info(self):
        return f"{self.year} {self.make} ({self.color})"

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"Current speed: {self.speed} km/h")

# --- Truck Class ---
class Truck(Car):
    def __init__(self, make, color, year, payload_capacity):
        # Call parent constructor
        super().__init__(make, color, year)
        # Initialize truck-specific attribute
        self.payload_capacity = payload_capacity

    def load_cargo(self, cargo_weight):
        print(f"Loading cargo weighing {cargo_weight} kg. "
              f"Max capacity: {self.payload_capacity} kg.")

    # Override get_info method
    def get_info(self):
        # Get basic info from parent method
        basic_info = super().get_info()
        # Add truck-specific info
        return f"{basic_info} - Payload: {self.payload_capacity} kg"

# Create an instance of Truck
my_truck = Truck("Volvo", "White", 2019, 10000) # 10-ton capacity

# Use methods on the Truck instance
print(my_truck.get_info())
my_truck.accelerate(40)
my_truck.load_cargo(7500)

```

---

**Problem 17: Data Structures - Dictionary for Frequency Counting**

*   **Objective:** Use the `dict` data structure for a common use case: counting the frequency of items (like words in a sentence).
*   **Task:** Create a function `count_word_frequency(sentence)` that accepts a string `sentence`. The function should:
    1.  Convert the sentence to all lowercase (`lower()`).
    2.  Split the sentence into a list of words (use `split()` - basic splitting by spaces is fine).
    3.  Use a `dict` to store the frequency of each word. The keys should be the words, and the values should be their counts.
    4.  Return the dictionary containing the word frequencies.
*   **Example Call and Output:**
    ```python
    text = "I like eating rice goreng and rice uduk like it very much"
    frequency = count_word_frequency(text)
    print(frequency)
    # Example Output (order might vary):
    # {'i': 1, 'like': 2, 'eating': 1, 'rice': 2, 'goreng': 1, 'and': 1, 'uduk': 1, 'it': 1, 'very': 1, 'much': 1}
    ```
*   **Tips:** Iterate through the list of words. For each word, check if it's already a key in the dictionary. If yes, increment its value. If no, add it to the dictionary with a value of 1. Using `dict.get(key, default_value)` can simplify this (e.g., `word_counts[word] = word_counts.get(word, 0) + 1`). The `collections.Counter` class is specifically designed for this and is even more idiomatic.

---

**Answer**

```python
# Your code here (Method 1: Using standard dict)
def count_word_frequency(sentence):
    word_counts = {}
    words = sentence.lower().split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

# Your code here (Method 2: Using collections.Counter - more Pythonic)
# from collections import Counter
# def count_word_frequency_counter(sentence):
#    words = sentence.lower().split()
#    return Counter(words)

# Example call
text = "I like eating rice goreng and rice uduk like it very much"
frequency = count_word_frequency(text)
print(frequency)

# frequency_counter = count_word_frequency_counter(text)
# print(frequency_counter)

```

---

**Problem 18: Basic Algorithm - Binary Search**

*   **Objective:** Implement an efficient search algorithm for finding an element in a **sorted** list.
*   **Task:** Create a function `binary_search(sorted_list, target)`:
    1.  The function accepts a `list` of numbers that is **already sorted** in ascending order (`sorted_list`) and a `target` number to search for.
    2.  Implement the *binary search* algorithm to find the index of the `target` within `sorted_list`.
    3.  If the `target` is found, return its index.
    4.  If the `target` is not found after the search completes, return `-1`.
    5.  **Important:** Do not use Python's built-in `list.index()` method or other shortcuts. Implement the logic manually using `left`, `right`, and `middle` pointers/indices.
*   **Example Calls:**
    ```python
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(binary_search(sorted_numbers, 23))  # Expected Output: 5
    print(binary_search(sorted_numbers, 91))  # Expected Output: 9
    print(binary_search(sorted_numbers, 1))   # Expected Output: -1
    print(binary_search(sorted_numbers, 50))  # Expected Output: -1
    ```
*   **Tips:** Initialize `left = 0`, `right = len(sorted_list) - 1`. While `left <= right`, calculate `middle = (left + right) // 2` (use integer division). Compare `sorted_list[middle]` with `target`, and update `left` or `right` accordingly based on whether the target might be in the left or right half.

---

**Answer**

```python
# Your code here
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        middle = (left + right) // 2 # Integer division
        middle_value = sorted_list[middle]

        if middle_value == target:
            return middle # Target found
        elif middle_value < target:
            left = middle + 1 # Search in the right half
        else: # middle_value > target
            right = middle - 1 # Search in the left half

    return -1 # Target not found

# Example calls:
sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"Index of 23: {binary_search(sorted_numbers, 23)}")
print(f"Index of 91: {binary_search(sorted_numbers, 91)}")
print(f"Index of 1: {binary_search(sorted_numbers, 1)}")
print(f"Index of 50: {binary_search(sorted_numbers, 50)}")

```

---

**Problem 19: Advanced Error Handling (Custom Exceptions)**

*   **Objective:** Understand how to create and raise custom exception classes for more specific and informative error handling.
*   **Task:**
    1.  Create a *custom exception class* named `ValidationError` that inherits from Python's built-in `Exception`. Its `__init__` should accept an error message.
    2.  Create a function `validate_user_input(user_data)` that accepts a dictionary `user_data` (e.g., `{"name": "...", "email": "...", "age": ...}`).
    3.  This function should perform validations:
        *   If `name` is missing, empty, or not a string, raise (`raise`) `ValidationError("Name cannot be empty.")`.
        *   If `email` is missing, not a string, or doesn't contain '@', raise `ValidationError("Invalid email format.")`. (A simple `'@' in email` check is sufficient).
        *   If `age` is missing, not an integer, or less than 18, raise `ValidationError("Age must be at least 18 years old.")`.
    4.  If all validations pass, the function can return `True` or a success message.
    5.  Outside the function, call `validate_user_input` within a `try...except` block. Specifically catch `ValidationError` and print its message. Also include a general `except Exception` block to catch other potential errors. Test with valid and invalid data.
*   **Tips:** Define the custom exception like `class ValidationError(Exception): pass` (or add custom logic if needed). Use `raise ValidationError("message")` to throw the error. In the `except` block, use `except ValidationError as ve:` to catch the specific error and access its message (`ve.args[0]` or just `ve`).

---

**Answer**

```python
# Your code here

# 1. Custom Exception Class
class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

# 2. Validation Function
def validate_user_input(user_data):
    # Validate name
    name = user_data.get("name")
    if not name or not isinstance(name, str):
        raise ValidationError("Name cannot be empty.")

    # Validate email
    email = user_data.get("email")
    if not email or not isinstance(email, str) or '@' not in email:
        raise ValidationError("Invalid email format.")

    # Validate age
    age = user_data.get("age")
    if age is None or not isinstance(age, int) or age < 18:
        raise ValidationError("Age must be at least 18 years old.")

    # If all checks pass
    return True

# 5. Test Calls within try...except
print("--- Test Case 1: Valid Data ---")
valid_data = {"name": "Alice", "email": "alice@example.com", "age": 30}
try:
    if validate_user_input(valid_data):
        print("Validation successful for valid data.")
except ValidationError as ve:
    print(f"Validation Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Test Case 2: Invalid Age ---")
invalid_age_data = {"name": "Bob", "email": "bob@test.co", "age": 17}
try:
    validate_user_input(invalid_age_data)
    print("Validation successful (unexpected).")
except ValidationError as ve:
    print(f"Validation Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Test Case 3: Missing Email ---")
missing_email_data = {"name": "Charlie", "age": 25}
try:
    validate_user_input(missing_email_data)
    print("Validation successful (unexpected).")
except ValidationError as ve:
    print(f"Validation Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

---

**Problem 20: Python Modules**

*   **Objective:** Understand how to organize code into separate files (modules) using Python's `import` system.
*   **Task:**
    1.  Create a file named `utils.py`. Inside it, define and prepare for export (which happens automatically for functions/variables defined at the top level):
        *   A function `capitalize_words(s)`: Takes a string and returns a new string with the first letter of each word capitalized (e.g., "hello world" -> "Hello World"). You can use `s.title()`.
        *   A constant `TAX_RATE = 0.11`.
    2.  Create a file named `main.py` in the *same directory*.
    3.  In `main.py`, *import* the `capitalize_words` function and the `TAX_RATE` constant from `utils.py`.
    4.  Use the imported function to transform the string "selamat pagi indonesia" to "Selamat Pagi Indonesia" and print the result.
    5.  Print the value of the imported `TAX_RATE`.
    6.  **How to Run:** Simply run the `main.py` file using `python main.py` from your terminal, ensuring `utils.py` is in the same directory.
*   **Tips:** In `utils.py`, just define the function and the variable. In `main.py`, use `import utils` and access them like `utils.capitalize_words(...)` and `utils.TAX_RATE`. Alternatively, use `from utils import capitalize_words, TAX_RATE` to import them directly into the `main.py` namespace.

---

**Answer**

**File: `utils.py`**

```python
# utils.py

TAX_RATE = 0.11

def capitalize_words(s):
  """Capitalizes the first letter of each word in a string."""
  if not isinstance(s, str):
    return ""
  # return s.title() # Simple method
  # More robust manual method if needed:
  words = s.split()
  capitalized_words_list = [word.capitalize() for word in words]
  return " ".join(capitalized_words_list)

```

**File: `main.py`**

```python
# main.py

# Import specific items from the utils module
from utils import capitalize_words, TAX_RATE
# Or import the whole module: import utils

# Use the imported function
original_string = "selamat pagi indonesia"
capitalized_string = capitalize_words(original_string)
# If using 'import utils': capitalized_string = utils.capitalize_words(original_string)

print(f"Original: {original_string}")
print(f"Capitalized: {capitalized_string}")

# Use the imported constant
print(f"The current tax rate is: {TAX_RATE}")
# If using 'import utils': print(f"The current tax rate is: {utils.TAX_RATE}")

```

---

**Additional Best Practices for Advanced Python:**

1.  **Clean Code:** Focus on readability, small focused functions/classes, avoid code duplication (DRY - Don't Repeat Yourself). Follow PEP 8 guidelines.
2.  **Immutability:** Where practical, favor immutable data types (like tuples) or avoid modifying mutable types (lists, dictionaries) in place, especially when passing them around. Create copies if modification is needed.
3.  **Pure Functions:** Aim for functions whose output depends *only* on their input arguments and have no *side effects* (e.g., don't modify global variables, don't perform I/O unless that's their explicit purpose). They are easier to test and reason about.
4.  **Asynchronous Patterns:** Understand `asyncio.gather` for running tasks concurrently, `asyncio.wait_for` for timeouts, etc.
5.  **Testing:** Write unit tests (using libraries like `unittest` or `pytest`) for your code, especially for core logic and utility functions.
6.  **Dependency Management:** Use `pip` and `requirements.txt` (or tools like Poetry, Pipenv) to manage project dependencies. Consider using virtual environments (`venv`).
7.  **Version Control (Git):** Essential for tracking changes, collaboration, and managing codebases.
8.  **Type Hinting:** Use Python's type hints (PEP 484) to improve code clarity and allow for static analysis.
9.  **Docstrings:** Write clear docstrings (PEP 257) for modules, classes, and functions explaining what they do, their parameters, and what they return.

---


Okay, let's continue building on the previous foundation, now focusing specifically on skills relevant to a **Cyber Security Purple Team Engineer** using Python. These questions will involve more interaction with security concepts, data formats, and common tools/APIs (often simulated or using public resources).

**Assumptions:**
*   The candidate understands the concepts from Q1-20.
*   Focus is on using Python for tasks that bridge offensive simulation and defensive detection/analysis.
*   Ethical use and simulation are emphasized. **Never run scanning or potentially harmful scripts against systems you do not have explicit permission to test.**

---

**Python Advanced Training Series - Cyber Security Purple Team Focus (21-30)**

The goal of this section is to apply Python skills to common Purple Team tasks, including basic network interaction, log analysis, interacting with security APIs, simple data analysis for detection, and automating tests.

---

**Problem 21: Basic Network Port Scanning (Sockets)**

*   **Objective:** Understand how to use Python's `socket` library to perform basic network reconnaissance (port scanning) to identify open TCP ports.
*   **Task:** Create a Python function `check_tcp_port(ip_address, port)` that attempts to establish a TCP connection to the given `ip_address` and `port`.
    1.  The function should return `True` if the connection is successful (port is open) and `False` otherwise (port is closed, filtered, or host is unreachable).
    2.  Set a reasonable timeout (e.g., 1 second) for the connection attempt to avoid long waits.
    3.  Handle potential errors gracefully (e.g., invalid IP address format, socket errors).
    4.  Write a main part of the script that takes a target IP and a list of common ports (e.g., 21, 22, 23, 80, 443, 3389) and calls `check_tcp_port` for each, printing the results.
*   **Tips:** Use `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`, `socket.settimeout()`, `socket.connect_ex()`. `connect_ex()` is useful as it returns `0` on success and an error code otherwise, avoiding exceptions for simple closed ports. **Use only against systems you own or have explicit permission for (e.g., localhost `127.0.0.1` or a dedicated test VM).**
*   **Purple Team Relevance:** Simulates initial recon phase of an attack; helps verify firewall rules or service availability.

---

**Answer**

```python
# Your code here
import socket

def check_tcp_port(ip_address, port, timeout=1):
    """Checks if a TCP port is open on the given IP address."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        # connect_ex returns 0 on success, errno otherwise
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            return True # Port is open
        else:
            return False # Port is closed or filtered
    except socket.gaierror:
        print(f"Error: Hostname could not be resolved for {ip_address}")
        return False
    except socket.error as e:
        # Catch other potential socket errors (e.g., network unreachable)
        # print(f"Socket error for {ip_address}:{port} - {e}") # Optional detailed error
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1" # Safer target: localhost (use a known target if testing externally)
    # target_ip = "scanme.nmap.org" # Example public test target (use responsibly)
    common_ports = [21, 22, 23, 80, 135, 443, 445, 3389, 8080]

    print(f"Scanning {target_ip}...")
    for port in common_ports:
        is_open = check_tcp_port(target_ip, port)
        status = "Open" if is_open else "Closed/Filtered"
        print(f"Port {port}: {status}")

    # Example: Check a specific known open port if running a local server
    # if check_tcp_port('127.0.0.1', 8000): # e.g., python -m http.server 8000
    #     print("Port 8000 is open locally.")
```

---

**Problem 22: Parsing Web Server Logs (Regex & File Handling)**

*   **Objective:** Use regular expressions to parse common log formats (like Apache or Nginx access logs) to extract meaningful information for analysis.
*   **Task:** Create a function `parse_access_log(log_file_path)` that reads a log file line by line.
    1.  Assume a common log format like: `IP_ADDRESS - - [TIMESTAMP] "HTTP_METHOD URL PROTOCOL" STATUS_CODE BYTES_SENT "REFERER" "USER_AGENT"`
    2.  Use regular expressions (`re` module) to extract the `IP_ADDRESS`, `TIMESTAMP`, `HTTP_METHOD`, `URL`, and `STATUS_CODE` from each valid log entry.
    3.  The function should return a list of dictionaries, where each dictionary represents a parsed log line.
    4.  Handle potential `FileNotFoundError` and lines that don't match the expected format.
*   **Example Log Line:** `192.168.1.101 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 ..."`
*   **Tips:** Use `re.match()` or `re.search()`. Define capture groups `(...)` in your regex pattern. Be mindful of escaping special characters in the pattern. Read the file line by line to handle potentially large files.
*   **Purple Team Relevance:** Analyzing web logs is crucial for detecting web attacks (SQLi, XSS scans, enumeration), identifying compromised accounts, or tracking attacker movement.

---

**Answer**

```python
# Your code here
import re
import os # To create a dummy log file

# Regex for Common Log Format (adjust if needed for your specific format)
# Groups: 1=IP, 2=Timestamp, 3=Method, 4=URL, 5=Status Code
log_pattern = re.compile(
    r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # IP Address
    r'\s+-\s+-\s+' # Separators
    r'\[(?P<timestamp>.*?)\]\s+' # Timestamp
    r'"(?P<method>GET|POST|PUT|DELETE|HEAD)\s+(?P<url>.*?)\s+HTTP/[\d.]+"\s+' # Request Line
    r'(?P<status>\d{3})\s+' # Status Code
    r'.*$' # Ignore the rest for this exercise
)

def parse_access_log(log_file_path):
    """Parses a web server access log file."""
    parsed_logs = []
    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    log_entry = match.groupdict() # Get captured groups as a dictionary
                    # Convert status code to integer if desired
                    log_entry['status'] = int(log_entry['status'])
                    parsed_logs.append(log_entry)
                # else: # Optional: Handle lines that don't match
                #     print(f"Skipping non-matching line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return parsed_logs

if __name__ == "__main__":
    # Create a dummy log file for testing
    dummy_log_content = """
192.168.1.101 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0..."
10.0.0.5 - - [10/Oct/2023:13:55:37 +0000] "POST /login.php HTTP/1.1" 401 512 "http://example.com" "curl/7.68.0"
192.168.1.102 - - [10/Oct/2023:13:55:38 +0000] "GET /admin/config HTTP/1.1" 403 256 "-" "BadBot/1.0"
Invalid log line here
172.16.0.10 - - [10/Oct/2023:13:55:39 +0000] "GET /scripts/../etc/passwd HTTP/1.1" 404 480 "-" "Nmap Scripting Engine"
    """
    dummy_log_path = "dummy_access.log"
    with open(dummy_log_path, "w") as f:
        f.write(dummy_log_content.strip())

    parsed_data = parse_access_log(dummy_log_path)

    if parsed_data:
        print(f"Successfully parsed {len(parsed_data)} log entries.")
        # Print the first few entries for verification
        for entry in parsed_data[:3]:
            print(entry)
    else:
        print("No log entries parsed.")

    # Clean up the dummy file
    # os.remove(dummy_log_path) # Uncomment to delete after running
```

---

**Problem 23: Interacting with Security APIs (Requests & JSON)**

*   **Objective:** Use the `requests` library to query a public security API (like VirusTotal or AbuseIPDB - check their terms for free usage) and parse the JSON response.
*   **Task:** Create a function `check_ip_reputation(ip_address, api_key)` that queries the AbuseIPDB API (as an example) to get reputation data for an IP address.
    1.  The function needs to make an HTTP GET request to the appropriate API endpoint (`https://api.abuseipdb.com/api/v2/check`).
    2.  Include the necessary headers: `Key` (your API key) and `Accept` (`application/json`).
    3.  Include query parameters: `ipAddress` and `maxAgeInDays` (e.g., 90).
    4.  Use the `requests` library. Handle potential request errors (network issues, non-200 status codes).
    5.  Parse the JSON response using `response.json()`.
    6.  Return the relevant part of the parsed JSON data (e.g., the 'data' dictionary).
*   **Tips:** You'll need to sign up for a free API key from AbuseIPDB (or a similar service). **Never hardcode API keys directly in your script.** Use environment variables or a configuration file (for this exercise, passing as an argument is acceptable, but mention best practices). Install `requests`: `pip install requests`.
*   **Purple Team Relevance:** Automating threat intelligence lookups for IPs, domains, or hashes observed during incidents or simulations.

---

**Answer**

```python
# Your code here
import requests
import json
import os # For getting API key from environment variable

# Best practice: Store API key in environment variable or config file
# For this example, we try environment first, then allow passing directly
ABUSEIPDB_API_KEY = os.environ.get("ABUSEIPDB_API_KEY", None)

def check_ip_reputation(ip_address, api_key):
    """Queries the AbuseIPDB API for IP reputation data."""
    if not api_key:
        print("Error: AbuseIPDB API key not provided or found in environment variables.")
        return None

    # Define the API endpoint and parameters
    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90',
        # 'verbose': True # Uncomment for more detailed output
    }
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the JSON response
        json_response = response.json()
        return json_response.get('data', None) # Return the 'data' part

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON response: {response.text}")
        return None

if __name__ == "__main__":
    # Replace with your actual API key if not using environment variables
    if ABUSEIPDB_API_KEY is None:
        print("Please set the ABUSEIPDB_API_KEY environment variable or enter it below.")
        # ABUSEIPDB_API_KEY = input("Enter your AbuseIPDB API Key: ") # Uncomment for interactive input

    if ABUSEIPDB_API_KEY:
        target_ip_good = "8.8.8.8" # Generally safe IP (Google DNS)
        target_ip_suspicious = "1.1.1.1" # Often has reports (Cloudflare DNS, check actual status)
        target_ip_bad = "118.25.6.39" # Frequently reported example (check current status)


        print(f"--- Checking {target_ip_good} ---")
        reputation_good = check_ip_reputation(target_ip_good, ABUSEIPDB_API_KEY)
        if reputation_good:
            print(f"Abuse Confidence Score: {reputation_good.get('abuseConfidenceScore')}")
            print(f"Country: {reputation_good.get('countryCode')}")
            print(f"ISP: {reputation_good.get('isp')}")
        else:
            print("Failed to get reputation data.")


        print(f"\n--- Checking {target_ip_bad} ---")
        reputation_bad = check_ip_reputation(target_ip_bad, ABUSEIPDB_API_KEY)
        if reputation_bad:
             print(f"Abuse Confidence Score: {reputation_bad.get('abuseConfidenceScore')}")
             print(f"Total Reports: {reputation_bad.get('totalReports')}")
             print(f"Last Reported At: {reputation_bad.get('lastReportedAt')}")
        else:
            print("Failed to get reputation data.")
    else:
        print("API Key not available. Skipping API checks.")
```

---

**Problem 24: Calculating File Hashes (hashlib)**

*   **Objective:** Understand how to compute cryptographic hashes (MD5, SHA1, SHA256) for files, commonly used for file identification and integrity verification.
*   **Task:** Create a function `calculate_hashes(file_path)` that:
    1.  Reads a file in binary mode (`'rb'`).
    2.  Calculates the MD5, SHA1, and SHA256 hashes of the file's content.
    3.  Returns a dictionary containing the lowercase hexadecimal representation of each hash (e.g., `{'md5': '...', 'sha1': '...', 'sha256': '...'}`).
    4.  Handle `FileNotFoundError`. Be efficient for potentially large files by reading in chunks.
*   **Tips:** Use the `hashlib` module (`hashlib.md5()`, `hashlib.sha1()`, `hashlib.sha256()`). Read the file in chunks (e.g., 4096 bytes) and update the hash object iteratively (`hasher.update(chunk)`). Use `hasher.hexdigest()` to get the final hash string.
*   **Purple Team Relevance:** Identifying known malicious files based on hash (IOC matching), verifying file integrity after potential modification, tracking malware variants.

---

**Answer**

```python
# Your code here
import hashlib
import os

def calculate_hashes(file_path, chunk_size=4096):
    """Calculates MD5, SHA1, and SHA256 hashes for a given file."""
    hashes = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256()}
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                for hasher in hashes.values():
                    hasher.update(chunk)

        # Return dictionary of hexdigests
        return {name: hasher.hexdigest() for name, hasher in hashes.items()}

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while hashing {file_path}: {e}")
        return None

if __name__ == "__main__":
    # Create a dummy file to hash
    dummy_file_path = "dummy_file_to_hash.txt"
    with open(dummy_file_path, "w") as f:
        f.write("This is a test file for hashing.\n")
        f.write("Purple teaming exercises are fun!\n")

    file_hashes = calculate_hashes(dummy_file_path)

    if file_hashes:
        print(f"Hashes for {dummy_file_path}:")
        print(f"  MD5:    {file_hashes['md5']}")
        print(f"  SHA1:   {file_hashes['sha1']}")
        print(f"  SHA256: {file_hashes['sha256']}")
    else:
        print(f"Could not calculate hashes for {dummy_file_path}")

    # Clean up the dummy file
    os.remove(dummy_file_path)

    # Example with a non-existent file
    print("\n--- Testing non-existent file ---")
    calculate_hashes("non_existent_file.xyz")
```

---

**Problem 25: Simple IOC Matching (Sets/Dictionaries)**

*   **Objective:** Efficiently check if observed data points (like IP addresses or domain names) exist within a predefined list of Indicators of Compromise (IOCs).
*   **Task:**
    1.  Define a set `bad_ips` containing known malicious IP addresses (strings).
    2.  Define a dictionary `suspicious_domains` where keys are suspicious domain names (strings) and values are reasons (e.g., "phishing", "C2").
    3.  Create a function `check_indicators(observed_ips, observed_domains)` that takes two lists: `observed_ips` (from logs or network traffic) and `observed_domains`.
    4.  The function should identify and return:
        *   A list of IPs from `observed_ips` that are present in `bad_ips`.
        *   A list of domains from `observed_domains` that are keys in `suspicious_domains`, possibly including the reason.
*   **Tips:** Use set intersection (`&` or `set.intersection()`) for efficient IP checking. Iterate through `observed_domains` and check for existence as keys in the `suspicious_domains` dictionary (`domain in suspicious_domains`).
*   **Purple Team Relevance:** Core activity in threat detection - quickly identifying known bad entities in observed data. Sets provide very fast lookups.

---

**Answer**

```python
# Your code here

# Define IOC lists (use sets for efficient lookups where appropriate)
bad_ips = {
    "198.51.100.5",
    "203.0.113.10",
    "118.25.6.39", # From AbuseIPDB example
    "1.2.3.4"      # Placeholder bad IP
}

suspicious_domains = {
    "malicious-site.example.com": "Known C2 Server",
    "phishing-login.example.net": "Phishing Domain",
    "randomstringxyz.ru": "DGA Suspected",
    "update.drive-by.info": "Drive-by Download Source"
}

def check_indicators(observed_ips, observed_domains):
    """Checks observed IPs and domains against known bad/suspicious lists."""
    found_bad_ips = list(set(observed_ips) & bad_ips) # Efficiently find intersection

    found_suspicious_domains = {} # Store domain and reason
    for domain in observed_domains:
        if domain in suspicious_domains:
            found_suspicious_domains[domain] = suspicious_domains[domain]

    return found_bad_ips, found_suspicious_domains

if __name__ == "__main__":
    # Simulate observed data
    live_ips = ["10.1.1.5", "192.168.0.20", "198.51.100.5", "8.8.8.8", "203.0.113.10"]
    live_domains = ["google.com", "internal.corp", "phishing-login.example.net", "microsoft.com", "randomstringxyz.ru"]

    matched_ips, matched_domains = check_indicators(live_ips, live_domains)

    print("--- IOC Matching Results ---")
    if matched_ips:
        print("Matched Bad IPs:")
        for ip in matched_ips:
            print(f"  - {ip}")
    else:
        print("No known bad IPs matched.")

    if matched_domains:
        print("\nMatched Suspicious Domains:")
        for domain, reason in matched_domains.items():
            print(f"  - {domain} ({reason})")
    else:
        print("No known suspicious domains matched.")
```

---

**Problem 26: Basic PCAP Analysis (Scapy)**

*   **Objective:** Use the `scapy` library to read a network packet capture (PCAP) file and extract specific information (e.g., DNS queries or HTTP hosts).
*   **Task:** Create a function `analyze_pcap(pcap_file_path)` that:
    1.  Reads packets from the given PCAP file using `scapy`.
    2.  Iterates through each packet.
    3.  If a packet contains a DNS query (UDP port 53, has `DNSQR` layer), extract and print the queried name (`qname`).
    4.  If a packet contains an HTTP request (TCP port 80, contains `Raw` layer that looks like an HTTP request), try to extract and print the `Host` header.
    5.  Handle potential errors like file not found or malformed packets.
*   **Tips:** Install `scapy`: `pip install scapy`. Use `rdpcap()` to read the file. Check for layers using `packet.haslayer(DNS)` or `packet.haslayer(TCP)`. Access layer fields like `packet[DNSQR].qname` or `packet[TCP].dport`. HTTP parsing might require checking the `Raw` layer payload and using string searching or regex for the `Host:` header. **You'll need a sample PCAP file for testing.** You can generate one with Wireshark/tcpdump or find samples online (e.g., Wireshark Sample Captures).
*   **Purple Team Relevance:** Analyzing network traffic is fundamental for understanding attacker actions (C2 communication, data exfiltration, lateral movement) and verifying detection rules based on network data.

---

**Answer**

```python
# Your code here
# Make sure to install scapy: pip install scapy
try:
    from scapy.all import rdpcap, DNS, DNSQR, TCP, Raw
    import re
except ImportError:
    print("Scapy is not installed. Please install it: pip install scapy")
    exit() # Exit if scapy is not available

# Simple regex to find Host header in HTTP request payload
http_host_pattern = re.compile(rb"Host:\s+([^\r\n]+)", re.IGNORECASE)

def analyze_pcap(pcap_file_path):
    """Reads a PCAP file and extracts DNS queries and HTTP Host headers."""
    try:
        packets = rdpcap(pcap_file_path)
    except FileNotFoundError:
        print(f"Error: PCAP file not found at {pcap_file_path}")
        return
    except Exception as e: # Scapy might raise various errors on malformed files
        print(f"Error reading PCAP file {pcap_file_path}: {e}")
        return

    print(f"Analyzing {len(packets)} packets from {pcap_file_path}...")

    dns_queries = set()
    http_hosts = set()

    for i, packet in enumerate(packets):
        try:
            # Check for DNS Queries (usually UDP destination port 53)
            if packet.haslayer(DNS) and packet.haslayer(DNSQR) and packet.dport == 53:
                # qname is often bytes, decode it
                qname = packet[DNSQR].qname.decode('utf-8', errors='ignore')
                if qname not in dns_queries:
                   print(f"  [Packet {i+1}] DNS Query: {qname}")
                   dns_queries.add(qname)


            # Check for potential HTTP Requests (usually TCP destination port 80)
            if packet.haslayer(TCP) and packet.dport == 80 and packet.haslayer(Raw):
                payload = packet[Raw].load
                # Basic check if it looks like an HTTP request method
                if payload.startswith((b'GET ', b'POST ', b'PUT ', b'HEAD ', b'DELETE ')):
                    match = http_host_pattern.search(payload)
                    if match:
                        host = match.group(1).decode('utf-8', errors='ignore')
                        if host not in http_hosts:
                            print(f"  [Packet {i+1}] HTTP Host Header: {host}")
                            http_hosts.add(host)

        except Exception as e:
            print(f"  [Packet {i+1}] Error processing packet: {e}") # Handle errors per packet

if __name__ == "__main__":
    # You need a sample PCAP file. Download one from Wireshark Sample Captures
    # or create one using Wireshark/tcpdump while browsing.
    # Example: sample_pcap_path = 'http.pcap' # Make sure this file exists
    sample_pcap_path = 'sample.pcap' # Replace with your actual PCAP file path

    # Check if the sample file exists before trying to analyze
    import os
    if os.path.exists(sample_pcap_path):
         analyze_pcap(sample_pcap_path)
    else:
         print(f"Error: Sample PCAP file '{sample_pcap_path}' not found.")
         print("Please download a sample PCAP or create one (e.g., using Wireshark)")
         print("and place it in the same directory or update the path.")

```

---

**Problem 27: Generating Simple Network Indicators**

*   **Objective:** Create simple network traffic or file artifacts designed to trigger specific, basic detection rules.
*   **Task:** Write two functions:
    1.  `generate_suspicious_dns_lookup(domain)`: Uses `socket.gethostbyname()` to perform a DNS lookup for a given `domain`. (This action itself might be logged by DNS servers or security tools).
    2.  `create_test_file_with_string(file_path, content_string)`: Creates a file at `file_path` containing the given `content_string`. This could be used to test file integrity monitoring or AV signature detection if `content_string` is a known bad signature (like the EICAR test string).
*   **Tips:** `socket.gethostbyname()` is straightforward but handle potential `socket.gaierror` if the domain doesn't resolve. For file creation, use standard `open()` with write mode (`'w'`).
*   **Example `content_string` (EICAR Test String):** `r'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'` (Use raw string `r''` or escape backslashes).
*   **Purple Team Relevance:** Creating controlled events to test if detection mechanisms (EDR, NIDS, SIEM rules) trigger as expected.

---

**Answer**

```python
# Your code here
import socket
import os

def generate_suspicious_dns_lookup(domain):
    """Performs a DNS lookup for the given domain."""
    print(f"Attempting DNS lookup for: {domain}")
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"  -> Resolved {domain} to {ip_address}")
        return True
    except socket.gaierror:
        print(f"  -> Failed to resolve {domain}")
        return False
    except Exception as e:
        print(f"  -> An unexpected error occurred during lookup: {e}")
        return False

def create_test_file_with_string(file_path, content_string):
    """Creates a file containing a specific string."""
    print(f"Creating test file at: {file_path}")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_string)
        print(f"  -> File created successfully.")
        return True
    except IOError as e:
        print(f"  -> Error creating file {file_path}: {e}")
        return False
    except Exception as e:
        print(f"  -> An unexpected error occurred during file creation: {e}")
        return False

if __name__ == "__main__":
    print("--- Generating Test Indicators ---")

    # 1. Suspicious DNS Lookup Simulation
    # Use a domain known for testing or one unlikely to be cached heavily
    # (Avoid high-traffic domains like google.com for clearer test logs)
    test_domain = "malware-test-domain.example.com" # A fictional domain
    generate_suspicious_dns_lookup(test_domain)
    generate_suspicious_dns_lookup("hopefullynonexistentdomain12345.xyz") # Likely fails

    print("\n---\n")

    # 2. Creating Test File (e.g., for EICAR)
    eicar_string = r'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
    test_file = "eicar_test.txt" # AV might immediately flag/delete this!
    created = create_test_file_with_string(test_file, eicar_string)

    if created:
        print(f"'{test_file}' created. Check if your AV detected it.")
        # Optional: Clean up the file immediately if needed
        try:
             # A small delay might be needed for AV to react before deletion
             # import time
             # time.sleep(5)
             if os.path.exists(test_file):
                  os.remove(test_file)
                  print(f"  -> Test file '{test_file}' removed.")
        except Exception as e:
             print(f"  -> Could not remove test file: {e}")
    else:
        print(f"Failed to create '{test_file}'.")

```

---

**Problem 28: Automating Detection Rule Testing**

*   **Objective:** Combine generating an indicator with checking for an expected detection log/alert (simulated).
*   **Task:** Create a function `test_dns_rule(domain_to_lookup, log_check_function)`:
    1.  Call the `generate_suspicious_dns_lookup(domain_to_lookup)` function (from Q27).
    2.  Wait for a short period (e.g., `time.sleep(5)`) to simulate log propagation/alert generation.
    3.  Call the provided `log_check_function`, passing the `domain_to_lookup` as an argument. This function *simulates* querying a SIEM or log source.
    4.  The `log_check_function` should return `True` if a log/alert related to the domain lookup is found (simulated), and `False` otherwise.
    5.  The `test_dns_rule` function should return `True` if the lookup was attempted *and* the log check returned `True`, indicating the rule likely fired. Return `False` otherwise.
*   **Implementation Detail:** You will need to *create a simple dummy `log_check_function`* for this exercise. This dummy function could, for example, check if the domain exists in a predefined list of "triggered alerts" or randomly return True/False for simulation purposes.
*   **Tips:** Use `import time`. Structure the logic clearly: generate, wait, check.
*   **Purple Team Relevance:** Automating the validation of detection rules. Did generating event X result in expected alert Y?

---

**Answer**

```python
# Your code here
import socket
import time
import random # For dummy check function

# --- Re-use function from Q27 ---
def generate_suspicious_dns_lookup(domain):
    """Performs a DNS lookup for the given domain."""
    print(f"Attempting DNS lookup for: {domain}")
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"  -> Resolved {domain} to {ip_address}")
        return True # Indicate lookup was attempted/successful
    except socket.gaierror:
        print(f"  -> Failed to resolve {domain}")
        return True # Still attempted, even if failed
    except Exception as e:
        print(f"  -> An unexpected error occurred during lookup: {e}")
        return False # Indicate a fundamental error occurred


# --- Dummy Log Check Function ---
# In a real scenario, this would query a SIEM API, parse a log file, etc.
SIMULATED_DETECTED_DOMAINS = {"evil-c2.example.org", "phishing-landing.example.net"}
def dummy_log_check(domain_looked_up):
    """Simulates checking logs/SIEM for an alert related to the domain."""
    print(f"Simulating log check for domain: {domain_looked_up}...")
    # Simulate some delay for the check itself
    time.sleep(random.uniform(0.5, 1.5))

    # Simple simulation logic: Did we intend for this domain to be detected?
    if domain_looked_up in SIMULATED_DETECTED_DOMAINS:
        print(f"  -> SIMULATED: Alert found for {domain_looked_up}!")
        return True
    else:
        # Simulate occasional false positives or finding unrelated logs? (Optional)
        # if random.random() < 0.1: # 10% chance of simulated unrelated finding
        #    print("  -> SIMULATED: Found unrelated activity (False Positive simulation).")
        #    return False # Or True depending on test goal
        print(f"  -> SIMULATED: No specific alert found for {domain_looked_up}.")
        return False

# --- Main Test Function ---
def test_dns_rule(domain_to_lookup, log_check_function, wait_time=5):
    """Generates a DNS lookup and checks if a simulated detection occurred."""
    print(f"\n--- Testing Detection Rule for Domain: {domain_to_lookup} ---")

    # 1. Generate the indicator event
    lookup_attempted = generate_suspicious_dns_lookup(domain_to_lookup)

    if not lookup_attempted:
        print("Failed to even attempt the DNS lookup. Test aborted.")
        return False # Cannot test if the trigger failed

    # 2. Wait for simulated log propagation/alerting
    print(f"Waiting {wait_time} seconds for logs/alert generation...")
    time.sleep(wait_time)

    # 3. Check for the expected log/alert
    detection_result = log_check_function(domain_to_lookup)

    # 4. Determine test outcome
    if detection_result:
        print(f"SUCCESS: DNS lookup for '{domain_to_lookup}' generated an expected detection.")
        return True
    else:
        print(f"FAILURE: DNS lookup for '{domain_to_lookup}' did NOT generate an expected detection.")
        return False

if __name__ == "__main__":
    # Test case 1: Domain expected to be detected
    test_dns_rule("evil-c2.example.org", dummy_log_check)

    # Test case 2: Domain NOT expected to be detected
    test_dns_rule("google.com", dummy_log_check)

    # Test case 3: Domain lookup might fail, but we still check logs
    test_dns_rule("nonexistentdomain12345abc.xyz", dummy_log_check)

```

---

**Problem 29: Basic Static File Analysis (Extracting Strings)**

*   **Objective:** Perform rudimentary static analysis on a file (potentially a binary/executable) by extracting printable ASCII strings.
*   **Task:** Create a function `extract_printable_strings(file_path, min_length=4)` that:
    1.  Reads the given `file_path` in binary mode (`'rb'`).
    2.  Iterates through the file content byte by byte or in chunks.
    3.  Identifies sequences of consecutive bytes that represent printable ASCII characters (decimal values 32-126).
    4.  Collects these sequences.
    5.  Returns a list of extracted strings that meet the `min_length` requirement.
    6.  Handle `FileNotFoundError`.
*   **Tips:** Read the file content. Iterate through bytes. Maintain a current potential string. If a byte is printable, append its character representation (`chr(byte)`) to the current string. If it's not printable, check if the current string meets `min_length` and add it to the results, then reset the current string. Remember to handle the end of the file.
*   **Purple Team Relevance:** Quick way to find interesting artifacts in unknown binaries (IPs, URLs, file paths, commands, registry keys) without executing them. Helps form hypotheses about file functionality.

---

**Answer**

```python
# Your code here
import string
import os

def extract_printable_strings(file_path, min_length=4):
    """Extracts printable ASCII strings from a file."""
    printable_chars = bytes(string.printable, 'ascii')
    found_strings = []
    try:
        with open(file_path, 'rb') as f:
            current_string = b""
            while True:
                byte = f.read(1)
                if not byte: # End of file
                    break

                # Check if the byte represents a printable ASCII character
                # Note: string.printable includes whitespace like \n, \t, \r.
                # You might want a stricter check (e.g., range(32, 127))
                # if byte[0] >= 32 and byte[0] <= 126: # Stricter check
                if byte in printable_chars:
                    current_string += byte
                else:
                    # If current string meets min length, add it
                    if len(current_string) >= min_length:
                        # Decode final string, ignoring errors
                        found_strings.append(current_string.decode('ascii', errors='ignore'))
                    current_string = b"" # Reset

            # Check the last string sequence after EOF
            if len(current_string) >= min_length:
                 found_strings.append(current_string.decode('ascii', errors='ignore'))

        return found_strings

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
        return None


if __name__ == "__main__":
    # Create a dummy binary-like file for testing
    dummy_bin_path = "dummy_file.bin"
    with open(dummy_bin_path, 'wb') as f:
        f.write(b'\x01\x02\x03\x04') # Non-printable
        f.write(b'This is string 1.\n') # Printable (including newline)
        f.write(b'\x05\x06')
        f.write(b'URL=http://example.com/path')
        f.write(b'\x07\x08\x09')
        f.write(b'Short') # Might be missed if min_length=5
        f.write(b'\x0A\x0B')
        f.write(b'AnotherLongStringHere')
        f.write(b'\x0C')

    print(f"--- Extracting strings from {dummy_bin_path} (min_length=4) ---")
    strings_found = extract_printable_strings(dummy_bin_path, min_length=4)

    if strings_found is not None:
        if strings_found:
            print("Found strings:")
            for s in strings_found:
                print(f"  - {repr(s)}") # Use repr to show whitespace chars
        else:
            print("No printable strings found meeting the criteria.")
    else:
        print("String extraction failed.")

    # Clean up
    os.remove(dummy_bin_path)

    # Example with non-existent file
    print("\n--- Testing non-existent file ---")
    extract_printable_strings("non_existent_binary.exe")

```

---

**Problem 30: Consolidating Findings into a Report (Data Structures & Formatting)**

*   **Objective:** Structure data collected from various analyses (like port scans, log parsing, IOC checks) into a formatted report (e.g., simple text or JSON).
*   **Task:** Create a function `generate_report(scan_results, log_findings, ioc_matches)` that takes data structures representing findings from previous steps (or simulated data):
    1.  `scan_results`: A dictionary mapping IPs to lists of open ports (e.g., `{'127.0.0.1': [80, 443]}`).
    2.  `log_findings`: A list of parsed log dictionaries (like from Q22).
    3.  `ioc_matches`: A tuple containing lists of matched IPs and domains (like from Q25, e.g., `(['1.2.3.4'], {'bad.com': 'C2'})`).
    4.  The function should format this information into a human-readable string report OR a structured JSON string. Choose one format.
*   **Example Output (Text Format):**
    ```
    *** Security Analysis Report ***

    [+] Port Scan Results:
      - 127.0.0.1: Ports [80, 443] open.

    [+] Interesting Log Entries (Top 5):
      - IP: 10.0.0.5, Status: 401, URL: /login.php
      - IP: 192.168.1.102, Status: 403, URL: /admin/config
      ... (more entries) ...

    [+] IOC Matches:
      - Matched Bad IPs: ['1.2.3.4']
      - Matched Suspicious Domains: {'bad.com': 'C2'}

    *** End of Report ***
    ```
*   **Tips:** Use f-strings or `str.format()` for text reports. Use the `json` module (`json.dumps()`) for JSON output, providing `indent` for readability. Iterate through the input data structures to populate the report sections.
*   **Purple Team Relevance:** Reporting findings clearly is essential. Consolidating data from different tools/scripts into a single view aids analysis and communication between Red and Blue teams.

---

**Answer**

```python
# Your code here
import json
from datetime import datetime

def generate_report_text(scan_results, log_findings, ioc_matches):
    """Generates a human-readable text report."""
    report_lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines.append("*** Security Analysis Report ***")
    report_lines.append(f"Generated: {now}")
    report_lines.append("=" * 30)

    # Port Scan Section
    report_lines.append("\n[+] Port Scan Results:")
    if scan_results:
        for ip, ports in scan_results.items():
            report_lines.append(f"  - {ip}: Ports {ports} open.")
    else:
        report_lines.append("  No port scan data provided.")

    # Log Findings Section
    report_lines.append("\n[+] Interesting Log Entries (Sample):")
    if log_findings:
        # Show only a sample, e.g., first 5
        limit = 5
        for i, entry in enumerate(log_findings[:limit]):
            # Assuming keys 'ip', 'status', 'url' exist from Q22 parsing
            ip = entry.get('ip', 'N/A')
            status = entry.get('status', 'N/A')
            url = entry.get('url', 'N/A')
            timestamp = entry.get('timestamp', '') # Optional
            report_lines.append(f"  - [{timestamp}] IP: {ip}, Status: {status}, URL: {url}")
        if len(log_findings) > limit:
            report_lines.append(f"  ... (and {len(log_findings) - limit} more entries)")
    else:
        report_lines.append("  No log findings provided.")

    # IOC Matches Section
    report_lines.append("\n[+] IOC Matches:")
    matched_ips, matched_domains = ioc_matches if ioc_matches else ([], {})
    if matched_ips:
         report_lines.append(f"  - Matched Bad IPs: {matched_ips}")
    else:
         report_lines.append("  - No known bad IPs matched.")

    if matched_domains:
        domains_str = ', '.join([f"{dom} ({reason})" for dom, reason in matched_domains.items()])
        report_lines.append(f"  - Matched Suspicious Domains: {domains_str}")
    else:
        report_lines.append("  - No known suspicious domains matched.")


    report_lines.append("\n" + "=" * 30)
    report_lines.append("*** End of Report ***")

    return "\n".join(report_lines)

def generate_report_json(scan_results, log_findings, ioc_matches):
    """Generates a structured JSON report string."""
    report_data = {
        "reportGeneratedTime": datetime.now().isoformat(),
        "portScanResults": scan_results or {},
        "logFindingsSample": log_findings[:5] if log_findings else [], # Include a sample
        "totalLogFindings": len(log_findings) if log_findings else 0,
        "iocMatches": {
            "matchedBadIps": ioc_matches[0] if ioc_matches else [],
            "matchedSuspiciousDomains": ioc_matches[1] if ioc_matches else {}
        }
    }
    try:
        # Use indent for pretty printing
        return json.dumps(report_data, indent=2)
    except TypeError as e:
        print(f"Error generating JSON report: {e}")
        return "{ 'error': 'Failed to serialize report data' }"


if __name__ == "__main__":
    # --- Simulate data from previous steps ---
    sim_scan_results = {'192.168.1.102': [80, 443], '10.0.0.5': [80]}
    sim_log_findings = [
        {'ip': '10.0.0.5', 'timestamp': '10/Oct/2023:13:55:37 +0000', 'method': 'POST', 'url': '/login.php', 'status': 401},
        {'ip': '192.168.1.102', 'timestamp': '10/Oct/2023:13:55:38 +0000', 'method': 'GET', 'url': '/admin/config', 'status': 403},
        {'ip': '172.16.0.10', 'timestamp': '10/Oct/2023:13:55:39 +0000', 'method': 'GET', 'url': '/scripts/../etc/passwd', 'status': 404}
    ]
    sim_ioc_matches = (['203.0.113.10'], {'phishing-login.example.net': 'Phishing Domain'})
    sim_empty_ioc = ([], {})


    # --- Generate Text Report ---
    print("--- Generating Text Report ---")
    text_report = generate_report_text(sim_scan_results, sim_log_findings, sim_ioc_matches)
    print(text_report)

    # --- Generate JSON Report ---
    print("\n\n--- Generating JSON Report ---")
    json_report = generate_report_json(sim_scan_results, sim_log_findings, sim_ioc_matches)
    print(json_report)

    print("\n\n--- Generating Text Report (Empty IOCs) ---")
    text_report_empty = generate_report_text({}, [], sim_empty_ioc)
    print(text_report_empty)

```

---

**Cyber Security Specific Best Practices Reminder:**

1.  **Security:** Be extremely careful when handling sensitive data (credentials, API keys, PII). Use secure methods like environment variables, vault solutions, or config files with appropriate permissions. Avoid hardcoding secrets.
2.  **Error Handling:** Network connections, API calls, and file operations often fail. Implement robust error handling (`try...except`) and logging to understand failures.
3.  **Input Validation:** If your script takes input (filenames, IPs, domains), validate it carefully to prevent injection attacks or unexpected behavior.
4.  **Resource Management:** Close sockets and file handles properly (using `with open(...)` is recommended for files). Be mindful of resource consumption (memory, CPU) when processing large files or many network connections.
5.  **Logging:** Implement proper logging (`logging` module) instead of just `print()` statements for production tools. Log errors, important actions, and outcomes.
6.  **Ethical Use:** **Reiterate:** Only run tests against systems you have explicit, written permission to test. Understand the potential impact of your scripts.
7.  **Modularity:** Break down complex tasks into smaller, reusable functions and potentially separate modules (like a `utils.py` for common tasks or `apis.py` for API interactions).
8.  **Dependencies:** Clearly document external library dependencies (e.g., in a `requirements.txt` file).

---