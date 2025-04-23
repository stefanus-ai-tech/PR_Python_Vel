**Python Fundamentals: A Hands-On Learning Path**

**Task Set 1: Getting Started - Displaying Info & Basic Variables**

1.  **Display a Message:** Write code to show the text "Python journey begins!" in the console output.
2.  **Store and Update Information:**
    - Declare a variable named `current_status` and assign it the string value "Initializing". Print `current_status`.
    - On the next line, change the value of `current_status` to "Ready". Print `current_status` again. (Observe Python's dynamic typing and variable reassignment).
3.  **Storing "Constant" Information (Convention):**
    - Declare a variable named `SITE_NAME` (using all caps is a common Python convention for values intended not to change) and assign it the value "CodeRunner". Print `SITE_NAME`.
    - On the next line, _try_ to change the value of `SITE_NAME` to "CodeHub". Print it again.
    - Run the code. **Observe that Python allows this change.** Unlike JavaScript's `const`, Python doesn't have built-in immutable variable bindings; the uppercase convention is a signal to other developers.
4.  **Basic Data Types:**
    - Declare `user_name` and assign it your name (a string).
    - Declare `user_age` and assign it your age (an integer).
    - Declare `user_height_meters` and assign it your height in meters (a float, e.g., `1.75`).
    - Declare `is_subscribed` and assign it `True` (a boolean - note the capital 'T').
    - Print each of these variables to the console.

**Task Set 2: Working with Numbers & Text**

5.  **Calculations:**
    - Declare `price = 50.0` and `quantity = 3`.
    - Calculate the `total_cost` by multiplying `price` and `quantity`. Print `total_cost`.
    - Declare `discount = 10.0`. Calculate the `final_cost` by subtracting `discount` from `total_cost`. Print `final_cost`.
6.  **Leftovers (Modulo):**
    - Declare `items = 17` and `items_per_box = 5`.
    - Calculate how many items will be `leftover` using the modulo operator (`%`). Print `leftover`.
7.  **Integer Division:**
    - Using `items` and `items_per_box` from task 6, calculate how many `full_boxes` can be made using integer division (`//`). Print `full_boxes`.
8.  **Combining Text (f-strings):**
    - Use the `user_name` and `user_age` variables from Task 4.
    - Create a `user_info` string using an **f-string** like this: `f"User: {user_name}, Age: {user_age}"`. Print `user_info`.
9.  **Text & Numbers - Observation 1 (Concatenation Error):**
    - _Try_ to print the result of `"Score: " + 95`.
    - Run the code. **Observe the TypeError**. Python does _not_ automatically convert numbers to strings for concatenation using `+`.
10. **Text & Numbers - Observation 2 (Explicit Conversion):**
    - Correct the previous task: Print the result of `"Score: " + str(95)`. Observe how `str()` is used for explicit conversion.
11. **Text & Numbers - Observation 3 (Numeric Conversion):**
    - Print the result of `int("100") - 10`. Observe how `int()` converts the string to a number before the subtraction. What happens if you try `int("hello")`? (You'll get a ValueError).
12. **Augmented Assignment:**
    - Declare `click_count = 0`.
    - Use the augmented assignment operator `+=` to increment `click_count` by 1 (`click_count += 1`). Print `click_count`.
    - Decrement `click_count` by 1 using `-=`. Print `click_count`. (Note: Python doesn't have `++` or `--` operators like JavaScript).

**Task Set 3: Making Decisions**

13. **Simple Check:**
    - Declare `temperature = 15`.
    - Write an `if` statement that prints "Wear a jacket." only if `temperature` is less than 20. Remember Python uses indentation, not curly braces. Run it.
    - Change `temperature` to 25 and run it again. Observe that nothing is printed.
14. **Either/Or:**
    - Declare `is_logged_in = False` (note capital 'F').
    - Write an `if/else` statement. If `is_logged_in` is `True`, print "Welcome back!". Otherwise (else), print "Please log in.".
15. **Multiple Choices:**
    - Declare `grade = 78`.
    - Write an `if/elif/else` chain (Python uses `elif` for "else if"):
      - If `grade >= 90`, print "A".
      - `elif` `grade >= 80`, print "B".
      - `elif` `grade >= 70`, print "C".
      - `else`, print "D".
    - Change the `grade` to different values (e.g., 95, 82, 60) and observe the output.
16. **Value Comparison:**
    - Declare `num_value = 10` and `str_value = "10"`.
    - Print the result of `num_value == str_value`. Observe `False`. (Python's `==` compares values but generally requires compatible types for equality unless one type knows how to compare against the other; here string and int are not considered equal).
    - Print the result of `num_value == int(str_value)`. Observe `True`.
17. **Logical AND:**
    - Declare `has_account = True` and `has_premium = False`.
    - Print the result of `has_account and has_premium`. Observe `False`.
    - Change `has_premium` to `True` and print the result again. Observe `True`. (`and` requires both sides to be true).
18. **Logical OR:**
    - Declare `is_weekend = False` and `is_holiday = True`.
    - Print the result of `is_weekend or is_holiday`. Observe `True`. (`or` requires at least one side to be true).
19. **Logical NOT:**
    - Declare `is_processing = True`.
    - Print the result of `not is_processing`. Observe `False`.
20. **Quick Decision (Conditional Expression):**
    - Declare `player_score = 45`.
    - Create a variable `result_message` using Python's conditional expression syntax: `"Win" if player_score > 50 else "Loss"`.
    - Print `result_message`. Change `player_score` to 60 and observe the change in `result_message`.

**Task Set 4: Repeating Actions (Loops)**

21. **Counting Up (range):** Write a `for` loop using `range()` that prints the numbers 0, 1, 2, 3, 4.
22. **Counting Down (range):** Write a `for` loop using `range()` that prints the numbers 5, 4, 3, 2, 1.
23. **Keep Going While...:**
    - Declare `retry_count = 3`.
    - Write a `while` loop that continues as long as `retry_count > 0`. Inside the loop, print `"Retrying..."` and decrease `retry_count` by 1 (`retry_count -= 1`).
24. **Process Items in a Sequence (List):**
    - Create a list: `colors = ["Red", "Green", "Blue"]`.
    - Use a `for` loop to iterate directly through `colors`. Inside the loop, print each `color`. (This is the Pythonic way, similar to JS `for...of`).
25. **Examine Properties of an Item (Dictionary):**
    - Create a dictionary: `car = { "make": "Toyota", "model": "Camry", "year": 2021 }`.
    - Use a `for` loop to iterate through `car`. Inside the loop, print the loop variable (e.g., `key`). Observe it prints the _keys_ ("make", "model", "year").
    - Modify the loop to iterate through `car.items()`. Inside the loop, unpack the key and value (e.g., `for key, value in car.items():`) and print both the key and its corresponding value.
26. **Skipping an Item:** Write a `for` loop using `range(1, 6)` (generates 1, 2, 3, 4, 5). Inside the loop, use an `if` statement and the `continue` keyword to skip printing the number 3.
27. **Stopping Early:** Write a `for` loop using `range(1, 6)`. Inside the loop, use an `if` statement and the `break` keyword to stop the loop entirely if the number 4 is reached. Print the numbers _before_ the loop stops.

**Task Set 5: Building Reusable Code Blocks (Functions)**

28. **Simple Greeting Function:**
    - Define a function named `show_greeting` using `def` that prints "Hello there!". Remember indentation.
    - Call the `show_greeting` function twice.
29. **Personalized Greeting:**
    - Define a function `greet_by_name` that accepts one parameter, `name`. Inside the function, use an f-string to print `f"Hello, {name}!"`.
    - Call `greet_by_name` with your name as the argument.
30. **Calculating and Returning a Value:**
    - Define a function `calculate_area` that takes `width` and `height` as parameters. Inside, it should `return` the result of `width * height`.
    - Call `calculate_area` with values like `10` and `5`. Store the returned value in a variable `area_result`. Print `area_result`.
31. **Function Scope Observation:**
    - Declare a variable `app_status = "Running"` outside any function (global scope).
    - Define a function `check_status`. Inside this function, declare a _new_ variable `internal_status = "OK"` (local scope). Print _both_ `app_status` (accessing global) and `internal_status` from _inside_ `check_status`.
    - Call `check_status()`.
    - Now, _try_ to print `internal_status` _outside_ the `check_status` function.
    - Run the code. **Observe the NameError**. This shows variables declared inside functions are typically not accessible outside (local scope). (Comment out the line causing the error to proceed).
32. **Lambda Function Syntax (Simple Anonymous Functions):**
    - Create a variable `add_lambda` and assign it a `lambda` function that takes two arguments (`x`, `y`) and returns their sum: `lambda x, y: x + y`.
    - Call `add_lambda` with values like `5` and `3` and print the result. Test it like a regular function.

**Task Set 6: Managing Collections of Data (Lists)**

33. **Create and Access:**
    - Create a list `fruits = ["Apple", "Banana", "Cherry"]`.
    - Print the element at index 1 (`Banana`) using square bracket notation `[]`.
    - Print the total number of elements in the list using the `len()` function.
34. **Adding/Removing from End:**
    - Use `fruits.append("Orange")` to add an item to the end. Print `fruits`.
    - Use `fruits.pop()` to remove and return the last item. Store the removed item in a variable `removed_fruit`. Print `removed_fruit` and the modified `fruits` list.
35. **Adding/Removing from Beginning:**
    - Use `fruits.insert(0, "Mango")` to add an item to the beginning (index 0). Print `fruits`.
    - Use `fruits.pop(0)` to remove and return the first item (index 0). Print the modified `fruits` list.
36. **Finding Items:**
    - _Try_ to find the index of "Banana" using `fruits.index("Banana")`. Print the result.
    - _Try_ to find the index of "Grape" using `fruits.index("Grape")`. **Observe the ValueError** if the item is not found. You might want to check if it exists first using the `in` operator.
    - Print the result of `"Apple" in fruits`. Observe `True`.
    - Print the result of `"Pear" in fruits`. Observe `False`.
37. **Getting a Section (Slicing):**
    - Create `numbers = [0, 1, 2, 3, 4, 5]`.
    - Create a _new_ list `sub_list` using slicing: `numbers[2:5]`. (Includes index 2, up to _but not including_ index 5).
    - Print `sub_list`.
    - Print the original `numbers` list. Observe it hasn't changed.
38. **Modifying in Place (Removing with `del` or `.remove()`):**
    - Use `del numbers[1:3]` to remove elements at index 1 and 2 using slicing with `del`. Print the modified `numbers` list.
    - Alternatively, use `numbers.remove(value)` to remove the _first occurrence_ of a specific `value`. Try removing the value `4` if it exists. Print the list.
39. **Modifying in Place (Inserting with Slicing):**
    - Reset `numbers = [0, 1, 2, 3, 4, 5]`.
    - Use slice assignment `numbers[1:1] = [8, 9]` to insert `8` and `9` at index 1 without removing anything.
    - Print the modified `numbers` list.
40. **Doing Something for Each Item (Loop):**
    - Use a standard `for` loop: `for fruit in fruits:` to print each fruit on a new line.
41. **Creating a New List Based on the Old (List Comprehension):**
    - Create `prices = [10, 20, 30]`.
    - Create `discounted_prices` using a list comprehension: `[price * 0.9 for price in prices]`.
    - Print `discounted_prices`.
42. **Creating a Filtered List (List Comprehension):**
    - Create `scores = [88, 54, 92, 71, 60]`.
    - Create `passing_scores` using a list comprehension with a condition: `[score for score in scores if score >= 70]`.
    - Print `passing_scores`.
43. **Calculating a Single Value from a List (Loop or `sum()`):**
    - Create `nums_to_sum = [1, 2, 3, 4, 5]`.
    - Calculate `total_sum` using the built-in `sum()` function: `sum(nums_to_sum)`.
    - Print `total_sum`. (For more complex reductions, you might use a loop or `functools.reduce`).

**Task Set 7: Structuring Data (Dictionaries)**

44. **Create and Access:**
    - Create a dictionary `book = { "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937 }`.
    - Print the `book['title']` using bracket notation.
    - Print the value associated with the key `'author'` using the `.get()` method: `book.get('author')`. What happens if you try `book.get('genre')` vs `book['genre']`?
45. **Adding/Modifying Properties:**
    - Add a new key-value pair: `book['genre'] = "Fantasy"`.
    - Change the value associated with the key `'year'`: `book['year'] = "Nineteen Thirty-Seven"`.
    - Print the entire `book` dictionary to see the changes.
46. **Dictionaries with Callables (Simulating Methods):**
    - Define a regular Python function `get_book_info(book_dict)` that takes a dictionary as an argument and returns a string like `f"{book_dict['title']} by {book_dict['author']}"`.
    - Call `get_book_info(book)` and print the result. (While you _can_ store functions as values in dictionaries, it's less common for simple data structures than defining standalone functions or using classes).
47. **Inspecting Dictionaries:**
    - Print the result of `book.keys()`. Observe it's a dictionary view object containing keys. Convert it to a list if needed: `list(book.keys())`.
    - Print the result of `book.values()`. Convert to a list: `list(book.values())`.
    - Print the result of `book.items()`. Observe it's a view object containing `(key, value)` tuples. Convert to a list: `list(book.items())`.

**Task Set 8: Pythonic Features & Unpacking**

48. **Extracting Dictionary Values (Unpacking in Assignment):**
    - Using the `book` dictionary, assign values to variables (less direct than JS destructuring, often done via keys):
      `title = book['title']`
      `author = book['author']`
      Print `title` and `author`.
49. **Extracting List/Tuple Elements (Unpacking):**
    - Create `coordinates = [100, 200, 50]`.
    - Extract the first two values into `x` and `y`: `x, y = coordinates[0], coordinates[1]` or more directly if you only need the first two: `x, y, _ = coordinates` (using `_` for the value you want to ignore). Print `x` and `y`.
50. **Combining Lists (Concatenation or `*` Operator):**
    - Create `list1 = ["A", "B"]` and `list2 = ["C", "D"]`.
    - Create `combined_list = list1 + list2`. Print `combined_list`.
    - Alternatively, create `combined_list_star = [*list1, *list2]`. Print `combined_list_star`.
51. **Combining Dictionaries (`update` or `**` Operator):\*\*
    - Create `settings1 = { "theme": "dark", "font_size": 12 }` and `settings2 = { "font_size": 14, "sidebar": "collapsed" }`.
    - Create `user_settings` by merging (Python 3.9+): `user_settings = settings1 | settings2`.
    - Alternatively (works in older Pythons): `user_settings = {**settings1, **settings2}`.
    - Print `user_settings`. Observe how `font_size` from `settings2` overwrites the one from `settings1`.
52. **Passing Multiple Arguments from List/Tuple (`*` Operator):**
    - Define `def log_values(val1, val2, val3): print(val1, val2, val3)`.
    - Create `values = ["One", "Two", "Three"]`.
    - Call `log_values(*values)`.
53. **Collecting Function Arguments (`*args` and `**kwargs`):\*\*
    - Define `def sum_all(*numbers): return sum(numbers)`.
    - Call `sum_all(1, 2)` and print the result.
    - Call `sum_all(10, 20, 30, 40)` and print the result. Observe how `*numbers` collects positional arguments into a tuple.
    - Define `def describe(**attributes): for key, value in attributes.items(): print(f"{key}: {value}")`.
    - Call `describe(name="Widget", color="Blue", quantity=5)`. Observe how `**attributes` collects keyword arguments into a dictionary.

**Task Set 9: Handling Unexpected Situations (Exception Handling)**

54. **Causing an Error:**
    - Declare `data = None`.
    - _Try_ to access an attribute on it: `print(data.value)`.
    - Run the code. **Observe the AttributeError** in the console. (Comment out the line causing the error to proceed).
55. **Catching an Error:**
    - Wrap the line `print(data.value)` (where `data` is `None`) inside a `try...except` block:
      ```python
      data = None
      try:
        print(data.value) # This line will cause an error
      except AttributeError as e: # Catch the specific error
        print("An error occurred!")
        print(f"Error message: {e}") # Print the specific error
      print("Program continues after error handling.")
      ```
    - Run this code. Observe that the message is printed from the `except` block, and the final "Program continues..." message also runs. Try changing `AttributeError` to `TypeError` and see what happens.
56. **Guaranteed Cleanup (Finally):**
    - Add a `finally` block to the previous `try...except`:
      ```python
      # ... (try and except blocks from above) ...
      finally:
        print("Cleanup action executed.")
      ```
    - Run it with `data = None` (causes error). Run it again with `data = {"value": "Real Data"}` (no error, but you'd access it like `data['value']` for a dictionary, or need a custom object). Observe that the `finally` block runs in _both_ cases where execution reaches the `try` block.

**Task Set 10: Dealing with Delays and Basic Asynchronicity (Conceptual)**

_(Note: True async programming with `asyncio` is more complex than basic JavaScript `setTimeout`/`Promise`. These tasks simulate delay and introduce the core `async`/`await` syntax.)_

57. **Simulating Delay (`time.sleep` - Blocking):**
    - Import the `time` module: `import time`.
    - Write `print("Message 1")`.
    - Write `time.sleep(1.5)` (waits for 1.5 seconds). Note: This _blocks_ the entire program.
    - Write `print("Message 2 (Delayed)")`.
    - Write `print("Message 3")`.
    - Run the code. Observe the order and the pause. Message 3 appears _after_ the delay.
58. **Introduction to `asyncio` (Setup):**
    - Import the `asyncio` module: `import asyncio`.
59. **Creating an Asynchronous Function (`async def`):**
    - Define an `async` function: `async def simulate_fetch(succeeds): ...`.
    - Inside the function, use `await asyncio.sleep(1)` to pause _this function's_ execution for 1 second without blocking the whole program (if run within an event loop).
    - After the sleep, use an `if succeeds:` statement. If true, `return "Data fetched successfully!"`. If false, raise an exception like `raise ValueError("Failed to fetch data.")`.
60. **Running an Async Function (Basic `asyncio.run`):**
    - Define another `async` function, e.g., `async def main(): ...`.
    - Inside `main`, use a `try...except` block.
    - Inside the `try` block, call your `simulate_fetch` using `await` and store the result: `result = await simulate_fetch(True)`. Print the `result`.
    - Inside the `except ValueError as e:` block, print the error `e`.
    - At the _end_ of your script (outside any function), run the `main` function using `asyncio.run(main())`.
61. **Handling Async Failure:**
    - Modify the call inside `main`'s `try` block to `result = await simulate_fetch(False)`.
    - Run the script again using `asyncio.run(main())`. Observe the error being caught by the `except` block.

**Mini-Project 1: Simple Counter**

62. **Setup:**
    - Declare a variable `count = 0`.
63. **Function Logic:**
    - Define a function `increment_counter`. Inside this function:
      - Use the `global` keyword to indicate you want to modify the `count` variable from the outer scope: `global count`.
      - Increment the `count` variable: `count += 1`.
      - Print the new count, perhaps using an f-string: `print(f"New count: {count}")`.
64. **Testing:**
    - Call `increment_counter()` several times directly in your script to test.

**Mini-Project 2: To-Do List Item Adder**

65. **Data Structure:** Create an empty list called `todo_items`.
66. **Adding Function:** Define a function `add_item(text)` that takes a string `text` as input. Inside the function, `append` the `text` onto the `todo_items` list.
67. **Display Function:** Define a function `display_items`. Inside this function:
    - Print a header like "--- TODO List ---".
    - Check if the list is empty (`if not todo_items:`). If so, print "(No items yet)".
    - Otherwise (else), use a `for` loop with `enumerate` to get both index and item: `for i, item in enumerate(todo_items):`. Print each item with its number (e.g., `f"{i + 1}. {item}"`).
68. **Putting it Together:**
    - Call `add_item("Learn Python")`.
    - Call `add_item("Practice Lists")`.
    - Call `display_items()`.
    - Call `add_item("Build a Project")`.
    - Call `display_items()` again to see the updated list.

---

This Python version emphasizes core data structures (lists, dictionaries), control flow, functions, Pythonic idioms like f-strings and list comprehensions, basic exception handling, and introduces the syntax for asynchronous programming with `asyncio`. Remember to run the code frequently and observe the output and any errors.
