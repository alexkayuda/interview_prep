package fileops

import (
	"errors"
	"fmt"
	"os"
	"strconv"
)

// NOTE: it starts with a LOWERCASE letter!!!!
// This is a private function and will not be visible outside of this package
func doSomething() {
	fmt.Println("AM I INVISIBLE???")
}

// NOTE: it starts with a UPPERCASE letter!!!!
// This tell compiler to expose this function outside of the package
// Therefore, this function will be visible outside of this package
func GetFloatFromFile(fileName string) (float64, error) {
	data, err := os.ReadFile(fileName)

	if err != nil {
		return 1000, errors.New("Failed to find a file.")
	}

	valueText := string(data)
	value, err := strconv.ParseFloat(valueText, 64)

	if err != nil {
		return 1000, errors.New("Failed to parse stored float value.")
	}

	return value, nil
}

func WriteFloatToFile(fileName string, balance float64) {
	valueText := fmt.Sprint(balance)
	os.WriteFile(fileName, []byte(valueText), 0644)
}
