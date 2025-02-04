package main

import "fmt"

func main() {
	age := 20
	name := "Mike"

	// manually add values
	fmt.Println("Hello,", name, ". You are:", age, "years old!")

	// FORMAT SPECIFIERS

	// insert values into placeholders
	fmt.Printf("Hello, %v. You are: %v years old!\n", name, age)

	// insert values into placeholders and wrap them around with ""
	fmt.Printf("Hello, %q. You are: %v years old!\n", name, age)

	// print type of a variable
	fmt.Printf("Age is of type: %T\n", age)

	// Format floats
	fmt.Printf("You have scored %f points!\n", 123.25)
	fmt.Printf("You have scored %0.2f points!\n", 123.25)

	// Saved Formated String
	var savedString = fmt.Sprintf("Hello, %v. You are: %v years old!\n", name, age)
	fmt.Println(savedString)
}
