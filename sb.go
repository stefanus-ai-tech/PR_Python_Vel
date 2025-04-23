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