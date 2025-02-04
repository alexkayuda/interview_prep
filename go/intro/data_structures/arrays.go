package main

import "fmt"

func main() {

	// array of type string of size 4
	names := [4]string{"Mike", "Jane", "Alex", "John"}
	names[0] = "Joe"

	// ages := [3]int{23, 24, 25}

	fmt.Println(names, len(names))

	// ##############################################################################
	// Slices = ArrayLists
	var scores = []int{1, 2, 3, 4}
	scores[2] = 5

	// append creates a new slice in the background
	scores = append(scores, 85)
	fmt.Println(scores, len(scores))

	// ##############################################################################
	// Slices
	rangeOne := names[1:3] // [1,3) -> Includes 1 but not 3, therefore, 1 and 2 only
	fmt.Println(rangeOne, len(rangeOne))

	rangeTwo := names[2:] // [2, last element] -> Includes from 2 to the last
	fmt.Println(rangeTwo, len(rangeTwo))
}
