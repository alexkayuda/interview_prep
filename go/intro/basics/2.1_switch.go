package maine

import (
	"fmt"
	"os"
	"time"
)

func main() {

	var age int
	var year_born int
	var groupName string

	fmt.Print("Введите возраст: ")
	fmt.Fscan(os.Stdin, &age)

	currentYear := time.Now().Year()
	year_born = currentYear - age

	switch {
	case year_born >= 1946 && year_born <= 1964:
		groupName = "бумер"
	case year_born >= 1965 && year_born <= 1980:
		groupName = "представитель"
	case year_born >= 1981 && year_born <= 1996:
		groupName = "миллениал"
	case year_born >= 1997 && year_born <= 2012:
		groupName = "зумер"
	case year_born >= 2013:
		groupName = "альфа"
	default:
		groupName = "undefined"
	}
	fmt.Println("Привет, " + groupName + "!\n")
	fmt.Println("------")

	a := -100

	switch {
	case a > 0:
		if a%2 == 0 {
			break // exit switch
		}
		fmt.Println("Odd positive value received")
	case a < 0:
		fmt.Println("Negative value received")

		/*
			У ключевого слова fallthrough есть особенности:
				- его можно использовать только в последней строке case, иначе будет ошибка компиляции;
				- оно игнорирует условие следующего по порядку case.
		*/
		fallthrough
	default:
		fmt.Println("Default value handling")
	}
}
