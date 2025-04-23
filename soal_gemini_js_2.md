Okay, here are the 30 problems from your Java code, rephrased as a JavaScript-themed questionnaire without the answers. I've adapted the terminology and concepts to fit JavaScript (e.g., `ArrayList` -> `Array`, `HashMap` -> `Object` or `Map`, `method` -> `function`).

---

**JavaScript Fundamentals Questionnaire**

**--- Problem 1: Introduction to Output and Simple Loops ---**
*   **Task:** Write JavaScript code using a `for` loop to print the string "Hello JavaScript!" to the console 5 times.

**--- Problem 2: Looping with Sequential Numbers ---**
*   **Task:** Write JavaScript code using a `for` loop to display the numbers 1 through 5, each on a new line, in the console.

**--- Problem 3: Introduction to Conditionals (if/else) within a Loop ---**
*   **Task:** Loop through numbers 1 to 5. For each number, print to the console whether it's "Small" (if the number is less than or equal to 3) or "Large" (if the number is greater than 3). The output should look like: "Number 1 is Small", "Number 4 is Large", etc.

**--- Problem 4: Using Modulo and Conditionals (Even/Odd) ---**
*   **Task:** Loop through numbers 0 to 5. For each number, print to the console whether the number is "even" or "odd". The output should look like: "Number 0 is even", "Number 1 is odd", etc.

**--- Problem 5: Controlling Loop Flow (`break`) ---**
*   **Task:** Loop through numbers starting from 0 up to (but not including) 9. If the current number is even, print "Number [X] is even". If the current number is odd, print "Number [X] is odd, stopping the loop." and immediately exit the loop using `break`.

**--- Problem 6: Nested Loops - Creating a Simple Pattern ---**
*   **Task:** Using nested `for` loops, generate and print the following pattern of stars (`*`) to the console:
    ```
    *
    **
    ***
    ****
    *****
    ```

**--- Problem 7: Introduction to Functions ---**
*   **Task:** Create a JavaScript function named `greetUser` that accepts one argument (a string representing a name). When called, the function should print a greeting like "Hello there, [Name]!" to the console. Demonstrate calling it with "Budi" and "Ani".

**--- Problem 8: Functions with Return Values ---**
*   **Task:** Create a JavaScript function named `calculateRectangleArea` that accepts two arguments (representing length and width, both numbers). The function should calculate and *return* the area of the rectangle (length * width). Demonstrate calling it with length 10 and width 11 and printing the returned result.

**--- Problem 9: Introduction to Arrays and Array Iteration ---**
*   **Task:** Create a JavaScript array named `fruitList` containing the strings: "Apple", "Orange", "Mango", "Banana". Iterate through the array and print each fruit name to the console on a new line.

**--- Problem 10: Functions Processing Arrays ---**
*   **Task:** Create a JavaScript function named `printAllElements` that accepts one argument (an array). The function should iterate through the given array and print each element to the console. Demonstrate calling it with the `fruitList` array from Problem 9.

**--- Problem 11: String Indexing and Slicing ---**
*   **Task:** Given the string `message = "Hello JavaScript World"`, write JavaScript code to:
    1.  Print the first character of the string.
    2.  Print the last character of the string.
    3.  Print the substring "JavaScript".

**--- Problem 12: Basic String Methods ---**
*   **Task:** Given the string `mixed_case = "JaVaScRiPt PrOgRaMmInG"`, write JavaScript code to:
    1.  Print the string converted to all uppercase letters.
    2.  Print the string converted to all lowercase letters.
    3.  Find and print the starting index of the substring "PrOg".

**--- Problem 13: Looping Through String Characters ---**
*   **Task:** Given the string "LOOP", write JavaScript code to loop through each character of the string and print each character on a new line in the console.

**--- Problem 14: Accessing Array Elements and Length ---**
*   **Task:** Given the array `colors = ["Red", "Green", "Yellow", "Blue", "Purple"]`, write JavaScript code to:
    1.  Print the first element of the array.
    2.  Print the last element of the array.
    3.  Print the total number of elements in the array.

**--- Problem 15: Modifying Arrays (`push`) and Checking Membership (`includes`) ---**
*   **Task:**
    1.  Create a JavaScript array `planets` initialized with ["Mercury", "Venus", "Earth"].
    2.  Add "Mars" to the *end* of the `planets` array.
    3.  Print the modified `planets` array.
    4.  Check if "Jupiter" is present in the array and print the boolean result (`true`/`false`).
    5.  Check if "Earth" is present in the array and print the boolean result (`true`/`false`).

**--- Problem 16: Introduction to `while` Loops ---**
*   **Task:** Write JavaScript code using a `while` loop to print the numbers 0 through 4, each on a new line, to the console.

**--- Problem 17: `while` Loop with a Condition ---**
*   **Task:** Initialize a variable `number` to 1. Use a `while` loop to repeatedly double the value of `number` and print it to the console. The loop should stop *before* the number exceeds 50.

**--- Problem 18: Getting User Input ---**
*   **Task:** Write JavaScript code that gets a user's name as input (e.g., using `prompt` in a browser or a similar mechanism in Node.js) and then prints a personalized greeting like "Hello, [Name]!" to the console.

**--- Problem 19: Using `else if` for Multiple Conditions ---**
*   **Task:** Write JavaScript code that gets an integer as input from the user. Then, print "Positive" if the number is greater than 0, "Negative" if the number is less than 0, and "Zero" if the number is exactly 0.

**--- Problem 20: Controlling Loop Flow (`continue`) ---**
*   **Task:** Write JavaScript code that loops through numbers from 1 to 10 (inclusive). Inside the loop, use the `continue` keyword to skip printing the even numbers. Only odd numbers should be printed to the console.

**--- Problem 21: Objects (Dictionaries) - Creation and Access ---**
*   **Task:** Create a JavaScript object named `studentInfo` with the following properties (key-value pairs):
    *   `name`: "Budi"
    *   `major`: "Computer Science"
    *   `id`: 12345
    *   Print the value associated with the `name` property.
    *   Print the value associated with the `id` property.

**--- Problem 22: Objects (Dictionaries) - Iteration ---**
*   **Task:** Using the `studentInfo` object from Problem 21, write JavaScript code to:
    1.  Print all the keys of the object.
    2.  Print all the values of the object.
    3.  Print all the key-value pairs in a format like "key: value".

**--- Problem 23: Function Default Parameters ---**
*   **Task:** Create a JavaScript function `power(base, exponent)` that calculates `base` raised to the power of `exponent`. Set a default value of 2 for the `exponent` parameter, so if the function is called with only one argument, it calculates the square.
    *   Demonstrate calling it as `power(5, 3)` and print the result.
    *   Demonstrate calling it as `power(7)` and print the result.

**--- Problem 24: Representing Simple Data Structures (like Tuples) ---**
*   **Task:** Create a JavaScript object `point` to represent coordinates `x: 10` and `y: 20`.
    1.  Print the `point` object itself to the console.
    2.  Print the value of the `x` property.
    3.  Briefly explain (in a comment or conceptually) how you might prevent this object's properties from being changed after creation in JavaScript. (Hint: Think about `Object.freeze()`).

**--- Problem 25: More Array Methods (`splice`, `pop`, removing by value) ---**
*   **Task:**
    1.  Start with the array `letters = ['a', 'b', 'd', 'e']`. Print the initial array.
    2.  Insert the letter 'c' into the array at the correct position (index 2) to maintain alphabetical order. Print the array after insertion.
    3.  Remove the *last* element from the array. Print the array after removal.
    4.  Remove the element 'a' from the array *by its value*. Print the final array.

**--- Problem 26: Combining Input, Loop, Array ---**
*   **Task:** Write JavaScript code that repeatedly asks the user to enter a number or the word "done". If the user enters a number, convert it to a number type and add it to an array. If the user enters "done" (case-insensitive), stop asking for input and print the final array containing all the numbers entered.

**--- Problem 27: Function Returning a Modified Array ---**
*   **Task:** Create a JavaScript function `getEvenNumbers` that accepts an array of integers as an argument. The function should return a *new* array containing only the even numbers from the original array. Test it by calling it with `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and printing the returned result.

**--- Problem 28: Checking Data Types ---**
*   **Task:** Declare variables with the following values: `20`, `20.3`, `"Yoman"`, `[]` (an empty array), `{}` (an empty object), `true`. Write JavaScript code that prints the data type of each variable using the `typeof` operator (or other appropriate methods for more specific types like arrays/objects if needed).

**--- Problem 29: Working with Object Values ---**
*   **Task:** Given the object `scores = {"Math": 85, "Science": 92, "History": 78, "English": 88}`, write JavaScript code to calculate and print the *average* score from the values in the object.

**--- Problem 30: Putting It Together - Simple Data Processor ---**
*   **Task:** You are given an array of objects, where each object represents a product:
    ```javascript
    const products = [
        { name: "Laptop", price: 1200 },
        { name: "Mouse", price: 25 },
        { name: "Keyboard", price: 75 },
        { name: "Monitor", price: 300 }
    ];
    ```
    Create a JavaScript function `findMostExpensiveProduct(productList)` that:
    1.  Accepts the array of product objects.
    2.  Finds the product with the highest price.
    3.  Returns the *name* of the most expensive product.
    Call the function with the `products` array and print the result in the format: "The most expensive product is: [ProductName]". Handle the case of an empty input array gracefully (e.g., return `null` or an empty string).

---