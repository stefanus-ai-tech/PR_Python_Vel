**PHP Programming Fundamentals Questionnaire**

---

**Problem 1: Introduction to Output and Simple Loops**

- **Objective:** Learn basic output and `for` loops in PHP.
- **Task:** Write PHP code using a `for` loop to produce the following output exactly five times, each on a new line:

```
Hello PHP!
```

- **Expected Output:**

```
Hello PHP!
Hello PHP!
Hello PHP!
Hello PHP!
Hello PHP!
```

- **PHP Tips:** Use `echo` or `print` for output. Append `PHP_EOL` (for command-line scripts) or `"<br>"` (for web
  output) to create new lines.

```php
<?php


?>
```

---

**Problem 2: Looping with Sequential Numbers**

- **Objective:** Use a `for` loop to iterate through a range of numbers.
- **Task:** Write PHP code using a `for` loop to display the numbers 1 through 5, each on a new line.
- **Expected Output:**

```
1
2
3
4
5
```

```php
<?php


?>
```

---

**Problem 3: Introduction to Conditionals (`if`/`else`) within a Loop**

- **Objective:** Combine loops and conditional statements.
- **Task:** Write PHP code that loops through numbers from 1 to 5. For each number, print whether it's "Small" (if the
  number is less than or equal to 3) or "Large" (if the number is greater than 3).
- **Expected Output:**

```
Number 1 is Small
Number 2 is Small
Number 3 is Small
Number 4 is Large
Number 5 is Large
```

- **PHP Tips:** Use an `if`/`else` statement inside the loop. You can use string concatenation (`.`) or interpolation
  (`"Number {$i} is {$status}"`) for the output.

```php
<?php


?>
```

---

**Problem 4: Using Modulo and Conditionals (Even/Odd)**

- **Objective:** Use the modulo operator (`%`) to determine even or odd numbers.
- **Task:** Write PHP code that loops through numbers from 0 to 5. For each number, print whether it is "even" or "odd".
- **Expected Output:**

```
Number 0 is even
Number 1 is odd
Number 2 is even
Number 3 is odd
Number 4 is even
Number 5 is odd
```

- **PHP Tips:** The modulo operator (`%`) gives the remainder of a division. `($number % 2 == 0)` is true if `$number`
  is even.

```php
<?php


?>
```

---

**Problem 5: Controlling Loop Flow (`break`)**

- **Objective:** Learn how to exit a loop prematurely using `break`.
- **Task:** Write PHP code that loops through numbers starting from 0. If the number is even, print that it's even. If
  the number is odd, print a message indicating it's odd and that the loop is stopping, then exit the loop immediately.
  The loop should attempt to go up to 9 if not stopped early.
- **Expected Output:**

```
Number 0 is even
Number 1 is odd, stopping the program.
```

- **PHP Tips:** Place the `break;` statement inside the conditional block where you want the loop to terminate.

```php
<?php


?>
```

---

**Problem 6: Nested Loops - Creating a Simple Pattern**

- **Objective:** Understand how nested loops work to create patterns.
- **Task:** Write PHP code using nested `for` loops to generate a right-angled triangle pattern made of asterisks (`*`),
  growing from one to five asterisks.
- **Expected Output:**

```
*
**
***
****
*****
```

- **PHP Tips:** The outer loop can control the number of rows (or the number of asterisks in the current row). The inner
  loop (or a function like `str_repeat()`) can print the asterisks for the current row.

```php
<?php


?>
```

---

**Problem 7: Introduction to Functions**

- **Objective:** Define and call simple functions in PHP.
- **Task:** Create a PHP function named `greetUser` that accepts one argument (a string representing a name) and prints
  a personalized greeting message. Then, call this function twice with the names "Budi" and "Ani".
- **Expected Output:**

```
Hello there, Budi
Hello there, Ani
```

- **PHP Tips:** Define functions using the `function` keyword: `function greetUser($name) { ... }`.

```php
<?php


?>
```

---

**Problem 8: Functions with Return Values**

- **Objective:** Create functions that perform a calculation and return a result.
- **Task:** Create a PHP function named `calculateRectangleArea` that accepts two integer arguments (length and width)
  and _returns_ the calculated area (length multiplied by width). Call the function with length 10 and width 11, and print
  the returned result.
- **Expected Output:**

```
110
```

- **PHP Tips:** Use the `return` keyword inside the function to send a value back to where the function was called.

```php
<?php


?>
```

---

**Problem 9: Introduction to Arrays (Indexed Arrays) and Array Iteration**

- **Objective:** Learn how to create and loop through indexed arrays in PHP.
- **Task:** Create a PHP array named `$fruitList` containing the strings "Apple", "Orange", "Mango", and "Banana". Then,
  write code to loop through the array and print each fruit name on a new line.
- **Expected Output:**

```
Apple
Orange
Mango
Banana
```

- **PHP Tips:** Create arrays using `['Apple', 'Orange', ...]` or `array('Apple', 'Orange', ...)`. Use a `foreach` loop
  (`foreach ($fruitList as $fruit)`) for easy iteration.

```php
<?php


?>
```

---

**Problem 10: Functions Processing Arrays**

- **Objective:** Write functions that take arrays as arguments.
- **Task:** Create a PHP function named `printAllElements` that accepts one argument (an array). The function should
  loop through the given array and print each element on a new line. Test the function by passing it the `$fruitList`
  array created in Problem 9.
- **Expected Output:**

```
Apple
Orange
Mango
Banana
```

- **PHP Tips:** PHP's dynamic typing means the function will work with arrays containing elements of various types
  without needing generics like in Java.

```php
<?php


?>
```

---

**Problem 11: String Indexing and Substrings**

- **Objective:** Access individual characters and parts of strings.
- **Task:** Given the string `$message = "Hello PHP World";`, write PHP code to:

1. Print the first character.
2. Print the last character.
3. Print the substring "PHP".

- **Expected Output:**

```
H
d
PHP
```

- **PHP Tips:** Access characters using bracket notation (e.g., `$message[0]`). Use `strlen()` to find the length for
  accessing the last character (`$message[strlen($message) - 1]`). Use `substr()` to extract substrings (`substr($string,
$start_index, $length)`).

```php
<?php


?>
```

---

**Problem 12: Basic String Methods**

- **Objective:** Use common built-in functions for string manipulation.
- **Task:** Given the string `$mixed_case = "PhP PrOgRaMmInG";`, write PHP code to:

1. Print the string converted to all uppercase letters.
2. Print the string converted to all lowercase letters.
3. Find and print the starting index (position) of the substring "PrOg".

- **Expected Output:**

```
PHP PROGRAMMING
php programming
4
```

- **PHP Tips:** Use `strtoupper()`, `strtolower()`, and `strpos()`. Note that `strpos()` returns the starting position
  (0-indexed) or `false` if the substring is not found.

```php
<?php


?>
```

---

**Problem 13: Looping Through String Characters**

- **Objective:** Iterate over the individual characters within a string.
- **Task:** Given the string `$word = "LOOP";`, write PHP code to print each character of the string on a new line.
- **Expected Output:**

```
L
O
O
P
```

- **PHP Tips:** You can use a `for` loop iterating from index 0 to `strlen($word) - 1` and access characters using
  `$word[$i]`. Alternatively, `str_split()` can convert the string to an array of characters for use with `foreach`.

```php
<?php


?>
```

---

**Problem 14: Accessing Array Elements and Length**

- **Objective:** Access specific elements of an indexed array and find its size.
- **Task:** Given the array `$colors = ["Red", "Green", "Yellow", "Blue", "Purple"];`, write PHP code to:

1. Print the first element ("Red").
2. Print the last element ("Purple").
3. Print the total number of elements in the array.

- **Expected Output:**

```
Red
Purple
5
```

- **PHP Tips:** Access elements using index (`$colors[0]`). Find the last index using `count($colors) - 1`. Use
  `count()` to get the total number of elements.

```php
<?php


?>
```

---

**Problem 15: Modifying Arrays (`array_push`) and Checking Membership (`in_array`)**

- **Objective:** Add elements to arrays and check if an element exists within an array.
- **Task:**

1. Create an indexed array `$planets` containing "Mercury", "Venus", "Earth".
2. Add "Mars" to the _end_ of the `$planets` array.
3. Print the modified `$planets` array.
4. Check if "Jupiter" is in the array and print the boolean result (`false`).
5. Check if "Earth" is in the array and print the boolean result (`true`).

- **Expected Output (boolean `false` might display as an empty string or 0 depending on context/casting, `true` as 1):**

```
Array
(
[0] => Mercury
[1] => Venus
[2] => Earth
[3] => Mars
)
bool(false)
bool(true)
```

_(Alternatively, for simpler output check)_

```
Planets: Mercury, Venus, Earth, Mars
Contains Jupiter? No
Contains Earth? Yes
```

- **PHP Tips:** Use `$planets[] = "Mars";` or `array_push($planets, "Mars");` to add to the end. Use
  `in_array('ElementName', $array)` to check for membership. Use `print_r($array);` or `var_dump($array);` to display
  array contents for debugging. Use `var_dump()` specifically to see the boolean values clearly.

```php
<?php


?>
```

---

**Problem 16: Introduction to `while` Loops**

- **Objective:** Understand the basic structure and usage of `while` loops.
- **Task:** Write PHP code using a `while` loop to print the numbers 0 through 4, each on a new line.
- **Expected Output:**

```
0
1
2
3
4
```

- **PHP Tips:** Initialize a counter variable before the loop. Specify the loop condition in the `while (...)`. Remember
  to increment the counter inside the loop to avoid an infinite loop.

---

**Problem 17: `while` Loop with a Condition**

- **Objective:** Use a `while` loop that continues as long as a specific condition is met.
- **Task:** Start with a variable `$number = 1;`. Write a `while` loop that continues as long as `$number` is less than

50. Inside the loop, print the current value of `$number`, and then double its value (`$number = $number * 2;`).

- **Expected Output:**

```
1
2
4
8
16
32
```

```php
<?php


?>
```

---

**Problem 18: Getting User Input (Command Line)**

- **Objective:** Learn how to receive input from the user in a command-line script.
- **Task:** Write a PHP script that:

1. Prompts the user to enter their name by printing "Enter your name: ".
2. Reads the name entered by the user.
3. Prints a personalized greeting like "Hello, [Name]!".

- **Example Interaction:**

```
Enter your name: Alice
Hello, Alice!
```

- **PHP Tips:** Use the `readline()` function to read a line of input from the console. Note: This works when running
  PHP scripts from the command line (e.g., `php your_script.php`), not directly in a web browser environment.

```php
<?php


?>
```

---

**Problem 19: Using `elseif` for Multiple Conditions**

- **Objective:** Handle multiple conditions using `if`/`elseif`/`else`.
- **Task:** Write a PHP script that:

1. Prompts the user to enter an integer.
2. Reads the integer input.
3. Prints "Positive" if the number is greater than 0.
4. Prints "Negative" if the number is less than 0.
5. Prints "Zero" if the number is exactly 0.

- **Example Interaction:**

```
Enter an integer: -5
Negative
```

```
Enter an integer: 10
Positive
```

```
Enter an integer: 0
Zero
```

- **PHP Tips:** Use `readline()` to get input. Convert the input to an integer using `(int)` or `intval()`. Use an `if
(...) { ... } elseif (...) { ... } else { ... }` structure. Consider adding checks for non-numeric input if making it
  more robust.

```php
<?php


?>
```

---

**Problem 20: Controlling Loop Flow (`continue`)**

- **Objective:** Learn how to skip the current iteration of a loop and proceed to the next using `continue`.
- **Task:** Write PHP code that loops through numbers from 1 to 10. Use the `continue` statement to skip the current
  iteration if the number is even. Print only the odd numbers, each on a new line.
- **Expected Output:**

```
1
3
5
7
9
```

- **PHP Tips:** Inside the loop, check if the number is even (`$i % 2 == 0`). If it is, execute `continue;` to
  immediately start the next iteration.

```php
<?php


?>
```

---

**Problem 21: Associative Arrays (Like Dictionaries/Maps) - Creation and Access**

- **Objective:** Create and access data in associative arrays (key-value pairs).
- **Task:** Create a PHP associative array named `$studentInfo` storing the following information: 'name' should be
  "Budi", 'major' should be "Computer Science", and 'id' should be 12345. Then, print the value associated with the 'name'
  key and the value associated with the 'id' key.
- **Expected Output:**

```
Budi
12345
```

- **PHP Tips:** Create associative arrays using `['key1' => 'value1', 'key2' => value2, ...]`. Access values using
  `$arrayName['keyName']`.

```php
<?php


?>
```

---

**Problem 22: Associative Arrays - Iteration**

- **Objective:** Loop through the keys, values, or key-value pairs of an associative array.
- **Task:** Using the `$studentInfo` array from Problem 21 (`['name' => "Budi", 'major' => "Computer Science", 'id' =>
12345]`), write PHP code to do the following:

1. Print "Keys:", then loop through and print only the keys of the array, each on a new line.
2. Print "Values:", then loop through and print only the values of the array, each on a new line.
3. Print "Key-Value Pairs:", then loop through and print each key and its corresponding value in the format "key:
   value", each pair on a new line.

- **Expected Output (Order of keys/pairs might vary):**

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

- **PHP Tips:** Use `foreach ($array as $key => $value)` to get both key and value. Use `foreach ($array as $value)` to
  get only values. Use `array_keys($array)` to get an array of keys, then loop through that. Use `array_values($array)`
  similarly for values.

```php
<?php


?>
```

---

**Problem 23: Function Default Argument Values**

- **Objective:** Define functions where some arguments have default values if not provided when called.
- **Task:** Create a PHP function named `power` that accepts two arguments: `$base` and `$exponent`. The `$exponent`
  should have a default value of 2. The function should return the result of `$base` raised to the power of `$exponent`.
- Call `power(5, 3)` and print the result.
- Call `power(7)` (letting the exponent default to 2) and print the result.
- **Expected Output:**

```
125
49
```

- **PHP Tips:** Define the function like `function power($base, $exponent = 2) { ... }`. You can use the `pow()`
  function or the `**` operator for exponentiation.

```php
<?php


?>
```

---

**Problem 24: Working with Structured Data (Associative Arrays/Objects)**

- **Objective:** Represent structured data (like a point with x and y coordinates) using PHP's data structures.
- **Task:** Create a PHP associative array named `$point` to represent a 2D point with an 'x' coordinate of 10 and a 'y'
  coordinate of 20.

1. Print the entire `$point` array (using `print_r` or `var_dump` is helpful here).
2. Print only the value of the 'x' coordinate.

- **Expected Output (using `print_r`):**

```
Array
(
[x] => 10
[y] => 20
)
10
```

- **PHP Tips:** While PHP doesn't have Records like Java 14+, associative arrays are commonly used for simple
  structures. Simple objects (`stdClass`) or custom classes can also be used.

```php
<?php


?>
```

---

**Problem 25: More Array Functions (`array_splice`, `array_pop`, `array_search`/`unset`)**

- **Objective:** Use functions to insert elements at specific positions, remove elements from the end, and remove
  elements by value.
- **Task:**

1. Start with the array `$letters = ['a', 'b', 'd', 'e'];`. Print the initial array.
2. Insert the letter 'c' into the array at index 2 (between 'b' and 'd'). Print the array after insertion.
3. Remove the _last_ element from the array. Print the array after removing the last element.
4. Remove the element with the _value_ 'a' from the array. Print the final array.

- **Expected Output (using `print_r` for clarity):**

```
Initial list: Array ( [0] => a [1] => b [2] => d [3] => e )
After insert: Array ( [0] => a [1] => b [2] => c [3] => d [4] => e )
After remove last: Array ( [0] => a [1] => b [2] => c [3] => d )
After remove 'a': Array ( [1] => b [2] => c [3] => d )
```

_(Note: Removing 'a' using `unset` after `array_search` keeps the original keys. Using `array_splice` would re-index.)_

- **PHP Tips:** Use `array_splice($letters, 2, 0, 'c');` to insert 'c' at index 2 without removing anything. Use
  `array_pop($letters);` to remove and return the last element. To remove by value: find the key using `$key =
array_search('a', $letters);`, then if found (`$key !== false`), remove using `unset($letters[$key]);` or
  `array_splice($letters, $key, 1);`. `array_values()` can be used after `unset` to re-index the array if needed.

```php
<?php


?>
```

---

**Problem 26: Combining Input, Loop, Array (Command Line)**

- **Objective:** Build a simple interactive program that collects user input into an array until a specific command is
  given.
- **Task:** Write a PHP command-line script that repeatedly:

1. Asks the user to "Enter a number (or 'done' to finish): ".
2. Reads the user's input.
3. If the input is "done" (case-insensitive), stop looping.
4. If the input is a number, convert it to an integer and add it to an array called `$numbers`.
5. After the loop finishes (user entered "done"), print the final `$numbers` array.

- **Example Interaction:**

```
Enter a number (or 'done' to finish): 10
Enter a number (or 'done' to finish): 25
Enter a number (or 'done' to finish): 8
Enter a number (or 'done' to finish): DoNe
Final list: Array ( [0] => 10 [1] => 25 [2] => 8 )
```

- **PHP Tips:** Use a `while(true)` loop and `break` when the condition is met. Use `readline()` for input. Use
  `strtolower()` to make the "done" check case-insensitive. Use `is_numeric()` to check if the input is a number before
  casting with `(int)` or `intval()`. Use `print_r()` to display the final array.

```php
<?php


?>
```

---

**Problem 27: Function Returning a Modified Array**

- **Objective:** Create a function that processes an array and returns a new array based on some criteria.
- **Task:** Create a PHP function named `getEvenNumbers` that takes one argument: an array of integers (`$numbers`). The
  function should create and return a _new_ array containing only the even numbers from the input array. Test the function
  by calling it with the array `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and printing the returned result.
- **Expected Output (using `print_r`):**

```
Array
(
[0] => 2
[1] => 4
[2] => 6
[3] => 8
[4] => 10
)
```

_(Note: Keys might be preserved or re-indexed depending on implementation)_

- **PHP Tips:** Inside the function, initialize an empty array (e.g., `$evenNumbers = [];`). Loop through the input
  `$numbers` array using `foreach`. If a number is even (`$number % 2 == 0`), add it to `$evenNumbers`. Return
  `$evenNumbers`. Alternatively, explore using `array_filter()` with a callback function for a more concise solution.

```php
<?php


?>
```

---

**Problem 28: Checking Data Types**

- **Objective:** Determine the data type of different PHP variables.
- **Task:** Create PHP variables with different data types: an integer, a float (decimal number), a string, an indexed
  array, an associative array, a boolean (`true` or `false`), and potentially a simple object (e.g., `new stdClass()`).
  For each variable, print its data type using a descriptive message.
- **Expected Output (Example):**

```
Type of a: integer
Type of b: double
Type of c: string
Type of d: array
Type of e: array
Type of f: boolean
Type of g: object
```

- **PHP Tips:** Use the `gettype()` function to get the data type as a string. For objects, `get_class($variable)` will
  give the class name.

```php
<?php


?>
```

---

**Problem 29: Working with Associative Array Values**

- **Objective:** Perform calculations or operations on values stored within an associative array.
- **Task:** Given the associative array `$scores = ["Math" => 85, "Science" => 92, "History" => 78, "English" => 88];`,
  write PHP code to calculate and print the _average_ score.
- **Expected Output (or close due to float precision):**

```
Average score: 85.75
```

- **PHP Tips:**

1. Get all the values using `array_values($scores)`.
2. Calculate the sum of these values using `array_sum()`.
3. Get the number of scores using `count($scores)`.
4. Divide the sum by the count to get the average. Ensure you handle potential division by zero if the array could be
   empty.

```php
<?php


?>
```

---

**Problem 30: Putting It Together - Simple Data Processor**

- **Objective:** Combine functions, arrays, associative arrays, and loops to process a small dataset.
- **Task:** You are given an array of associative arrays, where each inner array represents a product with its name and
  price:

```php
$products = [
["name" => "Laptop", "price" => 1200],
["name" => "Mouse", "price" => 25],
["name" => "Keyboard", "price" => 75],
["name" => "Monitor", "price" => 300]
];
```

Create a PHP function `find_most_expensive_product(array $product_list)` that:

1. Accepts the list (array) of product associative arrays.
2. Finds the product with the highest price.
3. Returns the _name_ (string) of the most expensive product. If the input array is empty, it should return `null` or an
   empty string.

- Call the function with the `$products` array and print the result in a user-friendly message.
- **Expected Output:**

```
The most expensive product is: Laptop
```

- **PHP Tips:**
- Inside the function, handle the empty array case first (e.g., `if (empty($product_list)) { return null; }`).
- Initialize variables to keep track of the highest price found so far (e.g., `$max_price = -1;` or `$max_price =
$product_list[0]['price'];`) and the name of that product (`$most_expensive_name = '';` or `$most_expensive_name =
$product_list[0]['name'];`).
- Loop through the `$product_list` using `foreach`. In each iteration, access the price from the current product array
  (`$product['price']`).
- Compare the current product's price with `$max_price`. If it's higher, update `$max_price` and `$most_expensive_name`.
- Return the `$most_expensive_name` after the loop finishes.

```php
<?php


?>
```

---
