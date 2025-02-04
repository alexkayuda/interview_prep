package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getInput(prompt string, reader *bufio.Reader) (string, error) {
	// Print a Prompt
	fmt.Print(prompt)

	// wait for "Enter" to be pressed (Enter == \n)
	input, error := reader.ReadString('\n')

	return strings.TrimSpace(input), error
}

func promptOptions(myBill bill) {
	// Create a Reader Object to read from stdin
	reader := bufio.NewReader(os.Stdin)

	// wait for "Enter" to be pressed (Enter == \n)
	options, _ := getInput("Choose Options:\n\ta - add item\n\ts - save bill\n\tt - add tip\nYour Input: ", reader)

	switch options {
	case "a":
		{
			name, _ := getInput("Item Name: ", reader)
			price, _ := getInput("Item Price: ", reader)

			//covert price string to float64
			convertedPrice, err := strconv.ParseFloat(price, 64)

			if err != nil {
				fmt.Println("Unable to parse. A price must be a number. Aborting...")
				promptOptions(myBill)
			}

			// add item to a user's bill
			myBill.addItem(name, convertedPrice)
			fmt.Printf("%v for a price of $%v was added to your bill\n", name, price)

			// return user to a prompt menu
			promptOptions(myBill)
		}
	case "t":
		{
			tip, _ := getInput("Enter Tip Amount ($): ", reader)

			convertedTip, err := strconv.ParseFloat(tip, 64)

			if err != nil {
				fmt.Println("Unable to parse. A price must be a number. Aborting...")
				promptOptions(myBill)
			}

			// Add tip to a user's bill
			myBill.updateTip(convertedTip)
			fmt.Printf("You have tipped $%v. Thank you!\n", tip)

			// return user to a prompt menu
			promptOptions(myBill)
		}
	case "s":
		{
			fmt.Println(myBill)
			myBill.save()

		}
	default:
		{
			fmt.Println("Invalid option. Try again...")
			promptOptions(myBill)
		}
	}
}

func generateBill() bill {
	// Create a Reader Object to read from stdin
	reader := bufio.NewReader(os.Stdin)

	name, _ := getInput("Create a new bill name: ", reader)

	b := newBill(name)
	fmt.Println("Name on the bill is: ", b.name)

	return b
}

func main() {

	bill := generateBill()
	promptOptions(bill)
	fmt.Println(bill.format())
}

// to run: go run main.go bill.go
