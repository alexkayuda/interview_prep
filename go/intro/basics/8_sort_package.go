package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func main() {

	// used generate the pseudo-random slice of n integers.
	// The array will be pseudo-random permutation of the integers in the range [0,n).
	age := rand.Perm(10)

	fmt.Println(age)

	// Sorting will MODIFY original array!!!
	sort.Ints(age)

	fmt.Println(age)
}
