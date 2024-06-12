package main

import "fmt"

// all values are passed by Value (a Copy of the original)
// unless Slices, Mapsm Functions
func updateNameByValue(name string) {
	name = "Jane"
}

// we accept a pointer to a string
// and then derecerence that pointer and point it to a new value
func updateNameByReference(name *string) {
	*name = "James"
}

func main() {
	name := "Mike"

	fmt.Println("Before Updating name: ", name)

	// &variable = physical address of that variable
	addressOfNameVariable := &name
	fmt.Println("Memory address of name variable is: ", addressOfNameVariable)

	// *&variable = value stored at physical address of that variable
	contentOfNameVariable := *addressOfNameVariable
	fmt.Println("Content stored at memory location is: ", contentOfNameVariable)

	updateNameByValue(name)

	fmt.Println("After Updating name By Value: ", name)

	// send a physical address of a variable to a function
	updateNameByReference(&name)
	fmt.Println("After Updating name By Reference: ", name)

}
