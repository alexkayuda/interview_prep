package main

import (
	"fmt"
	"strings"
)

func main() {
	greeting := "Hello World! It's me!"

	fmt.Println(greeting)

	fmt.Println(strings.Contains(greeting, "Hello")) //true
	fmt.Println(strings.ReplaceAll(greeting, "Hello", "Hi"))
	fmt.Println(strings.ToUpper(greeting))
	fmt.Println(len(strings.Split(greeting, " ")))
}
