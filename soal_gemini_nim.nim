**Nim Programming Problem Set (Based on Java Examples)**

**(Standard Imports often useful: `strutils`, `sequtils`, `tables`, `strformat`, `math`)**
_You may need to add `import <module_name>` at the top of your Nim file._

---

**Problem 1: Introduction to Output and Simple Loops**

- **Objective:** Learn basic output and `for` loops.
- **Task:** Write Nim code using a `for` loop to produce the following output:
  ```
  Hello Nim!
  Hello Nim!
  Hello Nim!
  Hello Nim!
  Hello Nim!
  ```
- **Tips:** Use `echo` for output and a `for` loop (e.g., `for i in 0..<5:`).

# Answer 1:
for i in countup(0,4):
    echo "Hello Nim!"

---

**Problem 2: Looping with Sequential Numbers**

- **Objective:** Use loops to generate number sequences.
- **Task:** Write Nim code using a `for` loop to display numbers 1 through 5, each on a new line.
  ```
  1
  2
  3
  4
  5
  ```
- **Tips:** Use a `for` loop with a range (e.g., `for i in 1..5:`).

# Answer 2:
for i in countup(1,5):
    echo i

---

**Problem 3: Introduction to Conditionals (`if`/`else`) within a Loop**

- **Objective:** Combine loops and conditional statements.
- **Task:** Loop from 1 to 5. For each number, print whether its "Small" (if the number is less than or equal to 3) or "Large" (if the number is greater than 3).

  Number 1 is Small
  Number 2 is Small
  Number 3 is Small
  Number 4 is Large
  Number 5 is Large

- **Tips:** Use `if`/`else` inside the loop. Use string formatting (e.g., `fmt"Number {i} is {status}"` from `strformat` or string concatenation `&`).

# Answer 3: 
for i in countup(1,5):
    var status = ""
    if (i > 3):
        status = "Large"
    else:
        status = "Small"
    echo "Number ",i, " is ", status
---

**Problem 4: Using Modulo and Conditionals (Even/Odd)**

- **Objective:** Use the modulo operator (`%` or `mod`) for divisibility checks.
- **Task:** Loop from 0 to 5. For each number, print whether it is "even" or "odd".
  ```
  Number 0 is even
  Number 1 is odd
  Number 2 is even
  Number 3 is odd
  Number 4 is even
  Number 5 is odd
  ```
- **Tips:** The modulo operator in Nim is `mod`. Check if `i mod 2 == 0`.

# Answer 4:
for i in countup(0,5):
    var status = ""
    if (i %% 2 == 0):
        status = "Even"
    else:
        status = "Odd"
    echo "Number ",i, " is ", status
---

**Problem 5: Controlling Loop Flow (`break`)**

- **Objective:** Learn how to exit a loop prematurely using `break`.
- **Task:** Loop from 0 up to (but not including) 10. If the number is even, print an "even" message. 
If the number is odd, print an "odd, stopping" message and immediately exit the loop.
  ```
  Number 0 is even
  Number 1 is odd, stopping the program
  ```
- **Tips:** Use an `if` condition to check for oddness (`i mod 2 != 0`) and use `break` to exit the `for` loop.

for i in countup(0,9):
    var status = ""
    if (i %% 2 == 0):
      status = "Even"
    else:
      status = "Odd"

    if (i == 1):
      echo "Number ",i, " is ", status, ", stopping the program"
      break
    else:
      echo "Number ",i, " is ", status


   
---

**Problem 6: Nested Loops - Creating a Simple Pattern**

- **Objective:** Understand how nested loops work to create patterns.
- **Task:** Use nested `for` loops to generate a right-angled triangle pattern of asterisks (`*`).
  ```
  *
  **
  ***
  ****
  *****
  ```
- **Tips:** The outer loop controls the rows (1 to 5). The inner loop controls the number of stars per row. You can repeat a character using the `*` operator (e.g., `"*" * count`).

import strutils

var bintang = "*"

for i in countup(1,5):
    for j in countup(1, i):
      echo bintang.repeat(i)
      break


---

**Problem 7: Introduction to Functions (Procedures in Nim)**

- **Objective:** Define and call simple procedures (`proc`).
- **Task:** Create a Nim `proc` named `greetUser` that accepts a name (string) as an argument and prints a greeting message like "Hello there, [name]". Call this procedure with the names "Budi" and "Ani".
  ```
  Hello there, Budi
  Hello there, Ani
  ```
- **Tips:** Define a procedure using `proc greetUser(name: string) =`. Call it like `greetUser("Budi")`.

---

**Problem 8: Procedures with Return Values**

- **Objective:** Define procedures that compute and return a value.
- **Task:** Create a Nim `proc` named `calculateRectangleArea` that accepts `length` and `width` (both integers) as arguments and returns their product (the area, as an integer). Call the procedure with length 10 and width 11, and print the returned result.
  ```
  110
  ```
- **Tips:** Define the procedure with a return type: `proc calculateRectangleArea(length, width: int): int =`. Use `result = length * width` or implicitly return the last expression's value.

---

**Problem 9: Introduction to Lists (Sequences in Nim) and Iteration**

- **Objective:** Create and iterate over dynamic lists (sequences).
- **Task:** Create a sequence (`seq`) named `fruitList` containing the strings "Apple", "Orange", "Mango", "Banana". Then, iterate through the sequence and print each fruit name on a new line.
  ```
  Apple
  Orange
  Mango
  Banana
  ```
- **Tips:** Initialize a sequence: `var fruitList = @["Apple", "Orange", "Mango", "Banana"]`. Iterate using `for fruit in fruitList:`.

---

**Problem 10: Procedures Processing Sequences**

- **Objective:** Write procedures that take sequences as input.
- **Task:** Create a generic Nim `proc` named `printAllElements` that accepts a sequence of any type (`seq[T]`) and prints each element of the sequence on a new line. Test it by calling it with the `fruitList` from Problem 9.
  ```
  Apple
  Orange
  Mango
  Banana
  ```
- **Tips:** Define the generic procedure: `proc printAllElements[T](listData: seq[T]) =`. Use a `for` loop inside.

---

**Problem 11: String Indexing and Slicing**

- **Objective:** Access individual characters and substrings within a string.
- **Task:** Given the string `message = "Hello Nim World"`, print:
  1.  The first character.
  2.  The last character.
  3.  The substring "Nim".
  ```
  H
  d
  Nim
  ```
- **Tips:** Access characters using `message[index]` (0-based). Get length with `message.len`. Access the last character with `message[message.len - 1]`. Use slicing `message[start..end]` (inclusive) or `message[start..<end]` (exclusive end).

---

**Problem 12: Basic String Methods (from `strutils`)**

- **Objective:** Use common string manipulation functions.
- **Task:** Given the string `mixedCase = "NiM pRoGrAmMiNg"`, print:
  1.  The string converted to uppercase.
  2.  The string converted to lowercase.
  3.  The starting index where the substring "pRoG" is found.
  ```
  NIM PROGRAMMING
  nim programming
  4
  ```
- **Tips:** Import `strutils`. Use `toUpperAscii()`, `toLowerAscii()`, and `find()`. `find()` returns -1 if the substring is not found.

---

**Problem 13: Looping Through String Characters**

- **Objective:** Iterate over the characters of a string.
- **Task:** Given the string `word = "LOOP"`, print each character on a new line.
  ```
  L
  O
  O
  P
  ```
- **Tips:** Use a `for` loop: `for c in word:`.

---

**Problem 14: Accessing Sequence Elements and Length**

- **Objective:** Get elements by index and find the size of a sequence.
- **Task:** Given the sequence `colors = @["Red", "Green", "Yellow", "Blue", "Purple"]`, print:
  1.  The first element.
  2.  The last element.
  3.  The total number of elements in the sequence.
  ```
  Red
  Purple
  5
  ```
- **Tips:** Access elements using `colors[index]` (0-based). Get the last element with `colors[colors.len - 1]` or `colors[^1]` (Nim 1.6+). Get the length with `colors.len`.

---

**Problem 15: Modifying Sequences (`add`) and Checking Membership (`in`)**

- **Objective:** Add elements to sequences and check if an element exists.
- **Task:** Create a sequence `planets` initialized with "Mercury", "Venus", "Earth". Add "Mars" to the end of the sequence. Print the final sequence. Then, check if "Jupiter" is in the sequence and print the boolean result. Finally, check if "Earth" is in the sequence and print the boolean result.
  ```
  @[Mercury, Venus, Earth, Mars]
  false
  true
  ```
- **Tips:** Initialize with `var planets = @["Mercury", "Venus", "Earth"]`. Add using `planets.add("Mars")`. Check membership using the `in` operator: `"Jupiter" in planets`. `echo` prints sequences with `@[]`.

---

**Problem 16: Introduction to `while` Loops**

- **Objective:** Use `while` loops for repetition based on a condition.
- **Task:** Use a `while` loop to print numbers from 0 up to (but not including) 5.
  ```
  0
  1
  2
  3
  4
  ```
- **Tips:** Initialize a counter variable (e.g., `var i = 0`). Use `while i < 5:`. Remember to increment the counter (`i += 1`) inside the loop.

---

**Problem 17: `while` Loop with a Condition**

- **Objective:** Use `while` loops for iterative calculations until a condition is met.
- **Task:** Start with a variable `number = 1`. Use a `while` loop to repeatedly double the `number` and print it. Stop the loop _before_ the number exceeds 50.
  ```
  1
  2
  4
  8
  16
  32
  ```
- **Tips:** The loop condition should be `while number < 50:`. Print the `number` _before_ doubling it inside the loop.

---

**Problem 18: Getting User Input**

- **Objective:** Read input from the user via the console.
- **Task:** Ask the user to enter their name and store it in a variable. Then, print a personalized greeting using the entered name.
  ```
  Enter your name: Alice
  Hello, Alice!
  ```
- **Tips:** Use `stdout.write("Enter your name: ")` to prompt without a newline. Read the input using `let name = stdin.readLine()`.

---

**Problem 19: Using `elif` for Multiple Conditions**

- **Objective:** Handle multiple exclusive conditions using `if`/`elif`/`else`.
- **Task:** Ask the user to enter an integer. Read the input, convert it to an integer, and then print whether the number is "Positive", "Negative", or "Zero".
  ```
  Enter an integer: 10
  Positive
  Enter an integer: -5
  Negative
  Enter an integer: 0
  Zero
  ```
- **Tips:** Read the input using `stdin.readLine()`. Convert the string to an integer using `parseInt()` from `strutils`. You might want to wrap the `parseInt` in a `try/except` block to handle non-integer input gracefully. Use `if num > 0: ... elif num < 0: ... else: ...`.

---

**Problem 20: Controlling Loop Flow (`continue`)**

- **Objective:** Learn how to skip the current iteration of a loop using `continue`.
- **Task:** Loop through numbers from 1 to 10 (inclusive). Print only the odd numbers. Use the `continue` statement to skip the processing for even numbers.
  ```
  1
  3
  5
  7
  9
  ```
- **Tips:** Inside the loop, use `if i mod 2 == 0: continue`. The `echo i` should come after this `if` statement.

---

**Problem 21: Dictionaries (Tables in Nim) - Creation and Access**

- **Objective:** Create and access key-value pairs using Tables.
- **Task:** Create a `Table` named `studentInfo` to store the following key-value pairs: "name" -> "Budi", "major" -> "Computer Science", "id" -> 12345. Print the entire table, then print the value associated with the key "name", and finally print the value associated with the key "id".
  ```
  {"major": "Computer Science", "name": "Budi", "id": 12345}  (Order may vary)
  Budi
  12345
  ```
- **Tips:** Import `tables`. Initialize using `var studentInfo = {"name": "Budi", "major": "Computer Science", "id": "12345"}.toTable` or add elements individually: `studentInfo["name"] = "Budi"`. Note that keys must be of the same type, and values must be of the same type. If mixing types (like string and int), you might use `JsonNode` from `json` or define a custom object/variant type. For this problem, let's assume ID is also stored as a string for simplicity with basic Tables, or use a `Table[string, JsonNode]`. _Let's adjust the task slightly for basic Tables: store ID as string "12345"._ If storing mixed types is essential, a `Table[string, JsonNode]` or `Table[string, RootObj]` approach is needed. (Revising based on Java using `Object`: let's use `Table[string, string]` and store the ID as `"12345"` for simplicity here.)

  ```nim
  import tables
  var studentInfo = initTable[string, string]() # Or JsonNode for mixed types
  studentInfo["name"] = "Budi"
  studentInfo["major"] = "Computer Science"
  studentInfo["id"] = "12345" # Storing as string for basic Table

  echo studentInfo
  echo studentInfo["name"]
  echo studentInfo["id"]
  ```

  _(Revised Expected Output based on string ID)_

  ```
  {"major": "Computer Science", "name": "Budi", "id": "12345"}
  Budi
  12345
  ```

---

**Problem 22: Tables (Dictionaries) - Iteration**

- **Objective:** Iterate over the keys, values, and key-value pairs of a Table.
- **Task:** Using the `studentInfo` Table from Problem 21, iterate and print:

  1.  All the keys, each preceded by "Key: ".
  2.  All the values, each preceded by "Value: ".
  3.  All key-value pairs in the format "Key-Value Pair: key -> value".

  ```
  Keys:
  Key: major
  Key: name
  Key: id
  (Order may vary)

  Values:
  Value: Computer Science
  Value: Budi
  Value: 12345
  (Order may vary)

  Key-Value Pairs:
  Key-Value Pair: major -> Computer Science
  Key-Value Pair: name -> Budi
  Key-Value Pair: id -> 12345
  (Order may vary)
  ```

- **Tips:** Use `for key in studentInfo.keys:`, `for value in studentInfo.values:`, and `for key, value in studentInfo.pairs:`.

---

**Problem 23: Procedure Default Arguments**

- **Objective:** Define procedures with optional parameters having default values.
- **Task:** Create a Nim `proc` named `power` that takes two integer arguments: `base` and `exponent`. The `exponent` parameter should have a default value of 2. The procedure should return `base` raised to the power of `exponent`. Call the procedure first with `base=5` and `exponent=3`, and then with just `base=7` (using the default exponent). Print both results.
  ```
  125
  49
  ```
- **Tips:** Define the procedure: `proc power(base: int, exponent: int = 2): int =`. Use `math.pow(base.float, exponent.float).int` for calculation (import `math`).

---

**Problem 24: Tuples (Immutable Structures)**

- **Objective:** Use tuples for fixed-size, potentially heterogeneous, immutable collections.
- **Task:** Create a named tuple type `Point` with integer fields `x` and `y`. Create an instance of `Point` representing (10, 20). Print the point instance itself, and then print just the `x` coordinate. Demonstrate immutability (conceptually, as Nim tuples are value types and reassignment creates a new tuple, but fields of a `var` tuple can be mutated unless it's a `let`).
  ```
  (x: 10, y: 20)
  10
  ```
- **Tips:** Define the tuple type: `type Point = tuple[x, y: int]`. Create an instance: `let point1: Point = (x: 10, y: 20)` or `let point1 = (x: 10, y: 20)`. Access fields using dot notation: `point1.x`.

---

**Problem 25: More Sequence Methods (`insert`, `delete`)**

- **Objective:** Modify sequences by inserting and removing elements at specific positions or by value.
- **Task:** Start with a sequence `letters = @['a', 'b', 'd', 'e']`.
  1.  Print the initial sequence.
  2.  Insert the character 'c' at index 2. Print the sequence.
  3.  Remove the _last_ element from the sequence. Print the sequence.
  4.  Remove the _first occurrence_ of the character 'a' from the sequence. Print the sequence.
  ```
  Initial list: @['a', 'b', 'd', 'e']
  After insert: @['a', 'b', 'c', 'd', 'e']
  After remove last: @['a', 'b', 'c', 'd']
  After remove 'a': @['b', 'c', 'd']
  ```
- **Tips:** Initialize: `var letters = @['a', 'b', 'd', 'e']`. Insert: `letters.insert('c', 2)`. Remove last: `letters.delete(letters.len - 1)` or `letters.delete(^1)` (Nim 1.6+). Remove by value: Find the index first using `letters.find('a')` and then use `letters.delete(index)` if the index is not -1.

---

**Problem 26: Combining Input, Loop, Sequence**

- **Objective:** Build a sequence dynamically based on user input within a loop.
- **Task:** Write a program that repeatedly asks the user to "Enter a number (or 'done' to finish):". If the user enters a valid integer, add it to a sequence of integers. If the user enters "done" (case-insensitive), stop asking and print the final sequence of collected numbers.
  ```
  Enter a number (or 'done' to finish): 10
  Enter a number (or 'done' to finish): 25
  Enter a number (or 'done' to finish): 8
  Enter a number (or 'done' to finish): DoNe
  Final list: @[10, 25, 8]
  ```
- **Tips:** Use a `while true:` loop. Inside, read input using `stdin.readLine()`. Check if the input (converted to lowercase using `strutils.toLowerAscii`) is equal to "done". If not "done", try to parse it into an integer using `strutils.parseInt()`. Use a `try/except ValueError:` block to handle cases where the input is not a valid integer. If parsing succeeds, add the integer to your sequence (`var numbers: seq[int] = @[]`).

---

**Problem 27: Procedure Returning a Modified Sequence**

- **Objective:** Create procedures that process a sequence and return a new, filtered sequence.
- **Task:** Create a Nim `proc` named `getEvenNumbers` that takes a sequence of integers (`seq[int]`) as input. It should return a _new_ sequence containing only the even numbers from the input sequence. Test the procedure by calling it with the sequence `@[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and printing the result.
  ```
  @[2, 4, 6, 8, 10]
  ```
- **Tips:** Define `proc getEvenNumbers(numbers: seq[int]): seq[int] =`. Inside, initialize an empty result sequence: `var evens: seq[int] = @[]`. Loop through the input `numbers`. If a number is even (`num mod 2 == 0`), add it to the `evens` sequence. Return `evens`. Alternatively, use `sequtils.filter`: `return numbers.filter(func(x: int): bool = x mod 2 == 0)` (requires `import sequtils`).

---

**Problem 28: Checking Data Types (Kind)**

- **Objective:** Determine the type or kind of a variable at runtime.
- **Task:** Create variables of different types (e.g., an integer, a float, a string, a sequence, a table, a tuple, a boolean). Use the `kind` property or `type.name` to print the type name or kind of each variable.
  ```
  Type of a: int
  Type of b: float
  Type of c: string
  Type of d: seq[int] (or similar)
  Type of e: Table[string, string] (or similar)
  Type of f: tuple[x: int, y: int] (or similar)
  Type of g: bool
  ```
  _(Note: Exact output might vary slightly based on how types are inferred or specified)_
- **Tips:** Define variables: `let a = 20`, `let b = 20.3`, `let c = "Yoman"`, `let d = @[1, 2]`, `let e = {"key": "val"}.toTable`, `let f = (x: 1, y: 2)`, `let g = true`. Print using `echo "Type of a: ", a.type.name` or `echo "Kind of a: ", a.kind`. `type.name` is usually more specific.

---

**Problem 29: Working with Table Values**

- **Objective:** Perform calculations or operations on values stored within a Table.
- **Task:** Given the Table `scores = {"Math": 85, "Science": 92, "History": 78, "English": 88}.toTable`, write Nim code to calculate and print the _average_ score.
  ```
  Average score: 85.75
  ```
- **Tips:** Import `tables`. Initialize the table: `let scores = {"Math": 85, "Science": 92, "History": 78, "English": 88}.toTable`. Get the values using `scores.values`. Calculate the sum: iterate through values or use `sum(scores.values)` (if `sequtils` is imported). Get the count using `scores.len`. Divide the sum (convert to float first if needed) by the count. Use `strformat.fmt` for formatted output.

---

**Problem 30: Putting It Together - Simple Data Processor**

- **Objective:** Combine procedures, sequences, objects (or Tables), and loops to process a small dataset.
- **Task:** You are given data representing products. A good way to represent this in Nim is using a sequence of objects.
  1.  Define an object type `Product` with fields `name: string` and `price: int`.
  2.  Create a sequence `products` containing several `Product` objects:
      - `Product(name: "Laptop", price: 1200)`
      - `Product(name: "Mouse", price: 25)`
      - `Product(name: "Keyboard", price: 75)`
      - `Product(name: "Monitor", price: 300)`
  3.  Create a procedure `findMostExpensiveProduct(productList: seq[Product]): string` that:
      - Accepts the sequence of `Product` objects.
      - Finds the product with the highest price.
      - Returns the _name_ of the most expensive product. Handle the case of an empty input list (e.g., return an empty string or raise an error).
  4.  Call the function with the `products` sequence and print the result.
  ```
  The most expensive product is: Laptop
  ```
- **Tips:** Define the object: `type Product = object; name: string; price: int`. Create the sequence: `let products = @[Product(name: "Laptop", price: 1200), ...]`. In the procedure, handle the empty list case (`if productList.len == 0: return ""`). Initialize variables `maxPrice = -1` (or `low(int)`) and `mostExpensiveName = ""`. Loop through the `productList`. In each iteration, access `product.price`. Compare with `maxPrice`. If higher, update `maxPrice` and `mostExpensiveName` (to `product.name`). Return `mostExpensiveName`.
