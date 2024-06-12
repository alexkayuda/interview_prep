package main

import (
	"fmt"
	"math/rand"
	"sort"
	"time"
)

func main() {

	// Generate Seed
	rand.Seed(time.Now().Unix())

	// used generate the pseudo-random slice of n integers.
	// The array will be pseudo-random permutation of the integers in the range [0,n).
	age := rand.Perm(10)

	fmt.Println(age)

	// Sorting will MODIFY original array!!!
	sort.Ints(age)

	fmt.Println(age)
}
