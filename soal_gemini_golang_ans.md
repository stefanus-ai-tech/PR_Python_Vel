Okay, here are the 30 problems adapted into a Go-themed questionnaire. I've changed JavaScript concepts and syntax (like `Array`, `Object`, `function`, `console.log`) to their Go equivalents (like `slice`, `struct`, `map`, `func`, `fmt.Println`).

---

**Go Fundamentals Questionnaire**

**--- Problem 1: Introduction to Output and Simple Loops ---**

- **Task:** Write Go code using a `for` loop to print the string "Hello Go!" to the console 5 times. You'll need the `fmt` package.

```go
package main

import (
	"fmt"
)

func main() {
	for i:=0; i < 5; i++ {
		fmt.Println("Hello Go!")
	}
}
```

**--- Problem 2: Looping with Sequential Numbers ---**

- **Task:** Write Go code using a `for` loop to display the numbers 1 through 5, each on a new line, in the console using `fmt.Println`.

```go
package main

import (
	"fmt"
)

func main() {
	for i:=1; i <= 5; i++ {
		fmt.Println(i)
	}
}
```

**--- Problem 3: Introduction to Conditionals (if/else) within a Loop ---**

- **Task:** Loop through numbers 1 to 5. For each number, print to the console whether it's "Small" (if the number is less than or equal to 3) or "Large" (if the number is greater than 3). Use `fmt.Printf` for formatted output like: "Number 1 is Small", "Number 4 is Large", etc.

```go
package main

import (
	"fmt"
)

func main() {
	for i:=1; i <= 5; i++ {
		var status string
		if i <= 3{
			status = "Small"
		} else {
			status = "Large"
		}

		fmt.Println("Number", i, "is", status )
	}
}
```

**--- Problem 4: Using Modulo and Conditionals (Even/Odd) ---**

- **Task:** Loop through numbers 0 to 5. For each number, print to the console whether the number is "even" or "odd" using the modulo operator (`%`). The output should look like: "Number 0 is even", "Number 1 is odd", etc. Use `fmt.Printf`.

```go
package main

import (
	"fmt"
)

func main() {
	for i:=1; i <= 5; i++ {
		var status string
		if i % 2 == 0 {
			status = "Even"
		} else {
			status = "Odd"
		}

		fmt.Println("Number", i, "is", status )
	}
}
```

**--- Problem 5: Controlling Loop Flow (`break`) ---**

- **Task:** Loop through numbers starting from 0 up to (but not including) 9. If the current number is even, print "Number [X] is even". If the current number is odd, print "Number [X] is odd, stopping the loop." and immediately exit the loop using `break`.

```go
package main

import (
	"fmt"
)

func main() {
	for i:=1; i < 9; i++ {
		var status string
		if i % 2 == 0 {
			status = "Even"
		} else {
			status = "Odd"
		}

		if i >= 2 {
			fmt.Println("Number", i, "is", status ,"Stopping the loop")
			break
		}

		fmt.Println("Number", i, "is", status )
	}
}
```

**--- Problem 6: Nested Loops - Creating a Simple Pattern ---**

- **Task:** Using nested `for` loops, generate and print the following pattern of stars (`*`) to the console. Use `fmt.Print` for the stars and `fmt.Println` for newlines.

  ```
  *
  **
  ***
  ****
  *****
  ```

```go
package main

import (
	"fmt"
	"strings"
)

func main() {

	bintang := "#"

	for i:=1; i < 6; i++ {
		fmt.Println(strings.Repeat(bintang, i))
	}
}

```

**--- Problem 7: Introduction to Functions ---**

- **Task:** Create a Go function named `greetUser` that accepts one argument (a string representing a name). When called, the function should print a greeting like "Hello there, [Name]!" to the console using `fmt.Printf`. Demonstrate calling it from your `main` function with "Budi" and "Ani".

```go
package main

import (
	"fmt"
)

func greetUser(x string) {
	fmt.Println("Hello there,", x)
}

func main() {
	greetUser("Budi")
	greetUser("Ani")
}

```

**--- Problem 8: Functions with Return Values ---**

- **Task:** Create a Go function named `calculateRectangleArea` that accepts two integer arguments (representing length and width). The function should calculate and _return_ the area of the rectangle (length \* width) as an integer. Demonstrate calling it from `main` with length 10 and width 11 and printing the returned result using `fmt.Println`.

```go
package main

import "fmt"

func calculateRectangleArea(width int, length int) int {
	return width * length
}

func main() {
	fmt.Println(calculateRectangleArea(10,11))
}
```

**--- Problem 9: Introduction to Slices and Slice Iteration ---**

- **Task:** Create a Go slice of strings named `fruitList` containing: "Apple", "Orange", "Mango", "Banana". Iterate through the slice using a `for...range` loop and print each fruit name to the console on a new line.

```go
package main

import "fmt"

func main() {
	fruitList := []string{"Apple", "Orange", "Mango", "Banana"}
	for _, s := range fruitList {
		fmt.Println(s)
	}
}
```

**--- Problem 10: Functions Processing Slices ---**

- **Task:** Create a Go function named `printAllElements` that accepts one argument (a slice of strings). The function should iterate through the given slice using `for...range` and print each element to the console. Demonstrate calling it from `main` with the `fruitList` slice from Problem 9.

```go
package main

import "fmt"

func printAllElements(x []string){
	for _, s := range x {
		fmt.Println(s)
	}

}

func main() {
	fruitList := []string{"Apple", "Orange", "Mango", "Banana"}
	printAllElements(fruitList)
}
```

**--- Problem 11: String Indexing and Slicing ---**

- **Task:** Given the string `message := "Hello Go World"`, write Go code to:
  1.  Print the first character (as a byte/rune) of the string. (Hint: `message[0]`).
  2.  Print the last character (as a byte/rune) of the string. (Hint: use `len()`).
  3.  Print the substring "Go" using slice notation.

```go
package main

import "fmt"

func main() {
	message := "Hello Go World"
	fmt.Println(message[:1])
	fmt.Println(message[len(message)-1:])
	fmt.Println(message[6:8])
}
```

**--- Problem 12: Basic String Manipulation (strings package) ---**

- **Task:** Given the string `mixedCase := "Go PrOgRaMmInG"`, write Go code using the `strings` package to:
  1.  Print the string converted to all uppercase letters (`strings.ToUpper`).
  2.  Print the string converted to all lowercase letters (`strings.ToLower`).
  3.  Find and print the starting index of the substring "PrOg" (`strings.Index`). Remember to import the `strings` package.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	mixedCase := "Go PrOgRaMmInG"
	fmt.Println(strings.ToUpper(mixedCase))
	fmt.Println(strings.ToLower(mixedCase))
	fmt.Println(strings.Index(mixedCase, "PrOg"))
}
```

**--- Problem 13: Looping Through String Characters (Runes) ---**

- **Task:** Given the string "LOOP", write Go code to loop through each character (rune) of the string using `for...range` and print each character on a new line in the console.

```go
package main

import (
	"fmt"
)

func main() {
	stringz := "LOOP"
	for _, s := range stringz {
		fmt.Printf("%c\n", s)
	}
}
```

**--- Problem 14: Accessing Slice Elements and Length ---**

- **Task:** Given the slice `colors := []string{"Red", "Green", "Yellow", "Blue", "Purple"}`, write Go code to:
  1.  Print the first element of the slice.
  2.  Print the last element of the slice (Hint: use `len()`).
  3.  Print the total number of elements in the slice using `len()`.

```go
package main

import "fmt"

func main() {
	colors := []string{"Red", "Green", "Yellow", "Blue", "Purple"}
	fmt.Println(colors[0])
	fmt.Println(colors[len(colors)-1])
	fmt.Println(len(colors))
}
```

**--- Problem 15: Modifying Slices (`append`) and Checking Membership ---**

- **Task:**
  1.  Create a Go slice `planets` initialized with `[]string{"Mercury", "Venus", "Earth"}`.
  2.  Use the `append` function to add "Mars" to the _end_ of the `planets` slice. Remember `append` returns a new slice, so reassign it (`planets = append(...)`).
  3.  Print the modified `planets` slice.
  4.  Write code (e.g., a loop or a helper function) to check if "Jupiter" is present in the slice and print the boolean result (`true`/`false`).
  5.  Check if "Earth" is present in the slice and print the boolean result (`true`/`false`).

```go
package main

import (
	"fmt"
	"slices"
)

func main() {
	planets := []string{"Mercury", "Venus", "Earth"}
	planets = append(planets, "Mars")
	fmt.Println(planets)

    isEarth := false
	isJupiter := false

	for !isJupiter {
		if slices.Contains(planets, "Jupiter"){
			isJupiter = true
			fmt.Println(isJupiter)
			break
		} else {
			fmt.Println(isJupiter)
			break
		}

	}

	for !isEarth {
		if slices.Contains(planets, "Earth"){
			isEarth = true
			fmt.Println((isEarth))
			break
		}	else {
			fmt.Println(isEarth)
			break
		}
	}

}
```

**--- Problem 16: Introduction to `for` as a `while` Loop ---**

- **Task:** Write Go code using a `for` loop with only a condition (Go's equivalent of `while`) to print the numbers 0 through 4, each on a new line, to the console. Initialize a counter variable before the loop.

```go
package main

import (
	"fmt"
)

func main() {
	var counter int
	for counter < 5{
		fmt.Println(counter)
		counter += 1
	}

}
```

**--- Problem 17: `for` Loop with a Condition ---**

- **Task:** Initialize an integer variable `number` to 1. Use a `for` loop (acting as `while`) to repeatedly double the value of `number` and print it to the console. The loop should stop _before_ the number exceeds 50.

```go
package main

import "fmt"

func main() {
	number := 1
	for number < 50 {
		fmt.Println(number)
		number *= 2
	}
}
```

**--- Problem 18: Getting User Input (bufio/os/fmt) ---**

- **Task:** Write Go code that reads a line of text (the user's name) from standard input (the console). You can use `bufio.NewReader(os.Stdin).ReadString('\n')`. Remember to handle potential errors and remove the trailing newline character (e.g., using `strings.TrimSpace`). Then print a personalized greeting like "Hello, [Name]!" to the console. You'll need to import `bufio`, `fmt`, `os`, and `strings`.

```go
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	fmt.Println("Input your name:")
	reader := bufio.NewReader(os.Stdin)
	name, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Your name is", name)
}
```

**--- Problem 19: Using `else if` for Multiple Conditions ---**

- **Task:** Write Go code that gets an integer as input from the user (read as string, then convert using `strconv.Atoi`). Handle potential conversion errors. Then, print "Positive" if the number is greater than 0, "Negative" if the number is less than 0, and "Zero" if the number is exactly 0. You'll need `fmt`, `bufio`, `os`, `strings`, and `strconv`.

```go
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Insert a number:")
	reader := bufio.NewReader(os.Stdin)
	number, err1 := reader.ReadString('\n')
	number = strings.TrimSpace(number)
	numberz, err2 := strconv.Atoi(number)
	if err1 != nil{
		log.Fatal(err1)
	}
	if err2 != nil{
		log.Fatal("Please insert integer, pretty please :'(")
	}
	if numberz < 0 {
		fmt.Println("Negative")
	} else if numberz > 0 {
		fmt.Println("Positive")
	} else {
		fmt.Println("Zero")
	}
}
```

**--- Problem 20: Controlling Loop Flow (`continue`) ---**

- **Task:** Write Go code that loops through numbers from 1 to 10 (inclusive). Inside the loop, use the `continue` keyword to skip processing for even numbers. Only odd numbers should be printed to the console.

```go
package main

import "fmt"

func main() {
	for number := 0; number <= 10; number++ {
		if number%2 == 0 {
			continue
		} else {
			fmt.Println(number)
		}
	}
}
```

**--- Problem 21: Maps (Key-Value Pairs) - Creation and Access ---**

- **Task:** Create a Go map named `studentInfo` with string keys and string values to store the following:
  - `"name"`: `"Budi"`
  - `"major"`: `"Computer Science"`
  - `"id"`: `"12345"` (Store ID as string for simplicity here)
  - Print the value associated with the `"name"` key.
  - Print the value associated with the `"id"` key. Use the syntax `map[key]`.

```go
package main

import "fmt"

func main() {
	studentInfo := map[string]any{
		"name":  "Budi",
		"major": "Computer Science",
		"id":    12345,
	}

	fmt.Println(studentInfo["name"])
	fmt.Println(studentInfo["id"])
}
```

**--- Problem 22: Maps (Key-Value Pairs) - Iteration ---**

- **Task:** Using the `studentInfo` map from Problem 21, write Go code using `for...range` to:
  1.  Print all the keys of the map.
  2.  Print all the values of the map.
  3.  Print all the key-value pairs in a format like "key: value".

```go
package main

import "fmt"

func main() {
	studentInfo := map[string]any{
		"name":  "Budi",
		"major": "Computer Science",
		"id":    12345,
	}
	for key := range studentInfo {
		fmt.Println(key)
	}
	for _, value := range studentInfo {
		fmt.Println(value)
	}
	for key, value := range studentInfo {
		fmt.Println(key, ":", value)
	}
}
```

**--- Problem 23: Simulating Default Parameters in Functions ---**

- **Task:** Create a Go function `power(base, exponent int) int` that calculates `base` raised to the power of `exponent` (assume non-negative exponent) using a loop. Go doesn't have default parameters directly.
  - Demonstrate calling it from `main` as `power(5, 3)` and print the result.
  - Demonstrate calling it from `main` as `power(7, 2)` (simulating a default exponent of 2 by explicitly passing it) and print the result.

```go
package main

import "fmt"

func power(base int, exponent int) int {
	result := 1
	for i := 0; i < exponent; i++ {
		result *= base
	}
	return result
}

func main() {
	fmt.Println(power(2, 5))
}
```

**--- Problem 24: Structs for Simple Data Structures ---**

- **Task:** Define a Go struct named `Point` with two integer fields: `X` and `Y` (use uppercase for exported fields).
  1.  Create an instance of the `Point` struct with `X` as 10 and `Y` as 20.
  2.  Print the `Point` instance itself to the console using `fmt.Println` or `fmt.Printf("%+v\n", ...)`.
  3.  Print the value of the `X` field specifically.
  4.  Briefly explain (in a comment) how Go uses exported (uppercase) vs. unexported (lowercase) field names for visibility control, which relates conceptually to preventing modification from _other_ packages.

```go
package main

import "fmt"

type Point struct {
	X int
	Y int
}

func main() {
	var pointz Point

	pointz.X = 10
	pointz.Y = 20

	fmt.Println(pointz)
	fmt.Println(pointz.X)
}
```

**--- Problem 25: More Slice Manipulation (`append` for insertion/removal) ---**

- **Task:**
  1.  Start with the slice `letters := []string{"a", "b", "d", "e"}`. Print the initial slice.
  2.  Insert the letter "c" into the slice at the correct position (index 2) to maintain alphabetical order. Use `append` with slicing gymnastics (`append(slice[:index], append([]string{newItem}, slice[index:]...)...)`). Print the slice after insertion.
  3.  Remove the _last_ element from the slice using slicing (`letters = letters[:len(letters)-1]`). Print the slice after removal.
  4.  Remove the element "a" (which is now at index 0) from the slice _by its value_. You'll likely need to find its index first, then use slicing and `append` similar to insertion (`append(slice[:index], slice[index+1:]...)`). Print the final slice.

```go
package main

import "fmt"

func indexOf(slice []string, value string)int {
	for i,v := range slice {
		if v == value {
			return i
		}
	}
	return -1
}

func main() {
	letters := []string{"a", "b", "d", "e"}
	fmt.Println(letters)
	letters = append(letters[:2], append([]string{"c"}, letters[2:]...)...)
	fmt.Println(letters)
	letters = letters[:len(letters)-1]
	fmt.Println(letters)
	indexToRemove := indexOf(letters, "a")
	letters = append(letters[:indexToRemove], letters[indexToRemove+1:] ...)
	fmt.Println(letters)

}
```

**--- Problem 26: Combining Input, Loop, Slice ---**

- **Task:** Write Go code that repeatedly asks the user to enter a number or the word "done". Read the input line. If the user enters a number, try converting it to an integer using `strconv.Atoi`. If successful, add it to an integer slice using `append`. If the user enters "done" (case-insensitive, use `strings.ToLower` or `strings.EqualFold`), stop asking for input. Handle potential conversion errors gracefully (e.g., print a message and continue). After the loop finishes, print the final slice containing all the valid numbers entered.

```go
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	var number []int

	for {
		fmt.Println("Insert a number or 'done' to complete the sentence:")
		reader := bufio.NewReader(os.Stdin)
		cache, err1 := reader.ReadString('\n')
		cache = strings.TrimSpace(cache)
		if err1 != nil {
			log.Fatal(err1)
		}
		if strings.ToLower(cache) == "done"{
			break
		} else{
			cacheInt, err2 := strconv.Atoi(cache)
			if err2 != nil {
				log.Fatal(err2)
			}
			number = append(number, cacheInt)
		}
	}
	fmt.Println(number)
}
```

**--- Problem 27: Function Returning a Modified Slice ---**

- **Task:** Create a Go function `getEvenNumbers` that accepts a slice of integers (`[]int`) as an argument. The function should return a _new_ slice (`[]int`) containing only the even numbers from the original slice. Test it by calling it from `main` with `[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}` and printing the returned result slice.

```go
package main

import "fmt"

func getEvenNumbers(x []int) []int {
	var xNew []int
	for i:=0;i<len(x);i++{
		if i % 2 != 0 {
			continue
		} else {
			xNew = append(xNew, i)
		}
	}
	return xNew
}

func main() {
	slicez := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(getEvenNumbers(slicez))
}
```

**--- Problem 28: Checking Data Types (`%T` verb) ---**

- **Task:** Declare variables in Go with the following values: `20` (int), `20.3` (float64), `"Yoman"` (string), `[]int{}` (empty int slice), `map[string]int{}` (empty map), `true` (bool). Write Go code that prints the data type of each variable using `fmt.Printf` with the `%T` format specifier.

```go
package main

import "fmt"

func main() {
	dat1 := 20
	dat2 := 20.3
	dat3 := "Yoman"
	var dat4 []int
	var dat5 map[string]int
	dat6 := true

	data := []any{dat1,dat2,dat3,dat4,dat5,dat6}

	for _, dat := range data{
		fmt.Printf("%T\n",dat)
	}

}
```

**--- Problem 29: Working with Map Values ---**

- **Task:** Given the map `scores := map[string]int{"Math": 85, "Science": 92, "History": 78, "English": 88}`, write Go code to calculate and print the _average_ score. Iterate through the map's values, sum them up, and divide by the number of entries. Remember to perform floating-point division (e.g., convert sum and count to `float64` before dividing).

```go
package main

import "fmt"

func sum(num []int) int {
	sum := 0
	for _, num := range num {
		sum += num
	}
	return sum
}

func main() {
	scores := map[string]int{"Math": 85, "Science": 92, "History": 78, "English": 88}
	var value []int

	for _, valuez := range scores {
		value = append(value, valuez)
	}

	sum := float64(sum(value))
	count := float64(len(scores))

	avg := sum / count
	fmt.Println(avg)

}
```

**--- Problem 30: Putting It Together - Simple Data Processor (Structs in Slices) ---**

- **Task:** Define a `Product` struct with `Name` (string) and `Price` (float64 or int) fields. Create a slice of `Product` structs:
  ```go
  products := []Product{
      {Name: "Laptop", Price: 1200},
      {Name: "Mouse", Price: 25},
      {Name: "Keyboard", Price: 75},
      {Name: "Monitor", Price: 300},
  }
  ```
  Create a Go function `findMostExpensiveProduct(productList []Product) string` that:
  1.  Accepts the slice of `Product` structs.
  2.  Handles the case of an empty input slice gracefully (e.g., return an empty string `""`).
  3.  Finds the product with the highest price.
  4.  Returns the _name_ of the most expensive product.
      Call the function from `main` with the `products` slice and print the result in the format: "The most expensive product is: [ProductName]".

```go
package main

import (
	"fmt"
)

type Product struct {
	Name  string
	Price float64
}

func findMostExpensiveProduct(productList []Product) string {
	var result string
	var priceList []float64
	var largest float64


	if productList == nil {
		fmt.Println("List can't be empty!")
	}
	for _, key  := range productList {
		priceList = append(priceList, key.Price)
	}

	largest = priceList[0]

	for dat:= 1; dat < len(productList); dat++{
		if largest < priceList[dat] {
			largest = priceList[dat]
		} else {
			continue
		}
	}

	for _, key  := range productList {
		if key.Price == largest{
			return key.Name
		}else {
			continue
		}
	}

	return result
}

func main() {


	products := []Product{
		{Name: "Laptop", Price: 1200},
		{Name: "Mouse", Price: 25},
		{Name: "Keyboard", Price: 75},
		{Name: "Monitor", Price: 300},
	}

	fmt.Println("The most expensive product is:",findMostExpensiveProduct(products))


}
```

---
