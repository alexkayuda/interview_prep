package main

import (
	"errors"
	"fmt"
	"os"
	"strconv"
)

var balanceSheetTitle = "balance.txt"

func main() {
	fmt.Println("Hello! Welcome to GO Bank")

	var userInput int
	accountBalance, err := readFromFile()

	if err != nil {
		fmt.Println(err)
		fmt.Println("-----")

		// system.exit(0)
		panic("SOMETHING WENT REALLY-REALLY WRONG")
	}

	// infinite loop
	for {

		fmt.Println("How can I help you?")
		fmt.Println("1. Check Balance")
		fmt.Println("2. Deposit Money")
		fmt.Println("3. Withdraw Money")
		fmt.Println("4. Exit")

		fmt.Print("Enter your choice here: ")
		fmt.Scan(&userInput)

		if userInput == 1 {
			fmt.Println("Your Current Balance is: ", accountBalance)
		} else if userInput == 2 {
			var depositAmount float64

			fmt.Print("\nHow much would you like to deposit? Enter amount: ")
			fmt.Scan(&depositAmount)

			if depositAmount >= 0 {
				accountBalance += depositAmount
				writeToFile(accountBalance)
				fmt.Println("Balance updated. You new balance is: ", accountBalance)
			} else {
				fmt.Println("Balance could NOT be updated. Deposit amount should be greater than 0")
				continue
			}
		} else if userInput == 3 {
			var withdrawalAmount float64

			fmt.Print("\nHow much would you like to withdraw? Enter amount: ")
			fmt.Scan(&withdrawalAmount)

			if withdrawalAmount > accountBalance {
				fmt.Println("Balance could NOT be updated. Withdrawal exceeds Account Balance")
				continue
			}

			if withdrawalAmount >= 0 {
				accountBalance -= withdrawalAmount
				writeToFile(accountBalance)
				fmt.Println("Balance updated. You new balance is: ", accountBalance)
			} else {
				fmt.Println("Balance could NOT be updated. Withdrawal amount should be greater than 0")
			}

		} else if userInput == 4 {
			fmt.Println("Thanks for choosing our bank, see you later!")

			// break out of the loop
			break
		} else {
			fmt.Println("Invalid Input, try again")
		}
	}

	fmt.Println("Goodbye!")
}

func writeToFile(balance float64) {

	// convert float to string
	balanceString := fmt.Sprintln(balance)

	// create or append to the "balance.txt" file
	// convert balanceString to an array of bytes
	// 0644 permissions = readable by all the user groups but only writable by the user
	// https://chmodcommand.com/chmod-0644/
	os.WriteFile(balanceSheetTitle, []byte(balanceString), 0644)
}

func readFromFile() (float64, error) {
	data, err := os.ReadFile(balanceSheetTitle)

	if err != nil {
		// something went wrong
		fmt.Println(err)

		return 0, errors.New("Could not open a specified file")
	}

	// convert byte array to string
	balanceString := string(data)

	// convert string to float64
	balance, err := strconv.ParseFloat(balanceString, 64)

	if err != nil {
		// something went wrong
		fmt.Println(err)

		return 0, errors.New("Could not convert string to a float64")
	}

	return balance, nil
}
