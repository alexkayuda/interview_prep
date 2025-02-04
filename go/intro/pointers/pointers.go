package main

import "fmt"

func main() {

	// use & to get the pointer to the address of a variable
	// use * to get the value that a pointer points to

	age := 32

	// create an int pointer that points to the address of a variable age
	var agePointer *int = &age
	// agePointer := &age

	fmt.Println("memory address of age variable is: ", agePointer)
	fmt.Println("value stored in an age variable is: ", *agePointer) //de-referencing a pointer

	// passed by value
	adultYears := getAdultYearsValue(age)
	fmt.Println("Passed by Value: ", adultYears)

	// passed by reference
	adultYears = getAdultYearsReference(agePointer)
	fmt.Println("Passed by Reference: ", adultYears)

}

// passed by value
func getAdultYearsValue(age int) int {
	return age - 18
}

// passed by reference
func getAdultYearsReference(age *int) int {
	return *age - 18
}
