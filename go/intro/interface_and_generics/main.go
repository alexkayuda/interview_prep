package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"example.com/notes/note"
	"example.com/notes/todo"
)

// Go Convention states that if there is only 1 method is defined in an interface
// we should name interface as follows:
// Method Name + ER
// Example: Save -> Saver OR Print -> Printer
type Saver interface {
	SaveToJsonFile() error
}

func main() {

	// ----- NOTE -----

	// get title and content from user
	title, content := getNoteData()

	// create an instance of type Note using Note's Constructor
	userNote, err := note.New(title, content)

	// check if there were any problems create a Note Object
	if err != nil {
		fmt.Println(err)
		return
	}

	err = saveData(userNote)

	if err != nil {
		return
	}

	// ----- TODO ------
	todoText := getUserInput("Enter TODO Text: ")

	todoNote, err := todo.New(todoText)
	todoNote.Display()
	err = saveData(todoNote)

	if err != nil {
		return
	}

}

func getNoteData() (string, string) {
	noteTitle := getUserInput("Note's Title: ")
	noteContent := getUserInput("Note's Content: ")

	return noteTitle, noteContent
}

func getUserInput(prompt string) string {
	fmt.Printf("%v ", prompt)

	// we are expecting a command line input -> os.Stdin
	reader := bufio.NewReader(os.Stdin)

	// Accept an input until we hit a line breat
	// // IMPORTANT to have a '' here because we treat it as a single character
	input, err := reader.ReadString('\n')

	if err != nil {
		return ""
	}

	// We need to modify the accepted sting because it contains a line break ('/n') at the end
	input = strings.TrimSuffix(input, "\n")
	input = strings.TrimSuffix(input, "\r")

	return input
}

func saveData(data Saver) error {

	err := data.SaveToJsonFile()

	if err != nil {
		fmt.Println("Saving failed")
		fmt.Println(err)
		return err
	} else {
		fmt.Println("Saving succeeded")
		return nil
	}
}
