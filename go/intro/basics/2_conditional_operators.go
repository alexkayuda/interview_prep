package main

import (
	"fmt"
	"runtime"
)

func main() {
	age := 30

	if age < 30 {
		fmt.Println("This is less than", age)
	} else if age > 30 {
		fmt.Println("This is greater than", age)
	} else {
		fmt.Println("This is equal to", age)
	}

	// ----------------------------------------------------------

	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}
