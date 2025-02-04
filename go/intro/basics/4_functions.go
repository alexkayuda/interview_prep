package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {

	// names := []string{"Mike", "Steven", "Jake", "Alex"}

	// sayGreeting(names[0])
	// sayBye(names[1])

	// // passing array and a function
	// cycleNames(names, sayGreeting)

	// area := circleArea(10.7)
	// fmt.Printf("Area of a Circle is: %0.2f \n", area)

	fullName := "Joe Doe"
	firstInitial, secondInitial := getInitials(fullName)
	fmt.Println(firstInitial, secondInitial)
}

func sayGreeting(name string) {
	fmt.Println("Hello, ", name)
}

func sayBye(name string) {
	fmt.Println("Bye, ", name)
}

// this function accepts an array of strings and a function that accepts a string
func cycleNames(names []string, sayHi func(string)) {
	for _, value := range names {
		sayHi(value)
	}
}

// returns a float64 value
func circleArea(radius float64) float64 {
	return math.Pi * radius * radius
}

// get a fullName as a string and return 2 strings!
func getInitials(fullName string) (string, string) {

	// capitalize the whole name
	capitalized := strings.ToUpper(fullName)

	// split into array of strings by space character
	splitted := strings.Split(capitalized, " ")

	var initials []string
	for _, value := range splitted {
		initials = append(initials, value[:1])
	}

	if len(initials) > 1 && len(initials) <= 2 {
		return initials[0], initials[1]
	} else {
		return initials[0], "_"
	}

}
