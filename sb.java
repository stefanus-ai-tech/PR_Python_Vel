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

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class sb{
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
    
    public static void main(String[] args) {
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
}




