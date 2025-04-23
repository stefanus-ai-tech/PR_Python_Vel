---

*JavaScript Fundamentals: A Hands-On Learning Path*

*Task Set 1: Getting Started - Displaying Info & Basic Variables*

1.  *Display a Message:* Write code to show the text "JavaScript journey begins!" in the developer console.
2.  *Store and Update Information:*
    *   Declare a variable named currentStatus using let and assign it the value "Initializing". Print currentStatus.
    *   On the next line, change the value of currentStatus to "Ready". Print currentStatus again. Observe how let allows reassignment.
3.  *Store Unchanging Information:*
    *   Declare a variable named siteName using const and assign it the value "CodeRunner". Print siteName.
    *   On the next line, try to change the value of siteName to "CodeHub".
    *   Run the code. *Observe the error* in the console. This shows that const variables cannot be reassigned after creation. (You'll need to comment out or remove the line causing the error to proceed).
4.  *Basic Data Types:*
    *   Declare userName and assign it your name (a string).
    *   Declare userAge and assign it your age (a number).
    *   Declare isSubscribed and assign it true (a boolean).
    *   Print each of these variables to the console.

*Task Set 2: Working with Numbers & Text*

5.  *Calculations:*
    *   Declare price = 50 and quantity = 3.
    *   Calculate the totalCost by multiplying price and quantity. Print totalCost.
    *   Declare discount = 10. Calculate the finalCost by subtracting discount from totalCost. Print finalCost.
6.  *Leftovers:*
    *   Declare items = 17 and itemsPerBox = 5.
    *   Calculate how many items will be leftover using the modulo operator (%). Print leftover.
7.  *Combining Text:*
    *   Use the userName and userAge variables from Task 4.
    *   Create a userInfo string using *template literals* (backticks `` ` `) like this: `"User: [userName], Age: [userAge]". Print userInfo.
8.  *Text & Numbers - Observation 1:*
    *   Print the result of "Score: " + 95. Observe how the number is automatically converted to a string for concatenation.
9.  *Text & Numbers - Observation 2:*
    *   Print the result of "100" - 10. Observe how the string "100" is treated as a number in this context.
10. *Incrementing:*
    *   Declare clickCount = 0.
    *   Use the ++ operator after the variable (clickCount++) and print the result on the same line.
    *   On the next line, print clickCount itself. Notice the difference (post-increment).
    *   Reset clickCount = 0.
    *   Use the ++ operator before the variable (++clickCount) and print the result. Notice the difference (pre-increment).

*Task Set 3: Making Decisions*

11. *Simple Check:*
    *   Declare temperature = 15.
    *   Write an if statement that prints "Wear a jacket." only if temperature is less than 20. Run it.
    *   Change temperature to 25 and run it again. Observe that nothing is printed.
12. *Either/Or:*
    *   Declare isLoggedIn = false.
    *   Write an if/else statement. If isLoggedIn is true, print "Welcome back!". Otherwise (else), print "Please log in.".
13. *Multiple Choices:*
    *   Declare grade = 78.
    *   Write an if/else if/else chain:
        *   If grade >= 90, print "A".
        *   Else if grade >= 80, print "B".
        *   Else if grade >= 70, print "C".
        *   Else, print "D".
    *   Change the grade to different values (e.g., 95, 82, 60) and observe the output.
14. *Strict vs. Loose Comparison - Observation:*
    *   Declare numValue = 10 and stringValue = "10".
    *   Print the result of numValue == stringValue. Observe true.
    *   Print the result of numValue === stringValue. Observe false. This shows === checks type and value.
15. *Logical AND:*
    *   Declare hasAccount = true and hasPremium = false.
    *   Print the result of hasAccount && hasPremium. Observe false.
    *   Change hasPremium to true and print the result again. Observe true. (&& requires both sides to be true).
16. *Logical OR:*
    *   Declare isWeekend = false and isHoliday = true.
    *   Print the result of isWeekend || isHoliday. Observe true. (|| requires at least one side to be true).
17. *Logical NOT:*
    *   Declare isProcessing = true.
    *   Print the result of !isProcessing. Observe false.
18. *Quick Decision (Ternary):*
    *   Declare playerScore = 45.
    *   Create a variable resultMessage using the ternary operator: playerScore > 50 ? "Win" : "Loss".
    *   Print resultMessage. Change playerScore to 60 and observe the change in resultMessage.

*Task Set 4: Repeating Actions*

19. *Counting Up:* Write a for loop that prints the numbers 0, 1, 2, 3, 4.
20. *Counting Down:* Write a for loop that prints the numbers 5, 4, 3, 2, 1.
21. *Keep Going While...:*
    *   Declare retryCount = 3.
    *   Write a while loop that continues as long as retryCount > 0. Inside the loop, print "Retrying..." and decrease retryCount by 1 (retryCount--).
22. *Process Items in a List (Array):*
    *   Create an array: colors = ["Red", "Green", "Blue"].
    *   Use a for...of loop to iterate through colors. Inside the loop, print each color. Observe that it prints the values.
23. *Examine Properties of an Item (Object):*
    *   Create an object: car = { make: "Toyota", model: "Camry", year: 2021 }.
    *   Use a for...in loop to iterate through car. Inside the loop, print the loop variable (e.g., propName). Observe it prints the keys ("make", "model", "year").
    *   Modify the for...in loop to print both the property name and its corresponding value using car[propName].
24. *Skipping an Item:* Write a for loop from 1 to 5. Inside the loop, use an if statement and the continue keyword to skip printing the number 3.
25. *Stopping Early:* Write a for loop from 1 to 5. Inside the loop, use an if statement and the break keyword to stop the loop entirely if the number 4 is reached. Print the numbers before the loop stops.

*Task Set 5: Building Reusable Code Blocks (Functions)*

26. *Simple Greeting Function:*
    *   Define a function named showGreeting that prints "Hello there!".
    *   Call the showGreeting function twice.
27. *Personalized Greeting:*
    *   Define a function greetByName that accepts one parameter, name. Inside the function, print Hello, ${name}!.
    *   Call greetByName with your name as the argument.
28. *Calculating and Returning a Value:*
    *   Define a function calculateArea that takes width and height as parameters. Inside, it should return the result of width * height.
    *   Call calculateArea with values like 10 and 5. Store the returned value in a variable areaResult. Print areaResult.
29. *Function Scope Observation:*
    *   Declare a variable appStatus = "Running" outside any function.
    *   Define a function checkStatus. Inside this function, declare a new variable internalStatus = "OK" using let. Print both appStatus and internalStatus from inside checkStatus.
    *   Call checkStatus().
    *   Now, try to print internalStatus outside the checkStatus function.
    *   Run the code. *Observe the error* in the console (ReferenceError). This shows variables declared inside functions are typically not accessible outside. (Comment out the line causing the error to proceed).
30. *Arrow Function Syntax:*
    *   Rewrite the calculateArea function from Task 28 using arrow function syntax: const calculateAreaArrow = (width, height) => { return width * height; };. Test it by calling it and printing the result.
31. *Concise Arrow Function:*
    *   If an arrow function only calculates and returns a single expression, you can make it shorter. Rewrite calculateAreaArrow like this: const calculateAreaConcise = (width, height) => width * height;. Test it.

*Task Set 6: Managing Collections of Data (Arrays)*

32. *Create and Access:*
    *   Create an array fruits = ["Apple", "Banana", "Cherry"].
    *   Print the element at index 1 (Banana).
    *   Print the total number of elements in the array using the .length property.
33. *Adding/Removing from End:*
    *   Use fruits.push("Orange") to add an item to the end. Print fruits.
    *   Use fruits.pop() to remove the last item. Store the removed item in a variable removedFruit. Print removedFruit and the modified fruits array.
34. *Adding/Removing from Beginning:*
    *   Use fruits.unshift("Mango") to add an item to the beginning. Print fruits.
    *   Use fruits.shift() to remove the first item. Print the modified fruits array.
35. *Finding Items:*
    *   Print the result of fruits.indexOf("Banana").
    *   Print the result of fruits.indexOf("Grape"). Observe the result (-1) when an item is not found.
    *   Print the result of fruits.includes("Apple"). Observe true.
    *   Print the result of fruits.includes("Pear"). Observe false.
36. *Getting a Section (Slice):*
    *   Create numbers = [0, 1, 2, 3, 4, 5].
    *   Create a new array subArray using numbers.slice(2, 5).
    *   Print subArray.
    *   Print the original numbers array. Observe it hasn't changed.
37. *Modifying in Place (Splice - Remove):*
    *   Use numbers.splice(1, 2) to remove 2 elements starting from index 1.
    *   Print the modified numbers array.
38. *Modifying in Place (Splice - Add):*
    *   Use numbers.splice(1, 0, 8, 9) to insert 8 and 9 at index 1 without removing anything.
    *   Print the modified numbers array.
39. *Doing Something for Each Item (forEach):*
    *   Use fruits.forEach((fruit) => { console.log(fruit); }); to print each fruit.
40. *Creating a New Array Based on the Old (map):*
    *   Create prices = [10, 20, 30].
    *   Create discountedPrices using prices.map((price) => price * 0.9);.
    *   Print discountedPrices.
41. *Creating a Filtered Array (filter):*
    *   Create scores = [88, 54, 92, 71, 60].
    *   Create passingScores using scores.filter((score) => score >= 70);.
    *   Print passingScores.
42. *Calculating a Single Value from an Array (reduce):*
    *   Create numsToSum = [1, 2, 3, 4, 5].
    *   Calculate totalSum using numsToSum.reduce((accumulator, currentVal) => accumulator + currentVal, 0);. (The 0 is the starting value for the accumulator).
    *   Print totalSum.

*Task Set 7: Structuring Data (Objects)*

43. *Create and Access:*
    *   Create an object book = { title: "The Hobbit", author: "J.R.R. Tolkien", year: 1937 }.
    *   Print the book.title using dot notation.
    *   Print the book['author'] using bracket notation.
44. *Adding/Modifying Properties:*
    *   Add a new property book.genre = "Fantasy".
    *   Change the book.year to "Nineteen Thirty-Seven".
    *   Print the entire book object to see the changes.
45. *Objects with Actions (Methods):*
    *   Add a method (a function property) to the book object: getInfo: function() { return this.title + " by " + this.author; }. (Note the use of this).
    *   Call the method using book.getInfo() and print the returned string.
46. *Inspecting Objects:*
    *   Print the result of Object.keys(book). Observe it's an array of property names.
    *   Print the result of Object.values(book). Observe it's an array of property values.
    *   Print the result of Object.entries(book). Observe it's an array of [key, value] pairs.

*Task Set 8: Modern JavaScript Power-ups (ES6+)*

47. *Extracting Object Properties (Destructuring):*
    *   Using the book object, declare variables title and author directly using destructuring: const { title, author } = book;. Print title and author.
48. *Extracting Array Elements (Destructuring):*
    *   Create coordinates = [100, 200, 50].
    *   Extract the first two values into x and y: const [x, y] = coordinates;. Print x and y.
49. *Combining Arrays (Spread Operator):*
    *   Create list1 = ["A", "B"] and list2 = ["C", "D"].
    *   Create combinedList = [...list1, ...list2]. Print combinedList.
50. *Combining Objects (Spread Operator):*
    *   Create settings1 = { theme: "dark", fontSize: 12 } and settings2 = { fontSize: 14, sidebar: "collapsed" }.
    *   Create userSettings = { ...settings1, ...settings2 }. Print userSettings. Observe how fontSize from settings2 overwrites the one from settings1.
51. *Passing Multiple Arguments from Array (Spread):*
    *   Define function logValues(val1, val2, val3) { console.log(val1, val2, val3); }.
    *   Create values = ["One", "Two", "Three"].
    *   Call logValues(...values).
52. *Collecting Function Arguments (Rest Parameter):*
    *   Define function sumAll(...numbers) { return numbers.reduce((sum, num) => sum + num, 0); }.
    *   Call sumAll(1, 2) and print the result.
    *   Call sumAll(10, 20, 30, 40) and print the result. Observe how ...numbers collects all arguments into an array.

*Task Set 9: Handling Unexpected Situations (Error Handling)*

53. *Causing an Error:*
    *   Declare data = null;.
    *   Try to access a property on it: console.log(data.value);.
    *   Run the code. *Observe the TypeError* in the console. (Comment out the line causing the error to proceed).
54. *Catching an Error:*
    *   Wrap the line console.log(data.value); (where data is null) inside a try...catch block:
        javascript
        let data = null;
        try {
          console.log(data.value); // This line will cause an error
        } catch (error) {
          console.log("An error occurred!");
          console.log("Error message:", error.message); // Print the specific error
        }
        console.log("Program continues after error handling.");
        
    *   Run this code. Observe that the error message is printed from the catch block, and the final "Program continues..." message also runs.
55. *Guaranteed Cleanup (Finally):*
    *   Add a finally block to the previous try...catch:
        javascript
        // ... (try and catch blocks from above) ...
        finally {
          console.log("Cleanup action executed.");
        }
        
    *   Run it with data = null (causes error). Run it again with data = { value: "Real Data" } (no error). Observe that the finally block runs in both cases.

*Task Set 10: Dealing with Delays (Asynchronous JavaScript)*

56. *Simulating Delay (setTimeout):*
    *   Write console.log("Message 1");.
    *   Write setTimeout(() => { console.log("Message 2 (Delayed)"); }, 1500); (1500 milliseconds = 1.5 seconds).
    *   Write console.log("Message 3");.
    *   Run the code. Observe the order in which the messages appear in the console. Notice "Message 3" appears before "Message 2".
57. *Creating a Promise (Simulating Success/Failure):*
    *   Define a function simulateFetch(succeeds) that returns a new Promise((resolve, reject) => { ... });.
    *   Inside the promise executor, use setTimeout(() => { ... }, 1000);.
    *   Inside the setTimeout, use an if (succeeds) statement. If true, call resolve("Data fetched successfully!"). If false, call reject("Failed to fetch data.").
58. *Using a Promise (Handling Success):*
    *   Call simulateFetch(true) (make it succeed).
    *   Chain .then((message) => { console.log("Success:", message); }).
    *   Run it and observe the success message after about 1 second.
59. *Using a Promise (Handling Failure):*
    *   Call simulateFetch(false) (make it fail).
    *   Chain .catch((error) => { console.log("Error:", error); }).
    *   Run it and observe the error message after about 1 second.
60. *Cleaner Async Code (Async/Await - Prep):*
    *   Define an async function: async function fetchDataAndProcess() { ... }.
61. *Cleaner Async Code (Async/Await - Try/Catch):*
    *   Inside fetchDataAndProcess, write a try...catch block.
    *   Inside the try block, call await simulateFetch(true) and store the result in a variable result: const result = await simulateFetch(true);. Then print console.log("Result:", result);.
    *   Inside the catch block, catch the error and print console.log("Caught error:", error);.
    *   Call the fetchDataAndProcess() function. Run it.
    *   Modify the call inside try to await simulateFetch(false) and run it again. Observe how async/await with try/catch handles both success and failure neatly.

*Mini-Project 1: Simple Counter*

62. *HTML Setup (Optional, or just imagine):* Imagine you have an HTML button and a paragraph (<p>) to display a count.
63. *JavaScript Logic:*
    *   Declare a variable count = 0.
    *   Get references to the button and paragraph elements (if doing HTML, otherwise skip).
    *   Define a function incrementCounter. Inside this function:
        *   Increment the count variable.
        *   Update the display (e.g., paragraphElement.textContent = count; or just console.log("New count:", count);).
    *   Add an event listener to the button (if doing HTML) to call incrementCounter on click, OR just call incrementCounter() several times directly in your script to test.

*Mini-Project 2: To-Do List Item Adder*

64. *Data Structure:* Create an empty array called todoItems.
65. *Adding Function:* Define a function addItem(text) that takes a string text as input. Inside the function, push the text onto the todoItems array.
66. *Display Function:* Define a function displayItems. Inside this function:
    *   Clear the current display (e.g., console.clear() or clear an HTML list).
    *   Use todoItems.forEach(...) to loop through the array. For each item, print it to the console (or add it to an HTML list).
67. *Putting it Together:*
    *   Call addItem("Learn JavaScript").
    *   Call addItem("Practice Arrays").
    *   Call displayItems().
    *   Call addItem("Build a Project").
    *   Call displayItems() again to see the updated list.

---

This hands-on approach requires you to actively write and run code. Pay close attention to the console output, especially when things don't work as expected (errors are learning opportunities!). This should build your foundational understanding through direct experience.
