package main

import "fmt"

type Weekday int

const (
	one   = 2*iota + 1 // 2*0+1
	three              // 2*1+1
	five               // 2*2+1
	seven              // 2*3+1
	nine
	eleven
)

/*
	 	Creating ENUMS of type WEEKDAY

		Для удобного объявления и инициализации блоков констант
		в Go есть автоматический инкремент *iota*
	 	При объявлении каждого блока const значение iota равно 0 и увеличивается на 1 для каждого следующего элемента
*/
const (
	Monday    Weekday = iota + 1 // 0 + 1 = 1
	Tuesday                      // 2
	Wednesday                    // 3
	Thursday                     // 4
	Friday                       // 5
	Saturday                     // 6
	Sunday                       // 7
)

func NextDay(day Weekday) Weekday {
	return (day % 7) + 1
}

func main() {

	fmt.Println(one, three, five, seven, nine, eleven)

	var today Weekday = Sunday
	tomorrow := NextDay(today)
	fmt.Println("today =", today, "tomorrow =", tomorrow) // today = 7 tomorrow = 1
}
