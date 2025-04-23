import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class soal_gemini_java_notes {

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
        for (int i = 1; i <=5 ; i ++) {
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
        String status = "";
        for (int i = 1; i < 6; i++){
            if (i>3){
                status = "Large";
            } else{
                status = "Small";
            }
            System.out.println(String.format("Number %d is %s ", i, status));
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
        String status = "";
        for (int i = 0; i < 6; i++){
            if (i%2==0){
                status = "Even";
            } else{
                status = "Odd";
            }
            System.out.println(String.format("Number %d is %s ", i, status));
        }
    }

    // --- Problem 5: Controlling Loop Flow (break) ---
    /**
     * Task: Loop 0 to 9. If odd, print stopping message and exit loop. If even, print even message.
     * Number 0 is even
     * Number 1 is odd, stopping the program.
     */
    public static void solveProblem5() {
        String status = "";
        for (int i = 0; i < 9; i++){
            if (i%2==0){
                status = "Even";
            } else{
                status = "Odd";
            }
            
            if (status == "Odd"){
                System.out.println(String.format("Number %d is %s, stopping the program", i, status));
                break;
            } else{
                System.out.println(String.format("Number %d is %s ", i, status));
                
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
        int batas = 6;
        String bintang = "*";
        for (int i = 1; i < batas; i++) {
            for (int j = i; j < batas; j++) {
                System.out.println(bintang.repeat(j));
                break;
            }
        }
    }

    // --- Problem 7: Introduction to Functions (Methods in Java) ---
    /**
     * Task: Create a method `greetUser` that accepts a name (String) and prints a greeting.
     * Example calls: greetUser("Budi"), greetUser("Ani")
     */
    public static void greetUser(String name) {
        System.out.println(String.format("Hello there, %s", name));
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

    public static int calculateRectangleArea(int length, int width){
        return(length * width);
    }


    public static void solveProblem8() {
        System.out.println(calculateRectangleArea(10, 11));
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
        ArrayList<String> fruitList = new ArrayList<>();
        fruitList.add("Apple");
        fruitList.add("Orange");
        fruitList.add("Mange");
        fruitList.add("Banana");

        for (String x: fruitList){
            System.out.println(x);
        }
    }

    // --- Problem 10: Functions Processing Lists ---
    /**
     * Task: Create a method `printAllElements` that accepts a List and prints its elements.
     * Example calls shown in solveProblem10.
     */
    // Using generics <T> makes the method reusable for lists of any type
    public static <T> void printAllElements(List<T> listData) {
        for (T x : listData) {
            System.out.println(x);
        }
    }
    /*
     * // Alternative without generics (less flexible, requires specific types)
     * public static void printAllIntegers(List<Integer> listData) { ... }
     * public static void printAllStrings(List<String> listData) { ... }
     */

    public static void solveProblem10() {
        ArrayList<String> fruitList = new ArrayList<>();
        fruitList.add("Apple");
        fruitList.add("Orange");
        fruitList.add("Mange");
        fruitList.add("Banana");

        printAllElements(fruitList);
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
        String firstChar = message.substring(0,1);
        String lastChar = message.substring(message.length()-1);
        String Python = message.substring(6,12);

        System.out.println(firstChar);
        System.out.println(lastChar);
        System.out.println(Python);
     }

    // --- Problem 12: Basic String Methods ---
    /**
     * Task: Given mixed_case = "PyThOn PrOgRaMmInG", print uppercase, lowercase, find index of "PrOg".
     * PYTHON PROGRAMMING
     * python programming
     * 7
     */
     public static void solveProblem12() {
        String mixed_case = "PyThOn PrOgRaMmInG";

        System.out.println(mixed_case.toUpperCase());
        System.out.println(mixed_case.toLowerCase());
        System.out.println(mixed_case.indexOf("PrOg"));

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
        String yoman = "LOOP";
        
        for (int i = 0; i < yoman.length(); i++){
            char c = yoman.charAt(i);
            System.out.println(c);
        }

     }

    // --- Problem 14: Accessing List Elements and Length ---
    /**
     * Task: Given colors = ["Red", ...], print first, last, and total number.
     * Red
     * Purple
     * 5
     */
    public static void solveProblem14() {
        String[] colors = {"Red", "Green","Yellow", "Blue", "Purple"};
        System.out.println(colors[0]);
        System.out.println(colors[colors.length-1]);
        System.out.println(colors.length);

    }

    // --- Problem 15: Modifying Lists (add) and Checking Membership (contains) ---
    /**
     * Task: Create planets list, add "Mars", print, check membership of "Jupiter" and "Earth".
     * [Mercury, Venus, Earth, Mars]
     * false
     * true
     */
     public static void solveProblem15() {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars"};
        boolean hasJupiter = Stream.of(planets).anyMatch(x -> x.equals("Jupiter"));
        boolean hasEarth = Stream.of(planets).anyMatch(x -> x.equals("Earth"));
        
        System.out.println(Arrays.toString(planets));
        System.out.println(hasJupiter);
        System.out.println(hasEarth);
        
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
        int i = 0;
        while (i < 5){
            System.out.println(i);
            i++;
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
        int i = 1;
        while (i < 50){
            if (i >= 50){
                break;
            } else{
                ;
            }
            System.out.println(i);
            i = i * 2;
        }
    }

    // --- Problem 18: Getting User Input ---
    /**
     * Task: Ask user for name, print personalized greeting.
     * Enter your name: Alice
     * Hello, Alice!
     */
     public static void solveProblem18() {
        try(Scanner input = new Scanner(System.in)){
            System.out.println("Enter your username: ");

            String userName = input.nextLine();
            System.out.println("Your username is: " + userName);
        }
     }

    // --- Problem 19: Using `else if` for Multiple Conditions ---
    /**
     * Task: Ask user for integer, print "Positive", "Negative", or "Zero".
     * Enter an integer: 10
     * Positive
     */
    public static void solveProblem19() {
        try (Scanner input = new Scanner(System.in)){
            System.out.println("Enter an integer: ");

            int integer = input.nextInt();
            if (integer > 0){
                System.out.println("Positive");
            } else if (integer < 0) {
                System.out.println("Negative");
            } else {
                System.out.println("Zero");
            }
        } catch (Exception e) {
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
        for (int i = 0; i <= 10; i++) {
            if (i % 2 == 0) {
                continue;
            } else{
                System.out.println(i);
            }
        }
    }

    // --- Problem 21: Dictionaries (HashMap) - Creation and Access ---
    /**
     * Task: Create a Map `studentInfo` (name, major, id) and print name and ID.
     * Budi
     * 12345
     */
     public static void solveProblem21() {
        HashMap<String, Object> studentInfo  = new HashMap<>();
        studentInfo.put("Name", "Budi");
        studentInfo.put("Major", "Computer Science");
        studentInfo.put("id", 12345);

        // studentInfo.forEach((key, value)-> System.out.println(key + " " + value));
        System.out.println(studentInfo);
        System.out.println(studentInfo.get("Name"));
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
        HashMap<String, Object> studentInfo  = new HashMap<>();
        studentInfo.put("Name", "Budi");
        studentInfo.put("Major", "Computer Science");
        studentInfo.put("id", 12345);

        System.out.println("========= Printing Keys start=========");
        for (Object i : studentInfo.keySet()){
            System.out.println(i);
        }
        System.out.println("========= Printing Keys end =========");
        System.out.println("========= Printing Values start=========");
        for (Object i : studentInfo.values()){
            System.out.println(i);
        }
        System.out.println("========= Printing Values end=========");
        System.out.println("========= Printing pairs start =========");
        for (Object i : studentInfo.keySet()){
            System.out.println("key: " + i + "value: " + studentInfo.get(i));
        }
        System.out.println("========= Printing pairs end =========");
     }

    // --- Problem 23: Function Default Arguments (Method Overloading in Java) ---
    /**
     * Task: Create a `power` method. Exponent defaults to 2.
     * Call power(5, 3) -> 125
     * Call power(7) -> 49
     */
     // Method that takes only the base, assumes exponent is 2
     
     public static int power(int a){
        return (int)Math.pow(a, 2);
     }

     public static int power(int a, int b){
        return (int)Math.pow(a, b);
     }

     public static void solveProblem23() {
        System.out.println(power(5,3));
        System.out.println(power(7));
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
        record immutable_stuff(int x, int y){}

        immutable_stuff immutable_stuff1 = new immutable_stuff(10,20);
        immutable_stuff immutable_stuff2 = new immutable_stuff(10,20);

        //toString()
        System.out.println(immutable_stuff1);

        // accessing fileds
        System.out.println("x: " + immutable_stuff1.x());
        System.out.println("y: " + immutable_stuff1.y());

        //equals()
        System.out.println(immutable_stuff1.equals(immutable_stuff2));
        
        //hashCode()
        System.out.println(immutable_stuff1 == immutable_stuff2);
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
        ArrayList<String> letters = new ArrayList<>();
        letters.add("a");
        letters.add("b");
        letters.add("d");
        letters.add("e");

        System.out.println("Initial: " + letters);

        letters.add(2, "c");
        System.out.println("Tambahin c di index 2: " + letters);

        letters.remove(letters.size() -1);
        System.out.println("Elemen terakhir diremove: " + letters);

        letters.remove("a");
        System.out.println("Remove a: " + letters);
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
        try (Scanner input = new Scanner(System.in)){
            System.out.println("Enter a number (or 'done' to finish): ");
            while (true) { 
                List<Integer> cache = new ArrayList<>();
                Object user_input = input.next();
                String string_user_input = (String) user_input;
                int int_user_input = (int) user_input;
                if (string_user_input.toLowerCase() == "done"){
                    System.out.println("Final list: " + cache);
                    break;
                } else{
                    cache.add(int_user_input);
                }
            }
        } catch (Exception e) {
        }
    }

    // --- Problem 27: Function Returning a Modified List ---
    /**
     * Task: Create method `getEvenNumbers` taking List<Integer>, returning new List<Integer> with only evens.
     * Test with [1, 2, ..., 10] -> [2, 4, 6, 8, 10]
     */

    public static List<Integer> getEvenNumbers(List<Integer> numbers) {
        List<Integer> evenify = numbers.stream()
                                        .filter(x -> x % 2 == 0)
                                        .collect(Collectors.toList());
        return(evenify);
    }


    public static void solveProblem27() {
        List<Integer> numberList = List.of(1,2,3,4,5,6,7,8,9,10);
        System.out.println(getEvenNumbers(numberList));
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
     public record z (int number){}
   
     public static void solveProblem28() {
        Object a = 20;
        Object b = 20.3;
        Object c = "Yoman";
        Object d = new ArrayList<>();
        Object e = new HashMap<>();
        Object f = new z(10);
        Object g = true;

        Object[] variables = {a,b,c,d,e,f,g};

        for (Object i : variables) {
            System.out.println(i + " have the data type of: " + i.getClass().getSimpleName());
        }

     }


//     **Problem 29: Working with Dictionary Values**

// * **Objective:** Perform calculations or operations on values stored within a dictionary.
// * **Task:** Given the dictionary 
// `scores = {"Math": 85, "Science": 92, "History": 78, "English": 88}`, 
// write Python code to calculate and print the *average* score.
// * **Expected Output (or close due to float precision):**
//     ```
//     Average score: 85.75
//     ```
// * **Tips:**
//     1.  Get all the values from the dictionary using `.values()`.
//     2.  Calculate the sum of these values (you can use the `sum()` function).
//     3.  Calculate the number of values (you can use `len()` on the dictionary or the values view).
//     4.  Divide the sum by the count to get the average.
// ---
    public static void solveProblem29() {
        HashMap<String, Integer> scores = new HashMap<>();
        scores.put("Math", 85);
        scores.put("Science", 92);
        scores.put("History", 78);
        scores.put("English", 88);

        double sum = scores.values().stream().mapToInt(Integer::intValue).sum();
        double averagez = sum / scores.size();

        System.out.println("So the average scores is: " + averagez);

    }

    // **Problem 30: Putting It Together - Simple Data Processor**

    // * **Objective:** Combine functions, lists, dictionaries, and loops to process 
    // a small dataset.
    // * **Task:** You are given a list of dictionaries, where each dictionary represents 
    // a product with its name and price:
    //     ```python
    //     products = [
    //         {"name": "Laptop", "price": 1200},
    //         {"name": "Mouse", "price": 25},
    //         {"name": "Keyboard", "price": 75},
    //         {"name": "Monitor", "price": 300}
    //     ]
    //     ```
    //     Create a function `find_most_expensive_product(product_list)` that:
    //     1.  Accepts the list of product dictionaries.
    //     2.  Finds the product with the highest price.
    //     3.  Returns the *name* of the most expensive product.
    //     * Call the function with the `products` list and print the result.
    // * **Expected Output:**
    //     ```
    //     The most expensive product is: Laptop
    //     ```
    // * **Tips:**
    //     * Initialize variables to keep track of the highest price found so far 
    //    (e.g., `max_price = -1` or price of the first item) 
    //     and the name of that product (`most_expensive_name = ""`).
    //     * Loop through the `product_list`. In each iteration, access the price from the 
    //     current product dictionary.
    //     * Compare the current product's price with `max_price`. If it's higher, update 
    //     `max_price` and `most_expensive_name`.
    //     * Return the `most_expensive_name` after the loop finishes. Handle the case of an 
    //     empty input list if necessary.
    

    public static String find_most_expensive_product(List<Map<String, Object>> product_list){
        int maxPrice = Integer.MIN_VALUE;
        String mostExpensiveProduct = null;

        for (Map<String, Object> product : product_list){
            Object priceObj = product.get("price");
            if (priceObj instanceof Integer){
                int price = (Integer) priceObj;
                if (price > maxPrice) {
                    maxPrice = price;
                    mostExpensiveProduct = (String) product.get("name");
                    
            }
        }
    }

    return mostExpensiveProduct;
    }
    public static void solveProblem30() {
        List<Map<String, Object>> products = new ArrayList<>();

        Map<String, Object> product1 = new HashMap<>();
        product1.put("name", "Laptop");
        product1.put("price", 1200);

        Map<String, Object> product2 = new HashMap<>();
        product2.put("name", "Mouse");
        product2.put("price", 25);

        Map<String, Object> product3 = new HashMap<>();
        product3.put("name", "Keyboard");
        product3.put("price", 75);

        Map<String, Object> product4 = new HashMap<>();
        product4.put("name", "Monitor");
        product4.put("price", 300);

        products.add(product1);
        products.add(product2);
        products.add(product3);
        products.add(product4);

        // System.out.println(products);
        // System.out.println(products.get(1).get("name"));
        // System.out.println(products.get(1).get("price"));
        System.out.println(find_most_expensive_product(products));
    }


} // End of JavaBasicsTraining class
