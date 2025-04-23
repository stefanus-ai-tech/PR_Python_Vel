import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List; // Using List interface is good practice
import java.util.Map;
import java.util.Scanner; // For user input

public class soal_gemini_java_ans{

    public static void main(String[] args) {
        System.out.println("--- Problem 1 ---");
        solveProblem1();
        System.out.println("\n--- Problem 2 ---");
        solveProblem2();
        System.out.println("\n--- Problem 3 ---");
        solveProblem3();
        System.out.println("\n--- Problem 4 ---");
        solveProblem4();
        System.out.println("\n--- Problem 5 ---");
        solveProblem5();
        System.out.println("\n--- Problem 6 ---");
        solveProblem6();
        System.out.println("\n--- Problem 7 ---");
        solveProblem7();
        System.out.println("\n--- Problem 8 ---");
        solveProblem8();
        System.out.println("\n--- Problem 9 ---");
        solveProblem9();
        System.out.println("\n--- Problem 10 ---");
        solveProblem10();
        System.out.println("\n--- Problem 11 ---");
        solveProblem11();
        System.out.println("\n--- Problem 12 ---");
        solveProblem12();
        System.out.println("\n--- Problem 13 ---");
        solveProblem13();
        System.out.println("\n--- Problem 14 ---");
        solveProblem14();
        System.out.println("\n--- Problem 15 ---");
        solveProblem15();
        System.out.println("\n--- Problem 16 ---");
        solveProblem16();
        System.out.println("\n--- Problem 17 ---");
        solveProblem17();
        System.out.println("\n--- Problem 18 ---");
        solveProblem18();
        System.out.println("\n--- Problem 19 ---");
        solveProblem19();
        System.out.println("\n--- Problem 20 ---");
        solveProblem20();
        System.out.println("\n--- Problem 21 ---");
        solveProblem21();
        System.out.println("\n--- Problem 22 ---");
        solveProblem22();
        System.out.println("\n--- Problem 23 ---");
        solveProblem23();
        System.out.println("\n--- Problem 24 ---");
        solveProblem24();
        System.out.println("\n--- Problem 25 ---");
        solveProblem25();
        System.out.println("\n--- Problem 26 ---");
        solveProblem26();
        System.out.println("\n--- Problem 27 ---");
        solveProblem27();
        System.out.println("\n--- Problem 28 ---");
        solveProblem28();
        System.out.println("\n--- Problem 29 ---");
        solveProblem29();
        System.out.println("\n--- Problem 30 ---");
        solveProblem30();
    }

    // Scanner for user input (shared across methods needing it)
    // Using try-with-resources in methods that use it, or closing it in main is better practice
    // For simplicity here, we'll create it as needed, but be mindful of resource leaks in real apps.

    // --- Problem 1: Introduction to Output and Simple Loops ---
    /**
     * Task: Write Java code using a for loop to produce the following output:
     * Hello Java!
     * Hello Java!
     * Hello Java!
     * Hello Java!
     * Hello Java!        
     */
    public static void solveProblem1() {
        for (int i = 0;i<5;i++){
            System.out.println("Hello Java!");
        }
    }

    // --- Problem 2: Looping with Sequential Numbers ---
    /**
     * Task: Write Java code using a for loop to display numbers 1 through 5.
     * 1
     * 2
     * 3
     * 4
     * 5
     */
    public static void solveProblem2() {
        // Standard Java for loop from 1 up to and including 5
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }
    }

    // --- Problem 3: Introduction to Conditionals (if/else) within a Loop ---
    /**
     * Task: Loop 1 to 5. Print "Small" (<= 3) or "Large" (> 3).
     * Number 1 is Small
     * Number 2 is Small
     * Number 3 is Small
     * Number 4 is Large
     * Number 5 is Large
     */
    public static void solveProblem3() {
        for (int number = 1; number <= 5; number++) {
            if (number <= 3) {
                System.out.printf("Number %d is Small%n", number); // printf for formatted output, %n for newline
            } else {
                System.out.printf("Number %d is Large%n", number);
            }
        }
    }

    // --- Problem 4: Using Modulo and Conditionals (Even/Odd) ---
    /**
     * Task: Loop 0 to 5. Print if even or odd.
     * Number 0 is even
     * Number 1 is odd
     * ...
     * Number 5 is odd
     */
    public static void solveProblem4() {
        for (int number = 0; number <= 5; number++) {
            if (number % 2 == 0) {
                System.out.printf("Number %d is even%n", number);
            } else {
                System.out.printf("Number %d is odd%n", number);
            }
        }
    }

    // --- Problem 5: Controlling Loop Flow (break) ---
    /**
     * Task: Loop 0 to 9. If odd, print stopping message and exit loop. If even, print even message.
     * Number 0 is even
     * Number 1 is odd, stopping the program.
     */
    public static void solveProblem5() {
        for (int number = 0; number <= 9; number++) {
            if (number % 2 != 0) { // Check if odd
                System.out.printf("Number %d is odd, stopping the program.%n", number);
                break; // Exit the loop
            } else {
                System.out.printf("Number %d is even%n", number);
            }
        }
    }

    // --- Problem 6: Nested Loops - Creating a Simple Pattern ---
    /**
     * Task: Generate a right-angled triangle pattern of stars.
     * *
     * **
     * ***
     * ****
     * *****
     */
    public static void solveProblem6() {
        int numRows = 5;
        for (int i = 1; i <= numRows; i++) { // Outer loop for rows
            for (int j = 1; j <= i; j++) { // Inner loop for stars in the current row
                System.out.print("*"); // Print star without newline
            }
            System.out.println(); // Move to the next line after printing stars for the row
        }
        // Alternative using String repetition (Java 11+)
        System.out.println("\nAlternative (Java 11+):");
        for (int i = 1; i <= numRows; i++) {
            System.out.println("*".repeat(i));
        }

    }

    // --- Problem 7: Introduction to Functions (Methods in Java) ---
    /**
     * Task: Create a method `greetUser` that accepts a name (String) and prints a greeting.
     * Example calls: greetUser("Budi"), greetUser("Ani")
     */
    public static void greetUser(String name) {
        System.out.printf("Hello, %s! Welcome!%n", name);
    }

    public static void solveProblem7() {
        greetUser("Budi");
        greetUser("Ani");
    }

    // --- Problem 8: Functions with Return Values ---
    /**
     * Task: Create a method `calculateRectangleArea` that accepts length and width (int) and returns the area (int).
     * Example calls shown in solveProblem8.
     */
    public static int calculateRectangleArea(int length, int width) {
        return length * width;
    }

    public static void solveProblem8() {
        int plotLength = 10;
        int plotWidth = 5;
        int plotArea = calculateRectangleArea(plotLength, plotWidth);
        System.out.printf("The area of the plot is: %d%n", plotArea); // Output: 50

        System.out.println(calculateRectangleArea(8, 3)); // Output: 24
    }

    // --- Problem 9: Introduction to Lists (ArrayList) and List Iteration ---
    /**
     * Task: Create an ArrayList `fruitList` and print each fruit.
     * Apple
     * Orange
     * Mango
     * Banana
     */
    public static void solveProblem9() {
        // Create and initialize an ArrayList
        // Using List interface on the left is good practice
        List<String> fruitList = new ArrayList<>(Arrays.asList("Apple", "Orange", "Mango", "Banana"));

        // Iterate using an enhanced for loop (for-each)
        for (String fruit : fruitList) {
            System.out.println(fruit);
        }
    }

    // --- Problem 10: Functions Processing Lists ---
    /**
     * Task: Create a method `printAllElements` that accepts a List and prints its elements.
     * Example calls shown in solveProblem10.
     */
    // Using generics <T> makes the method reusable for lists of any type
    public static <T> void printAllElements(List<T> listData) {
        for (T element : listData) {
            System.out.println(element);
        }
    }
    /*
     * // Alternative without generics (less flexible, requires specific types)
     * public static void printAllIntegers(List<Integer> listData) { ... }
     * public static void printAllStrings(List<String> listData) { ... }
     */

    public static void solveProblem10() {
        List<Integer> numbers = new ArrayList<>(Arrays.asList(10, 20, 30));
        List<String> names = new ArrayList<>(Arrays.asList("Adi", "Bima", "Citra"));

        System.out.println("Printing numbers:");
        printAllElements(numbers);

        System.out.println("\nPrinting names:");
        printAllElements(names);
    }

    // --- Problem 11: String Indexing and Slicing ---
    /**
     * Task: Given message = "Hello Python World", print first char, last char, "Python" substring.
     * H
     * d
     * Python
     */
     public static void solveProblem11() {
        String message = "Hello Python World";

        // 1. Print the first character (index 0)
        System.out.println(message.charAt(0));

        // 2. Print the last character (index length - 1)
        System.out.println(message.charAt(message.length() - 1));

        // 3. Print the substring "Python" (indices 6 through 11, end index is exclusive)
        System.out.println(message.substring(6, 12));
     }

    // --- Problem 12: Basic String Methods ---
    /**
     * Task: Given mixed_case = "PyThOn PrOgRaMmInG", print uppercase, lowercase, find index of "PrOg".
     * PYTHON PROGRAMMING
     * python programming
     * 7
     */
     public static void solveProblem12() {
        String mixedCase = "PyThOn PrOgRaMmInG";

        // 1. Uppercase
        System.out.println(mixedCase.toUpperCase());

        // 2. Lowercase
        System.out.println(mixedCase.toLowerCase());

        // 3. Find substring index (returns -1 if not found)
        System.out.println(mixedCase.indexOf("PrOg"));
     }

    // --- Problem 13: Looping Through String Characters ---
    /**
     * Task: Print each character of "LOOP" on a new line.
     * L
     * O
     * O
     * P
     */
     public static void solveProblem13() {
        String word = "LOOP";

        // Iterate using enhanced for loop over the character array
        for (char character : word.toCharArray()) {
            System.out.println(character);
        }
         // Alternative: traditional for loop
         // for (int i = 0; i < word.length(); i++) {
         //     System.out.println(word.charAt(i));
         // }
     }

    // --- Problem 14: Accessing List Elements and Length ---
    /**
     * Task: Given colors = ["Red", ...], print first, last, and total number.
     * Red
     * Purple
     * 5
     */
    public static void solveProblem14() {
        List<String> colors = new ArrayList<>(Arrays.asList("Red", "Green", "Blue", "Yellow", "Purple"));

        // 1. First color (index 0)
        System.out.println(colors.get(0));

        // 2. Last color (index size - 1)
        System.out.println(colors.get(colors.size() - 1));

        // 3. Total number of colors (size)
        System.out.println(colors.size());
    }

    // --- Problem 15: Modifying Lists (add) and Checking Membership (contains) ---
    /**
     * Task: Create planets list, add "Mars", print, check membership of "Jupiter" and "Earth".
     * [Mercury, Venus, Earth, Mars]
     * false
     * true
     */
     public static void solveProblem15() {
        // 1. Create the list
        List<String> planets = new ArrayList<>(Arrays.asList("Mercury", "Venus", "Earth"));

        // 2. Add "Mars" (append equivalent)
        planets.add("Mars");

        // 3. Print the updated list (ArrayList's toString() gives nice output)
        System.out.println(planets);

        // 4. Check for "Jupiter" (in equivalent)
        System.out.println(planets.contains("Jupiter"));

        // 5. Check for "Earth"
        System.out.println(planets.contains("Earth"));
     }

    // --- Problem 16: Introduction to `while` Loops ---
    /**
     * Task: Use a while loop to print numbers 0 through 4.
     * 0
     * 1
     * 2
     * 3
     * 4
     */
    public static void solveProblem16() {
        int count = 0;
        while (count < 5) { // Condition: count is less than 5
            System.out.println(count);
            count++; // Increment the counter (equivalent to count = count + 1)
        }
    }

    // --- Problem 17: `while` Loop with a Condition ---
    /**
     * Task: Start with number = 1. While loop to double and print, stop before exceeding 50.
     * 1
     * 2
     * 4
     * 8
     * 16
     * 32
     */
    public static void solveProblem17() {
        int number = 1;
        while (number <= 50) { // Check the condition *before* printing/doubling for this iteration
            System.out.println(number);
            number *= 2; // Double the number for the next potential iteration
        }
         // Alternative logic (print first, then check if next step is too big)
         /*
         System.out.println("\nAlternative Logic:");
         number = 1;
         while (true) {
             System.out.println(number);
             if (number * 2 > 50) {
                 break;
             }
             number *= 2;
         }
         */
    }

    // --- Problem 18: Getting User Input ---
    /**
     * Task: Ask user for name, print personalized greeting.
     * Enter your name: Alice
     * Hello, Alice!
     */
     public static void solveProblem18() {
         // Use try-with-resources to ensure the Scanner is closed automatically
         try (Scanner scanner = new Scanner(System.in)) {
             // 1. Ask for name
             System.out.print("Enter your name: "); // Use print to keep cursor on the same line

             // 2. Store input
             String userName = scanner.nextLine(); // Read the whole line of text

             // 3. Print greeting
             System.out.printf("Hello, %s!%n", userName);
         } // Scanner is automatically closed here
     }

    // --- Problem 19: Using `else if` for Multiple Conditions ---
    /**
     * Task: Ask user for integer, print "Positive", "Negative", or "Zero".
     * Enter an integer: 10
     * Positive
     */
    public static void solveProblem19() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter an integer: ");
            try {
                // 2. Read input and convert to integer
                int number = Integer.parseInt(scanner.nextLine()); // Read line then parse

                // 3, 4, 5. Check the number
                if (number > 0) {
                    System.out.println("Positive");
                } else if (number < 0) {
                    System.out.println("Negative");
                } else {
                    System.out.println("Zero");
                }
            } catch (NumberFormatException e) {
                // Handle cases where input is not a valid integer
                System.out.println("Invalid input. Please enter an integer.");
            }
        }
    }

    // --- Problem 20: Controlling Loop Flow (`continue`) ---
    /**
     * Task: Loop 1 to 10. Print only odd numbers using `continue` to skip evens.
     * 1
     * 3
     * 5
     * 7
     * 9
     */
    public static void solveProblem20() {
        for (int number = 1; number <= 10; number++) {
            if (number % 2 == 0) { // Check if the number is even
                continue; // Skip the rest of this iteration
            }
            // This line is reached only if the number is odd
            System.out.println(number);
        }
    }

    // --- Problem 21: Dictionaries (HashMap) - Creation and Access ---
    /**
     * Task: Create a Map `studentInfo` (name, major, id) and print name and ID.
     * Budi
     * 12345
     */
     public static void solveProblem21() {
        // 1. Create the HashMap
        // Using Map interface on the left. Need to specify key and value types.
        // Using Object for value type allows mixing String and Integer.
        Map<String, Object> studentInfo = new HashMap<>();
        studentInfo.put("name", "Budi");
        studentInfo.put("major", "Computer Science");
        studentInfo.put("id", 12345); // Autoboxing converts int to Integer

        // 2. Print the name (value associated with key "name")
        System.out.println(studentInfo.get("name"));

        // 3. Print the ID
        System.out.println(studentInfo.get("id"));
     }

    // --- Problem 22: Dictionaries (HashMap) - Iteration ---
    /**
     * Task: Iterate through keys, values, and key-value pairs of studentInfo.
     * Keys:
     * id
     * name
     * major
     *
     * Values:
     * 12345
     * Budi
     * Computer Science
     *
     * Key-Value Pairs:
     * id: 12345
     * name: Budi
     * major: Computer Science
     * (Order in HashMap is not guaranteed)
     */
     public static void solveProblem22() {
         Map<String, Object> studentInfo = new HashMap<>();
         studentInfo.put("name", "Budi");
         studentInfo.put("major", "Computer Science");
         studentInfo.put("id", 12345);

         // 1. Print keys
         System.out.println("Keys:");
         for (String key : studentInfo.keySet()) { // Iterate over the set of keys
             System.out.println(key);
         }

         // 2. Print values
         System.out.println("\nValues:");
         for (Object value : studentInfo.values()) { // Iterate over the collection of values
             System.out.println(value);
         }

         // 3. Print key-value pairs
         System.out.println("\nKey-Value Pairs:");
         // Iterate over the set of Map.Entry objects
         for (Map.Entry<String, Object> entry : studentInfo.entrySet()) {
             System.out.printf("%s: %s%n", entry.getKey(), entry.getValue());
         }
     }

    // --- Problem 23: Function Default Arguments (Method Overloading in Java) ---
    /**
     * Task: Create a `power` method. Exponent defaults to 2.
     * Call power(5, 3) -> 125
     * Call power(7) -> 49
     */
     // Method that takes only the base, assumes exponent is 2
     public static double power(double base) {
         // Calls the other version of the method with exponent 2
         return power(base, 2);
     }

     // Method that takes both base and exponent
     public static double power(double base, int exponent) {
         // Use Math.pow for calculation
         return Math.pow(base, exponent);
     }

     public static void solveProblem23() {
         // Call with both arguments
         System.out.println(power(5, 3)); // Output: 125.0

         // Call with only the base (uses the overloaded method with default exponent)
         System.out.println(power(7));   // Output: 49.0
     }

    // --- Problem 24: Tuples (Immutable Records/Classes in Java) ---
    /**
     * Task: Create an immutable point (10, 20), print it, print x. Demonstrate immutability.
     * Point[x=10, y=20]  (or similar toString output)
     * 10
     */
    // Using Java Record (available Java 14+) for concise immutable data carriers
    record Point(int x, int y) {}

    // If using older Java, you'd create a class:
    /*
    static class Point { // Use static for inner class if used within static context like main
        private final int x; // final makes them immutable after construction
        private final int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() { return x; }
        public int getY() { return y; }

        @Override
        public String toString() { return String.format("Point(x=%d, y=%d)", x, y); }
    }
    */

     public static void solveProblem24() {
         // 1. Create the immutable Point object
         Point point = new Point(10, 20);

         // 2. Print the point (Records have automatic toString)
         System.out.println(point);

         // 3. Print the first element (x-coordinate) using the accessor method
         System.out.println(point.x()); // Accessor for record component 'x'
         // If using the class version: System.out.println(point.getX());

         // 4. Try to change element (compile-time error for Records/final fields)
         // point.x = 15; // This line will not compile because record components are final.
         // point.setX(15); // No setter methods generated for records

         System.out.println("\nAttempting to modify a Record field results in a compile-time error.");
     }

    // --- Problem 25: More List Methods (`add(index)`, `remove(index)`, `remove(Object)`) ---
    /**
     * Task: Start with letters = ['a', 'b', 'd', 'e']. Insert 'c', remove last, remove 'a'.
     * Initial list: [a, b, d, e]
     * After insert: [a, b, c, d, e]
     * After remove last: [a, b, c, d] (Removed 'e')
     * After remove 'a': [b, c, d]
     */
     public static void solveProblem25() {
        // 1. Start with the list
        List<String> letters = new ArrayList<>(Arrays.asList("a", "b", "d", "e"));
        System.out.println("Initial list: " + letters);

        // 2. Insert 'c' at index 2
        letters.add(2, "c"); // Inserts 'c' before the element currently at index 2 ('d')
        System.out.println("After insert: " + letters);

        // 3. Remove the last element using its index (size - 1)
        // .remove(index) returns the removed element
        String removedElement = letters.remove(letters.size() - 1);
        System.out.println("After remove last: " + letters + " (Removed '" + removedElement + "')");

        // 4. Remove 'a' by its value
        // .remove(Object) returns true if the element was found and removed, false otherwise
        boolean removed = letters.remove("a"); // Removes the first occurrence of "a"
        System.out.println("After remove 'a': " + letters + " (Removed successfully: " + removed + ")");
     }

    // --- Problem 26: Combining Input, Loop, List ---
    /**
     * Task: Repeatedly ask user for number or "done". Add numbers to list. Print list at end.
     * Enter a number (or 'done' to finish): 10
     * Enter a number (or 'done' to finish): 25
     * Enter a number (or 'done' to finish): 8
     * Enter a number (or 'done' to finish): DoNe
     * Final list: [10, 25, 8]
     */
    public static void solveProblem26() {
        List<Integer> numbers = new ArrayList<>();
        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                System.out.print("Enter a number (or 'done' to finish): ");
                String userInput = scanner.nextLine();

                if (userInput.equalsIgnoreCase("done")) { // Case-insensitive check
                    break; // Exit loop
                }

                try {
                    // Try converting to integer
                    int num = Integer.parseInt(userInput);
                    numbers.add(num); // Add to list
                } catch (NumberFormatException e) {
                    // Handle invalid number input (that wasn't "done")
                    System.out.println("Invalid input. Please enter an integer or 'done'.");
                }
            }
        } // Scanner closed automatically

        System.out.println("Final list: " + numbers);
    }

    // --- Problem 27: Function Returning a Modified List ---
    /**
     * Task: Create method `getEvenNumbers` taking List<Integer>, returning new List<Integer> with only evens.
     * Test with [1, 2, ..., 10] -> [2, 4, 6, 8, 10]
     */
    public static List<Integer> getEvenNumbers(List<Integer> inputList) {
        List<Integer> evenNumbers = new ArrayList<>(); // Create new list
        for (Integer number : inputList) { // Iterate through input list
            if (number != null && number % 2 == 0) { // Check if even (and not null)
                evenNumbers.add(number); // Add to new list
            }
        }
        return evenNumbers; // Return the new list
    }

    public static void solveProblem27() {
        List<Integer> myList = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        List<Integer> evenResult = getEvenNumbers(myList);
        System.out.println(evenResult); // Output: [2, 4, 6, 8, 10]

        // Test with nulls or empty list
        List<Integer> mixedList = new ArrayList<>(Arrays.asList(1, null, 2, 3, null, 4));
        System.out.println(getEvenNumbers(mixedList)); // Output: [2, 4]
        List<Integer> emptyList = new ArrayList<>();
        System.out.println(getEvenNumbers(emptyList)); // Output: []
    }

    // --- Problem 28: Checking Data Types ---
    /**
     * Task: Print the data type (class name) of various variables.
     * Type of a: Integer
     * Type of b: Double
     * Type of c: String
     * Type of d: ArrayList
     * Type of e: HashMap
     * Type of f: Point (or custom class/array type if not using Record)
     * Type of g: Boolean
     */
     public static void solveProblem28() {
        // Java uses wrapper classes for primitives when stored in collections
        // or when using Object type. `int` becomes `Integer`, `double` becomes `Double`, etc.
        Integer a = 10; // Autoboxing
        Double b = 3.14; // Autoboxing
        String c = "Hello";
        List<Integer> d = new ArrayList<>(Arrays.asList(1, 2, 3));
        Map<String, String> e = new HashMap<>();
        e.put("key", "value");
        Point f = new Point(1, 2); // Using the Record from Problem 24
        Boolean g = true; // Autoboxing

        // Using getClass().getSimpleName() to get the class name without package
        System.out.printf("Type of a: %s%n", a.getClass().getSimpleName());
        System.out.printf("Type of b: %s%n", b.getClass().getSimpleName());
        System.out.printf("Type of c: %s%n", c.getClass().getSimpleName());
        System.out.printf("Type of d: %s%n", d.getClass().getSimpleName());
        System.out.printf("Type of e: %s%n", e.getClass().getSimpleName());
        System.out.printf("Type of f: %s%n", f.getClass().getSimpleName());
        System.out.printf("Type of g: %s%n", g.getClass().getSimpleName());

        // Demonstrating instanceof
        if (a instanceof Integer) {
             System.out.println("Variable 'a' is an Integer.");
        }
     }

    // --- Problem 29: Working with Dictionary Values ---
    /**
     * Task: Given `scores` Map, calculate and print the average score.
     * Average score: 85.75
     */
    public static void solveProblem29() {
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Math", 85);
        scores.put("Science", 92);
        scores.put("History", 78);
        scores.put("English", 88);

        // 1. Get the collection of values
        // Collection<Integer> scoreValues = scores.values(); // Can store if needed

        // 2. Calculate sum
        double totalScore = 0; // Use double for sum to allow fractional average
        for (Integer score : scores.values()) {
            if (score != null) { // Check for null just in case
                 totalScore += score;
            }
        }

        // 3. Get the count
        int numScores = scores.size();

        // 4. Calculate average
        if (numScores > 0) {
            double averageScore = totalScore / numScores;
            System.out.printf("Average score: %.2f%n", averageScore); // Format to 2 decimal places
        } else {
            System.out.println("Cannot calculate average of empty scores.");
        }
    }

    // --- Problem 30: Putting It Together - Simple Data Processor ---
    /**
     * Task: Given list of product Maps (name, price), find name of most expensive product.
     * Input: [{"name": "Laptop", "price": 1200}, ...]
     * Output: The most expensive product is: Laptop
     */
    public static String findMostExpensiveProduct(List<Map<String, Object>> productList) {
        if (productList == null || productList.isEmpty()) {
            return null; // Or throw exception, or return default message
        }

        String mostExpensiveName = null;
        // Initialize maxPrice carefully - use first product's price or minimum possible value
        double maxPrice = -1.0; // Use double for price comparison flexibility
        boolean firstProduct = true;

        for (Map<String, Object> product : productList) {
             // Safely get price, handle potential non-Integer types if map is truly Object
             Object priceObject = product.get("price");
             if (!(priceObject instanceof Number)) continue; // Skip if price isn't a number

             double currentPrice = ((Number) priceObject).doubleValue();
             String currentName = (String) product.get("name"); // Assume name is String

             if (firstProduct || currentPrice > maxPrice) {
                 maxPrice = currentPrice;
                 mostExpensiveName = currentName;
                 firstProduct = false;
             }
        }
        return mostExpensiveName;
    }

     public static void solveProblem30() {
         // Create the list of product maps
         List<Map<String, Object>> products = new ArrayList<>();

         Map<String, Object> p1 = new HashMap<>();
         p1.put("name", "Laptop"); p1.put("price", 1200);
         products.add(p1);

         Map<String, Object> p2 = new HashMap<>();
         p2.put("name", "Mouse"); p2.put("price", 25);
         products.add(p2);

         Map<String, Object> p3 = new HashMap<>();
         p3.put("name", "Keyboard"); p3.put("price", 75);
         products.add(p3);

         Map<String, Object> p4 = new HashMap<>();
         p4.put("name", "Monitor"); p4.put("price", 300.50); // Test with double
         products.add(p4);


         String expensiveProductName = findMostExpensiveProduct(products);

         if (expensiveProductName != null) {
             System.out.println("The most expensive product is: " + expensiveProductName);
         } else {
             System.out.println("The product list is empty or invalid.");
         }

         // Test empty list
         List<Map<String, Object>> emptyProducts = new ArrayList<>();
         System.out.println("Most expensive in empty list: " + findMostExpensiveProduct(emptyProducts)); // Should be null/message
     }

} // End of JavaBasicsTraining class
