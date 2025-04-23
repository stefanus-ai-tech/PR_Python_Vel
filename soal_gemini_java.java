import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List; // Using List interface is good practice
import java.util.Map;
import java.util.Scanner; // For user input

public class soal_gemini_java {

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
     * Hello Python!
     * Hello Python!
     * Hello Python!
     * Hello Python!
     * Hello Python!
     */
    public static void solveProblem1() {

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

    }

    // --- Problem 5: Controlling Loop Flow (break) ---
    /**
     * Task: Loop 0 to 9. If odd, print stopping message and exit loop. If even, print even message.
     * Number 0 is even
     * Number 1 is odd, stopping the program.
     */
    public static void solveProblem5() {

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


    }

    // --- Problem 7: Introduction to Functions (Methods in Java) ---
    /**
     * Task: Create a method `greetUser` that accepts a name (String) and prints a greeting.
     * Example calls: greetUser("Budi"), greetUser("Ani")
     */
    public static void solveProblem7() {


    }

    // --- Problem 8: Functions with Return Values ---
    /**
     * Task: Create a method `calculateRectangleArea` that accepts length and width (int) and returns the area (int).
     * Example calls shown in solveProblem8.
     */


    public static void solveProblem8() {

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

    }

    // --- Problem 10: Functions Processing Lists ---
    /**
     * Task: Create a method `printAllElements` that accepts a List and prints its elements.
     * Example calls shown in solveProblem10.
     */
    // Using generics <T> makes the method reusable for lists of any type
    public static <T> void printAllElements(List<T> listData) {

    }
    /*
     * // Alternative without generics (less flexible, requires specific types)
     * public static void printAllIntegers(List<Integer> listData) { ... }
     * public static void printAllStrings(List<String> listData) { ... }
     */

    public static void solveProblem10() {
   
    }

    // --- Problem 11: String Indexing and Slicing ---
    /**
     * Task: Given message = "Hello Python World", print first char, last char, "Python" substring.
     * H
     * d
     * Python
     */
     public static void solveProblem11() {
  
     }

    // --- Problem 12: Basic String Methods ---
    /**
     * Task: Given mixed_case = "PyThOn PrOgRaMmInG", print uppercase, lowercase, find index of "PrOg".
     * PYTHON PROGRAMMING
     * python programming
     * 7
     */
     public static void solveProblem12() {
  
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

     }

    // --- Problem 14: Accessing List Elements and Length ---
    /**
     * Task: Given colors = ["Red", ...], print first, last, and total number.
     * Red
     * Purple
     * 5
     */
    public static void solveProblem14() {
 
    }

    // --- Problem 15: Modifying Lists (add) and Checking Membership (contains) ---
    /**
     * Task: Create planets list, add "Mars", print, check membership of "Jupiter" and "Earth".
     * [Mercury, Venus, Earth, Mars]
     * false
     * true
     */
     public static void solveProblem15() {

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

    }

    // --- Problem 18: Getting User Input ---
    /**
     * Task: Ask user for name, print personalized greeting.
     * Enter your name: Alice
     * Hello, Alice!
     */
     public static void solveProblem18() {

     }

    // --- Problem 19: Using `else if` for Multiple Conditions ---
    /**
     * Task: Ask user for integer, print "Positive", "Negative", or "Zero".
     * Enter an integer: 10
     * Positive
     */
    public static void solveProblem19() {
 
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

    }

    // --- Problem 21: Dictionaries (HashMap) - Creation and Access ---
    /**
     * Task: Create a Map `studentInfo` (name, major, id) and print name and ID.
     * Budi
     * 12345
     */
     public static void solveProblem21() {

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

     }

    // --- Problem 23: Function Default Arguments (Method Overloading in Java) ---
    /**
     * Task: Create a `power` method. Exponent defaults to 2.
     * Call power(5, 3) -> 125
     * Call power(7) -> 49
     */
     // Method that takes only the base, assumes exponent is 2

     public static void solveProblem23() {

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

    }

    // --- Problem 27: Function Returning a Modified List ---
    /**
     * Task: Create method `getEvenNumbers` taking List<Integer>, returning new List<Integer> with only evens.
     * Test with [1, 2, ..., 10] -> [2, 4, 6, 8, 10]
     */
    public static List<Integer> getEvenNumbers(List<Integer> inputList) {

    }

    public static void solveProblem27() {

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

     }

    // --- Problem 29: Working with Dictionary Values ---
    /**
     * Task: Given `scores` Map, calculate and print the average score.
     * Average score: 85.75
     */
    public static void solveProblem29() {
    
    }

    // --- Problem 30: Putting It Together - Simple Data Processor ---
    /**
     * Task: Given list of product Maps (name, price), find name of most expensive product.
     * Input: [{"name": "Laptop", "price": 1200}, ...]
     * Output: The most expensive product is: Laptop
     */
    public static String findMostExpensiveProduct(List<Map<String, Object>> productList) {
    
    }

} // End of JavaBasicsTraining class
