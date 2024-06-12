package main

import "fmt"

func main() {
	age := 30

	if age < 30 {
		fmt.Println("This is less than", age)
	} else if age > 30 {
		fmt.Println("This is greater than", age)
	} else {
		fmt.Println("This is equal to", age)
	}
}
