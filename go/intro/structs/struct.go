package main

import (
	"fmt"

	"example.com/structs/user"
)

func main() {
	firstName := getUserData("Please enter your first name: ")
	lastName := getUserData("Please enter your last name: ")
	birthdate := getUserData("Please enter your birthdate (MM/DD/YYYY): ")

	appUser, err := user.New(firstName, lastName, birthdate)

	// User constuction error occured
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("--- User Struct Method ---")
	appUser.GetUserData()

	// fmt.Println("--- Clearing data is NOT avaialbe because method is PRIVATE ---")
	// appUser.clearUser()

	// ----------- ADMIN -----------

	admin, err := user.NewAdmin("test@example.com", "passw0rd", appUser)

	// User constuction error occured
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("--- Admin's Inherited Struct Method ---")
	admin.GetUserData()

}

func getUserData(promptText string) string {
	fmt.Print(promptText)
	var value string
	fmt.Scanln(&value)
	return value
}
