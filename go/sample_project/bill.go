package main

import (
	"fmt"
	"os"
)

// Creating our custom "Object" that has the following fields
type bill struct {
	name  string
	items map[string]float64
	tip   float64
	total float64
}

// Constructor
// to instanciate a new Bill "Object"
func newBill(name string) bill {
	newBill := bill{
		name:  name,
		items: map[string]float64{},
		tip:   0,
		total: 0,
	}

	return newBill
}

// add item to a bill
func (myBill *bill) addItem(name string, price float64) {
	myBill.items[name] = price
	myBill.total += price
}

// update tips
func (myBill *bill) updateTip(tipValue float64) {
	myBill.tip = tipValue
	myBill.total += tipValue
}

// Receiver Function
// Allows us to ONLY be used on Bill Objects
// received a copy of the bill that was used to call this func
func (myBill *bill) format() string {
	// var total float64 = 0
	// myBill.total = 0

	formattedString := "Bill breakdown: \n"

	for key, value := range myBill.items {
		formattedString += fmt.Sprintf("%-25v ...$%v\n", key+":", value)
		// myBill.total += value
	}

	// adding tip
	formattedString += fmt.Sprintf("%-25v ...$%0.2f\n", "Tip:", myBill.tip)

	// %-25v = Insert a first value (Total:) but offset it to -25 characters to the left.
	// Meaning:  |Total:_________|
	// If, we had + 25, we would get |________Total:|
	formattedString += fmt.Sprintf("%-25v ...$%0.2f\n", "Total:", myBill.total)

	return formattedString
}

func (myBill *bill) save() {
	data := []byte(myBill.format())

	err := os.WriteFile(myBill.name+".txt", data, 0644)

	if err != nil {
		panic(err)
	} else {
		fmt.Println("Bill was saved under a name: ", myBill.name)
	}
}
