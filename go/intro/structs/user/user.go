package user

import (
	"errors"
	"fmt"
	"time"
)

// Upper case is used to export / make it visible outside of this file
type User struct {
	firstName string
	lastName  string
	birthDate string

	// createdAt is also a struct (from std lib)
	createdAt time.Time
}

// STRUCT EMBEDDING (Inheritance)
type Admin struct {
	email    string
	password string
	User     // pointing to the User struct
}

func NewAdmin(email string, password string, user *User) (*Admin, error) {
	return &Admin{
		email:    email,
		password: password,
		User:     *user,
		// User: User{
		// 	firstName: "ADMIN",
		// 	lastName:  "ADMIN",
		// 	birthDate: "--/--/1900",
		// 	createdAt: time.Now(),
		// },
	}, nil
}

// Constructor!
func New(firstName, lastName, birthdate string) (*User, error) {

	if firstName == "" || lastName == "" || birthdate == "" {
		return nil, errors.New("firstName, lastName, dob must be specified")
	}

	return &User{
		firstName: firstName,
		lastName:  lastName,
		birthDate: birthdate,
		createdAt: time.Now(),
	}, nil
}

// To associate METHOD (same as func but called method when in struct) with struct
// RECEIVER ARGUMENT
func (user User) GetUserData() {
	fmt.Println(user.firstName)
	fmt.Println(user.lastName)
	fmt.Println(user.birthDate)
	fmt.Println(user.createdAt)
}

// if we don't create a pointer, user object will be passed as value and won't change the struct
// this is a PRIVATE method
func (user *User) ClearUser() {
	user.firstName = ""
	user.lastName = ""
	user.birthDate = ""
}
