import java.util.ArrayDeque; // For ArrayList
import java.util.ArrayList;    // For array utility methods like toString, sort
import java.util.Arrays;   // For Graph Adjacency List
import java.util.HashMap;// For implementing Queue interface, also a List
import java.util.LinkedList;      // Interface for lists
import java.util.List;       // Interface for maps (used in Graph)
import java.util.Map;     // Interface for queues
import java.util.NoSuchElementException;   // For user input (Praktikum)
import java.util.Queue;     // Built-in Stack class (though Deque is preferred now)
import java.util.Scanner; // For empty structure exceptions
import java.util.Stack; // Recommended implementation for Stack/Queue interfaces

/**
 * Demonstrates various Data Structures and Algorithms concepts in Java.
 * Based on the provided mindmap.
 */
public class DataStructuresDemo {

    public static void main(String[] args) {
        System.out.println("===== Data Structures and Algorithms in Java Demo =====");

        // --- Tipe Data dan Array ---
        basicJavaTypesAndSyntax();
        oneDimensionalArrays();
        twoDimensionalArrays();
        arrayListExample();

        // --- Interfaces and Implementations ---
        interfaceImplementationDemo();

        // --- Stack ---
        stackDemo();
        customArrayStackDemo();

        // --- Queue ---
        queueDemo();
        customArrayQueueDemo(); // Simple, non-circular for demo

        // --- Linked List ---
        singlyLinkedListDemo();
        // Doubly Linked List would be similar but with prev pointers

        // --- Searching ---
        searchingDemo();

        // --- Sorting ---
        sortingDemo();

        // --- Binary Tree / Binary Search Tree ---
        binarySearchTreeDemo();

        // --- Graph ---
        graphDemo();

        // --- Praktikum: Input Example ---
        // inputExample(); // Uncomment to run input example

        System.out.println("\\n===== Demo End =====");
    }

    // --- Tipe Data dan Array ---

    public static void basicJavaTypesAndSyntax() {
        System.out.println("\\n--- Basic Java Types and Syntax ---");
        // Primitive Data Types
        int integerVar = 10;        // Integer (byte, short, int, long)
        double doubleVar = 3.14;    // Floating point (float, double)
        char charVar = 'A';         // Character
        boolean booleanVar = true;  // Boolean

        // String (Object, not primitive, but commonly used)
        String stringVar = "Hello Java";

        // Identifiers: variable names (integerVar), class name (DataStructuresDemo), 
        // method name (basicJavaTypesAndSyntax)
        // Keywords: public, static, void, int, double, char, boolean, class, new, etc.

        System.out.println("Integer: " + integerVar);
        System.out.println("Double: " + doubleVar);
        System.out.println("Char: " + charVar);
        System.out.println("Boolean: " + booleanVar);
        System.out.println("String: " + stringVar);

        // Simple operation (Model of Computation - Arithmetic)
        int sum = integerVar + 5;
        System.out.println("Sum: " + sum);

        // Comparison (Model of Computation - Comparison)
        boolean isGreater = integerVar > 5;
        System.out.println("Is integerVar > 5? " + isGreater);
    }

    public static void oneDimensionalArrays() {
        System.out.println("\\n--- 1D Arrays ---");
        // Declaration and Initialization
        int[] numbers = new int[5]; // Declares an array of 5 integers, initialized to 0
        String[] names = {"Alice", "Bob", "Charlie"}; // Declare and initialize

        // Assigning values using index (0 to n-1)
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;
        // numbers[5] = 60; // This would cause an ArrayIndexOutOfBoundsException

        System.out.println("Element at index 2 in numbers: " + numbers[2]); // Output: 30
        System.out.println("First name in names: " + names[0]); // Output: Alice
        System.out.println("Length of numbers array: " + numbers.length); // Output: 5

        // Iterating through an array
        System.out.print("Numbers array elements: ");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();

        System.out.print("Names array elements (enhanced for loop): ");
        for (String name : names) {
            System.out.print(name + " ");
        }
        System.out.println();
        // Memory: Elements are stored contiguously (bersebelahan)
    }

    public static void twoDimensionalArrays() {
        System.out.println("\\n--- 2D Arrays (Matrices) ---");
        // Declaration and Initialization
        int[][] matrix = new int[2][3]; // 2 rows, 3 columns
        String[][] board = {
            {"X", "O", "X"},
            {"O", "X", "O"},
            {"X", "X", "O"}
        };

        // Assigning values
        matrix[0][0] = 1; matrix[0][1] = 2; matrix[0][2] = 3;
        matrix[1][0] = 4; matrix[1][1] = 5; matrix[1][2] = 6;

        System.out.println("Element at row 1, col 2 in matrix: " + matrix[1][2]); // Output: 6
        System.out.println("Element at row 0, col 0 in board: " + board[0][0]); // Output: X

        // Iterating through a 2D array
        System.out.println("Matrix elements:");
        for (int i = 0; i < matrix.length; i++) { // Iterate through rows
            for (int j = 0; j < matrix[i].length; j++) { // Iterate through columns in that row
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println(); // New line after each row
        }
        // Memory: Often row-major order, still logically contiguous blocks
    }

    public static void arrayListExample() {
        System.out.println("\\n--- ArrayList (Dynamic Array) ---");
        // Declaration - Uses Generics for type safety (Tipe Data Objek)
        // Must use Wrapper classes (Integer, Double) for primitive types
        List<String> fruitList = new ArrayList<>(); // Using 'new'

        // Adding elements (Amortized O(1) time complexity)
        fruitList.add("Apple");
        fruitList.add("Banana");
        fruitList.add("Orange");
        fruitList.add(1, "Mango"); // Add at specific index

        System.out.println("Fruit List: " + fruitList);
        System.out.println("Element at index 2: " + fruitList.get(2)); // O(1) access
        System.out.println("Size of list: " + fruitList.size());

        // Removing elements (O(n) time complexity in general)
        fruitList.remove("Banana");
        fruitList.remove(0); // Remove element at index 0

        System.out.println("Fruit List after removals: " + fruitList);

        // Checking if empty
        System.out.println("Is list empty? " + fruitList.isEmpty());
    }


    // --- Interfaces and Implementations ---

    // Example Interface (Abstract Data Type - ADT)
    interface SimpleList<E> {
        void add(E element);
        E get(int index);
        int size();
        boolean isEmpty();
    }

    // Example Implementation
    static class SimpleArrayList<E> implements SimpleList<E> {
        private Object[] data;
        private int size;
        private static final int DEFAULT_CAPACITY = 10;

        public SimpleArrayList() {
            data = new Object[DEFAULT_CAPACITY];
            size = 0;
        }

        @Override
        public void add(E element) {
            if (size == data.length) {
                resize(); // Handle dynamic resizing (like ArrayList)
            }
            data[size++] = element;
        }

        @SuppressWarnings("unchecked")
        @Override
        public E get(int index) {
            if (index < 0 || index >= size) {
                throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
            }
            return (E) data[index]; // Requires casting
        }

        @Override
        public int size() {
            return size;
        }

        @Override
        public boolean isEmpty() {
            return size == 0;
        }

        private void resize() {
            int newCapacity = data.length * 2;
            data = Arrays.copyOf(data, newCapacity);
            System.out.println("Resized internal array to capacity: " + newCapacity);
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder("[");
            for(int i = 0; i < size; i++) {
                sb.append(data[i]);
                if (i < size - 1) sb.append(", ");
            }
            sb.append("]");
            return sb.toString();
        }
    }

    public static void interfaceImplementationDemo() {
        System.out.println("\\n--- Interface and Implementation Demo ---");
        SimpleList<String> myList = new SimpleArrayList<>();
        myList.add("Implement");
        myList.add("Interface");
        System.out.println("My Simple List: " + myList);
        System.out.println("Element at index 0: " + myList.get(0));
        System.out.println("Size: " + myList.size());
    }


    // --- Stack --- (LIFO: Last-In, First-Out)

    public static void stackDemo() {
        System.out.println("\\n--- Stack Demo (using java.util.Stack - Legacy) ---");
        Stack<String> legacyStack = new Stack<>(); // Older implementation
        legacyStack.push("Task 1"); // add(x) / push(x)
        legacyStack.push("Task 2");
        legacyStack.push("Task 3");

        System.out.println("Legacy Stack: " + legacyStack);
        System.out.println("Top element (peek): " + legacyStack.peek()); // Look at top without removing
        System.out.println("Stack size: " + legacyStack.size());

        while (!legacyStack.isEmpty()) {
            System.out.println("Popped: " + legacyStack.pop()); // remove() / pop()
        }
        System.out.println("Is legacy stack empty? " + legacyStack.isEmpty());

        System.out.println("\\n--- Stack Demo (using Deque Interface - Recommended) ---");
        // Use ArrayDeque for better performance than legacy Stack
        Queue<String> stackAsDeque = new ArrayDeque<>(); // Use Deque interface if needed
        ArrayDeque<String> stack = new ArrayDeque<>();

        stack.push("Item A"); // Preferred method for stack behavior
        stack.push("Item B");
        stack.push("Item C");

        System.out.println("Deque as Stack: " + stack);
        System.out.println("Top element (peek): " + stack.peek());

        while (!stack.isEmpty()) {
            System.out.println("Popped: " + stack.pop());
        }
    }

    // Custom Stack using Array (Simple Fixed Size)
    static class ArrayStack<E> {
        private Object[] stackArray;
        private int top; // Index of the top element
        private static final int DEFAULT_CAPACITY = 10;

        public ArrayStack() {
            stackArray = new Object[DEFAULT_CAPACITY];
            top = -1; // Stack is initially empty
        }

        public void push(E element) { // add(x)
            if (top == stackArray.length - 1) {
                 // For simplicity, throw error. A real implementation would resize.
                 throw new StackOverflowError("Stack is full");
            }
            stackArray[++top] = element;
        }

        @SuppressWarnings("unchecked")
        public E pop() { // remove()
            if (isEmpty()) {
                throw new NoSuchElementException("Stack is empty");
            }
            E element = (E) stackArray[top];
            stackArray[top--] = null; // Help GC
            return element;
        }

        @SuppressWarnings("unchecked")
        public E peek() { // top()
             if (isEmpty()) {
                throw new NoSuchElementException("Stack is empty");
            }
            return (E) stackArray[top];
        }

        public boolean isEmpty() {
            return top == -1;
        }

        public int size() {
            return top + 1;
        }
    }

     public static void customArrayStackDemo() {
        System.out.println("\\n--- Custom Array Stack Demo ---");
        ArrayStack<Integer> myStack = new ArrayStack<>();
        myStack.push(100);
        myStack.push(200);
        myStack.push(300);

        System.out.println("Custom Stack size: " + myStack.size());
        System.out.println("Top element (peek): " + myStack.peek());

        while (!myStack.isEmpty()) {
            System.out.println("Popped: " + myStack.pop());
        }
        System.out.println("Is custom stack empty? " + myStack.isEmpty());
     }

    // --- Queue --- (FIFO: First-In, First-Out)

    public static void queueDemo() {
        System.out.println("\\n--- Queue Demo (using Queue Interface with LinkedList) ---");
        // LinkedList implements the Queue interface
        Queue<String> customerQueue = new LinkedList<>();

        // add(x) / offer(x) - Enqueue
        customerQueue.offer("Customer 1"); // offer is preferred (doesn't throw exception if full)
        customerQueue.add("Customer 2");   // add throws exception if capacity-restricted queue is full
        customerQueue.offer("Customer 3");

        System.out.println("Customer Queue: " + customerQueue);
        System.out.println("Queue size: " + customerQueue.size());
        System.out.println("Front element (element/peek): " + customerQueue.peek()); // peek() returns null if empty
        // System.out.println("Front element (element): " + customerQueue.element()); // element() throws exception if empty

        // remove() / poll() - Dequeue
        while (!customerQueue.isEmpty()) {
            System.out.println("Serving: " + customerQueue.poll()); // poll() returns null if empty
            // System.out.println("Serving: " + customerQueue.remove()); // remove() throws exception if empty
        }
        System.out.println("Is queue empty? " + customerQueue.isEmpty());

         System.out.println("\\n--- Queue Demo (using ArrayDeque - Recommended) ---");
        // ArrayDeque is generally more efficient for Queue operations than LinkedList
        Queue<String> efficientQueue = new ArrayDeque<>();
        efficientQueue.offer("Job A");
        efficientQueue.offer("Job B");
        System.out.println("Efficient Queue: " + efficientQueue);
        System.out.println("Processing: " + efficientQueue.poll());
        System.out.println("Efficient Queue: " + efficientQueue);

    }

    // Custom Queue using Array (Simple Fixed Size, Non-Circular)
    // NOTE: A circular array implementation is much more efficient for queues.
    static class ArrayQueue<E> {
        private Object[] queueArray;
        private int size;
        private static final int DEFAULT_CAPACITY = 10;

        public ArrayQueue() {
            queueArray = new Object[DEFAULT_CAPACITY];
            size = 0;
        }
        
        public boolean enqueue(E element) { // add(x) / offer(x)
            if (size == queueArray.length) {
                // For simplicity, return false. Real implementation might resize or throw exception.
                System.err.println("Queue is full!");
                return false;
            }
            queueArray[size++] = element;
            return true;
        }

        @SuppressWarnings("unchecked")
        public E dequeue() { // remove() / poll()
            if (isEmpty()) {
                 throw new NoSuchElementException("Queue is empty");
            }
            E element = (E) queueArray[0];
            // Shift all elements left (INEFFICIENT! O(n)) - Circular array avoids this.
            for (int i = 0; i < size - 1; i++) {
                queueArray[i] = queueArray[i + 1];
            }
            queueArray[--size] = null; // Help GC
            return element;
        }

        @SuppressWarnings("unchecked")
        public E peek() { // first() / element()
             if (isEmpty()) {
                throw new NoSuchElementException("Queue is empty");
            }
            return (E) queueArray[0];
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public int size() {
            return size;
        }
    }

    public static void customArrayQueueDemo() {
        System.out.println("\\n--- Custom Array Queue Demo (Non-Circular - Inefficient Dequeue) ---");
        ArrayQueue<String> myQueue = new ArrayQueue<>();
        myQueue.enqueue("Request 1");
        myQueue.enqueue("Request 2");
        myQueue.enqueue("Request 3");

        System.out.println("Custom Queue size: " + myQueue.size());
        System.out.println("Front element (peek): " + myQueue.peek());

        System.out.println("Dequeued: " + myQueue.dequeue()); // This is O(n) here
        System.out.println("Front element after dequeue: " + myQueue.peek());
        System.out.println("Custom Queue size: " + myQueue.size());

         while (!myQueue.isEmpty()) {
             System.out.println("Dequeued: " + myQueue.dequeue());
         }
        System.out.println("Is custom queue empty? " + myQueue.isEmpty());
    }

    // --- Linked List ---

    // Node for Singly Linked List
    static class Node<E> {
        E data;
        Node<E> next; // Pointer to the next node

        Node(E data) {
            this.data = data;
            this.next = null;
        }
    }

    // Simple Singly Linked List Implementation
    static class SinglyLinkedList<E> {
        private Node<E> head; // Reference to the first node
        private Node<E> tail; // Reference to the last node
        private int size;

        public SinglyLinkedList() {
            head = null;
            tail = null;
            size = 0;
        }

        public int size() {
            return size;
        }

        public boolean isEmpty() {
            return size == 0;
        }

        // Add element to the front (O(1))
        public void addFirst(E element) {
            Node<E> newNode = new Node<>(element);
            newNode.next = head;
            head = newNode;
            if (tail == null) { // If list was empty
                tail = head;
            }
            size++;
        }

        // Add element to the end (O(1) because we have a tail pointer)
        public void addLast(E element) {
            Node<E> newNode = new Node<>(element);
            if (isEmpty()) {
                head = newNode;
                tail = newNode;
            } else {
                tail.next = newNode;
                tail = newNode;
            }
            size++;
        }

        // Remove element from the front (O(1))
        public E removeFirst() {
            if (isEmpty()) {
                 throw new NoSuchElementException("List is empty");
            }
            E data = head.data;
            head = head.next;
            size--;
            if (isEmpty()) { // If list becomes empty
                tail = null;
            }
            return data;
        }

        // Display the list (O(n))
        public void display() {
            System.out.print("LinkedList: [");
            Node<E> current = head;
            while (current != null) {
                System.out.print(current.data);
                if (current.next != null) {
                    System.out.print(" -> ");
                }
                current = current.next;
            }
            System.out.println("]");
        }
    }

    public static void singlyLinkedListDemo() {
        System.out.println("\\n--- Singly Linked List Demo ---");
        SinglyLinkedList<String> list = new SinglyLinkedList<>();
        list.addLast("Node A");
        list.addLast("Node B");
        list.addFirst("Node Zero");
        list.addLast("Node C");

        list.display();
        System.out.println("List size: " + list.size());

        System.out.println("Removed first: " + list.removeFirst());
        list.display();
        System.out.println("List size: " + list.size());
    }


    // --- Searching ---

    // Sequential Search (Linear Search) - O(n)
    public static int sequentialSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i; // Return index if found
            }
        }
        return -1; // Return -1 if not found
    }

    // Binary Search - O(log n) - Requires SORTED array
    public static int binarySearch(int[] sortedArr, int target) {
        int low = 0;
        int high = sortedArr.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2; // Avoid potential integer overflow

            if (sortedArr[mid] == target) {
                return mid; // Target found at mid index
            } else if (sortedArr[mid] < target) {
                low = mid + 1; // Search in the right half
            } else { // sortedArr[mid] > target
                high = mid - 1; // Search in the left half
            }
        }
        return -1; // Target not found
    }

    public static void searchingDemo() {
        System.out.println("\\n--- Searching Demo ---");
        int[] data = {23, 5, 67, 12, 45, 8, 34};
        int target1 = 12;
        int target2 = 99;

        System.out.println("Data Array: " + Arrays.toString(data));

        // Sequential Search
        int index1 = sequentialSearch(data, target1);
        int index2 = sequentialSearch(data, target2);
        System.out.println("Sequential Search for " + target1 + ": Index " + index1 + (index1 != -1 ? " (Found)" : " (Not Found)"));
        System.out.println("Sequential Search for " + target2 + ": Index " + index2 + (index2 != -1 ? " (Found)" : " (Not Found)"));

        // Binary Search (requires sorted array)
        int[] sortedData = Arrays.copyOf(data, data.length);
        Arrays.sort(sortedData); // Use built-in sort (often O(n log n))
        System.out.println("Sorted Data Array: " + Arrays.toString(sortedData));

        int index3 = binarySearch(sortedData, target1);
        int index4 = binarySearch(sortedData, target2);
        System.out.println("Binary Search for " + target1 + ": Index " + index3 + (index3 != -1 ? " (Found)" : " (Not Found)"));
        System.out.println("Binary Search for " + target2 + ": Index " + index4 + (index4 != -1 ? " (Found)" : " (Not Found)"));

        // Java's built-in binary search
        int index5 = Arrays.binarySearch(sortedData, target1); // Uses binary search internally
        System.out.println("Arrays.binarySearch for " + target1 + ": Index " + index5);
    }


    // --- Sorting ---

    // Merge Sort - O(n log n) - Comparison-Based
    public static void mergeSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return; // Base case: already sorted
        }
        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        mergeSort(left);  // Recursively sort left half
        mergeSort(right); // Recursively sort right half
        merge(arr, left, right); // Merge sorted halves
    }

    private static void merge(int[] result, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }
        // Copy remaining elements from left (if any)
        while (i < left.length) {
            result[k++] = left[i++];
        }
        // Copy remaining elements from right (if any)
        while (j < right.length) {
            result[k++] = right[j++];
        }
    }

     // Counting Sort - O(n + k) where k is the range of input - Not Comparison-Based
     // Works best for non-negative integers with a known, reasonably small range.
    public static void countingSort(int[] arr, int maxVal) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        int[] count = new int[maxVal + 1]; // Array to store counts of each element
        int[] output = new int[arr.length]; // Output array

        // 1. Count occurrences of each element
        for (int value : arr) {
            if (value < 0 || value > maxVal) {
                throw new IllegalArgumentException("Value out of range for Counting Sort: " + value);
            }
            count[value]++;
        }

        // 2. Modify count array to store cumulative counts (positions in output)
        for (int i = 1; i <= maxVal; i++) {
            count[i] += count[i - 1];
        }

        // 3. Build the output array (iterate backwards for stability)
        for (int i = arr.length - 1; i >= 0; i--) {
            int value = arr[i];
            output[count[value] - 1] = value;
            count[value]--; // Decrement count for the next occurrence of this value
        }

        // 4. Copy sorted elements back to original array
        System.arraycopy(output, 0, arr, 0, arr.length);
    }


    public static void sortingDemo() {
        System.out.println("\\n--- Sorting Demo ---");
        int[] dataToSort1 = {38, 27, 43, 3, 9, 82, 10};
        int[] dataToSort2 = {5, 1, 4, 1, 5, 9, 2, 6}; // For counting sort (maxVal=9)

        System.out.println("Original Array 1: " + Arrays.toString(dataToSort1));
        mergeSort(dataToSort1);
        System.out.println("Merge Sorted Array 1: " + Arrays.toString(dataToSort1));


        System.out.println("\\nOriginal Array 2: " + Arrays.toString(dataToSort2));
        try {
            countingSort(dataToSort2, 9); // maxVal is 9
             System.out.println("Counting Sorted Array 2: " + Arrays.toString(dataToSort2));
        } catch (IllegalArgumentException e) {
            System.err.println("Counting Sort Error: " + e.getMessage());
        }

        // Java's built-in sort (uses highly optimized algorithms like Timsort)
        int[] dataToSort3 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("\\nOriginal Array 3: " + Arrays.toString(dataToSort3));
        Arrays.sort(dataToSort3); // Very efficient built-in sort
        System.out.println("Arrays.sort() Result: " + Arrays.toString(dataToSort3));
    }

    // --- Binary Tree / Binary Search Tree ---

    // Node for Binary Tree
    static class TreeNode {
        int data;
        TreeNode left;  // Left child
        TreeNode right; // Right child
        // TreeNode parent; // Could add parent pointer if needed

        TreeNode(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    // Simple Binary Search Tree Implementation
    static class BinarySearchTree {
        private TreeNode root; // Root node

        public BinarySearchTree() {
            root = null;
        }

        // Insert data (Pencarian Data) - O(log n) average, O(n) worst case
        public void insert(int data) {
            root = insertRecursive(root, data);
        }

        private TreeNode insertRecursive(TreeNode current, int data) {
            if (current == null) {
                return new TreeNode(data); // Base case: Found insertion point
            }

            if (data < current.data) {
                current.left = insertRecursive(current.left, data);
            } else if (data > current.data) {
                current.right = insertRecursive(current.right, data);
            } else {
                // data already exists, do nothing (or handle duplicates as needed)
                return current;
            }
            return current;
        }

        // Search for data (Pencarian Data) - O(log n) average, O(n) worst case
        public boolean contains(int data) {
            return containsRecursive(root, data);
        }

        private boolean containsRecursive(TreeNode current, int data) {
            if (current == null) {
                return false; // Base case: Not found
            }
            if (data == current.data) {
                return true; // Found
            }
            return data < current.data
                   ? containsRecursive(current.left, data)
                   : containsRecursive(current.right, data);
        }

        // In-order traversal (visits nodes in sorted order for BST)
        public void printInOrder() {
            System.out.print("BST In-Order: [ ");
            printInOrderRecursive(root);
            System.out.println("]");
        }

        private void printInOrderRecursive(TreeNode node) {
            if (node != null) {
                printInOrderRecursive(node.left);
                System.out.print(node.data + " ");
                printInOrderRecursive(node.right);
            }
        }
        // Deletion (Penghapusan Data) is more complex, involving different cases (leaf, one child, two children)
        // Not implemented here for brevity.
    }

     public static void binarySearchTreeDemo() {
        System.out.println("\\n--- Binary Search Tree (BST) Demo ---");
        BinarySearchTree bst = new BinarySearchTree();
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);

        bst.printInOrder(); // Should print sorted: [ 20 30 40 50 60 70 80 ]

        System.out.println("BST contains 40? " + bst.contains(40)); // true
        System.out.println("BST contains 99? " + bst.contains(99)); // false
     }

    // --- Graph ---

    // Simple Graph implementation using Adjacency List
    static class Graph<T> {
        // Use a Map to store the adjacency list (Node -> List of Neighbors)
        private Map<T, List<T>> adjacencyList;

        public Graph() {
            adjacencyList = new HashMap<>();
        }

        // Add a new node (vertex)
        public void addNode(T node) {
            adjacencyList.putIfAbsent(node, new LinkedList<>()); // Use LinkedList for neighbor list
        }

        // Add an edge between two nodes (undirected for simplicity here)
        public void addEdge(T node1, T node2) {
            // Ensure both nodes exist
            addNode(node1);
            addNode(node2);

            // Add edge from node1 to node2 and node2 to node1
            adjacencyList.get(node1).add(node2);
            adjacencyList.get(node2).add(node1); // Remove this line for a directed graph
        }

        // Get neighbors of a node
        public List<T> getNeighbors(T node) {
            return adjacencyList.getOrDefault(node, new LinkedList<>());
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder("Graph Adjacency List:\\n");
            for (Map.Entry<T, List<T>> entry : adjacencyList.entrySet()) {
                sb.append(entry.getKey()).append(" -> ").append(entry.getValue()).append("\\n");
            }
            return sb.toString();
        }

        // Basic Breadth-First Search (BFS) - Example Traversal
        public void bfs(T startNode) {
             if (!adjacencyList.containsKey(startNode)) {
                 System.out.println("Start node " + startNode + " not in graph.");
                 return;
             }
             System.out.print("BFS starting from " + startNode + ": ");
             Queue<T> queue = new ArrayDeque<>();
             Map<T, Boolean> visited = new HashMap<>(); // Keep track of visited nodes

             queue.offer(startNode);
             visited.put(startNode, true);

             while (!queue.isEmpty()) {
                 T currentNode = queue.poll();
                 System.out.print(currentNode + " ");

                 for (T neighbor : getNeighbors(currentNode)) {
                     if (!visited.getOrDefault(neighbor, false)) {
                         visited.put(neighbor, true);
                         queue.offer(neighbor);
                     }
                 }
             }
             System.out.println();
        }
    }

    public static void graphDemo() {
        System.out.println("\\n--- Graph Demo (Adjacency List) ---");
        Graph<String> cityGraph = new Graph<>();

        // Add nodes (cities)
        cityGraph.addNode("Jakarta");
        cityGraph.addNode("Bandung");
        cityGraph.addNode("Surabaya");
        cityGraph.addNode("Yogyakarta");
        cityGraph.addNode("Semarang");

        // Add edges (routes - undirected)
        cityGraph.addEdge("Jakarta", "Bandung");
        cityGraph.addEdge("Jakarta", "Semarang");
        cityGraph.addEdge("Bandung", "Yogyakarta");
        cityGraph.addEdge("Semarang", "Surabaya");
        cityGraph.addEdge("Semarang", "Yogyakarta");
        cityGraph.addEdge("Yogyakarta", "Surabaya");

        System.out.println(cityGraph);

        System.out.println("Neighbors of Semarang: " + cityGraph.getNeighbors("Semarang"));

        // Perform a BFS traversal
        cityGraph.bfs("Jakarta");
    }


    // --- Praktikum: Input Example ---

    public static void inputExample() {
        System.out.println("\\n--- Input Example (Scanner) ---");
        Scanner scanner = new Scanner(System.in); // Create Scanner object for keyboard input

        System.out.print("Enter your name: ");
        String name = scanner.nextLine(); // Read a full line of text

        System.out.print("Enter your age: ");
        int age = scanner.nextInt(); // Read an integer
        // Be careful: nextInt() doesn't consume the newline character.
        scanner.nextLine(); // Consume the leftover newline

        System.out.println("\\nHello, " + name + "! You are " + age + " years old.");

        // Example: Reading array elements
        System.out.print("How many numbers do you want to enter? ");
        int count = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        if (count > 0) {
            int[] userNumbers = new int[count];
            System.out.println("Enter " + count + " numbers:");
            for (int i = 0; i < count; i++) {
                System.out.print("Number " + (i + 1) + ": ");
                userNumbers[i] = scanner.nextInt();
                scanner.nextLine(); // Consume newline
            }
            System.out.println("You entered: " + Arrays.toString(userNumbers));
        }

        scanner.close(); // Close the scanner when done
    }
}
