package main

import "fmt"

func main() {

	// Resource: https://go.dev/tour/basics/11

	strings()

	integers()

	bytes()

	floats()
}

func strings() {

	// Strings
	var nameOne string = "Example String 1"
	var nameTwo = "Example 2"
	var nameThree string

	fmt.Println(nameOne, nameTwo, nameThree)

	nameTwo = "Example 22"
	nameThree = "Example 3"

	// Another way of variable declaration
	nameFour := "Example 4"

	fmt.Println(nameOne, nameTwo, nameThree, nameFour)
}

func integers() {

	// integers
	var ageOne int = 20
	var ageTwo = 30
	ageThree := 40

	fmt.Println(ageOne, ageTwo, ageThree)

	// int  int8  int16  int32  int64
	var numOne int8 = 25  // -128 to 127
	var numTwo int16 = 27 //-32768 to 32767

	fmt.Println(numOne, numTwo)

	// uint uint8 uint16 uint32 uint64 uintptr
	var numThree uint8 = 24   // 0 to 255
	var numFour uint = 124214 // big number >= 0

	fmt.Println(numThree, numFour)
}

func bytes() {

	// byte == alias for uint8 => 0 - 155
	var byteOne byte = 24

	fmt.Println(byteOne)
}

func floats() {
	// there are only 32 and 64

	var floatOne float32 = 2324.2
	var floatTwo float64 = 123.43
	floatThree := 123.24

	fmt.Println(floatOne, floatTwo, floatThree)

}
