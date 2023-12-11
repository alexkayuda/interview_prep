package main

import "fmt"

func main() {
	menu := map[string]float64{
		"soup":  4.99,
		"pie":   7.99,
		"salad": 10.99,
	}

	fmt.Println(menu)
	fmt.Println(menu["pie"])

	// looping through maps
	for key, value := range menu {
		fmt.Println(key, " - ", value)
	}

	// update map value
	menu["soup"] = 5.99
}
