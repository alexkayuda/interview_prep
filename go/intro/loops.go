package main

import "fmt"

func main() {

	// runWhileLoop()

	// runForLoop()

	names := []string{"Alex", "Mike", "Jane", "Joe"}
	loopOverNamesOne(names)
	loopOverNamesTwo(names)
}

func runWhileLoop() {
	// While  loop
	x := 0

	for x < 5 {
		fmt.Println("The value of x is:", x)
		x++
	}

	// here, the value of x is 5!
	fmt.Println("The value of x AFTER LOOP is:", x)
}

func runForLoop() {

	// For Loop
	for i := 0; i < 5; i++ {
		fmt.Println("The value of i is:", i)
	}
}

func loopOverNamesOne(names []string) {

	for i := 0; i < len(names); i++ {
		fmt.Println(names[i])
	}
}

func loopOverNamesTwo(names []string) {

	for index, value := range names {
		fmt.Printf("Index: %v\tValue: %v\n", index, value)
	}
}
