package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"example.com/notes/note"
)

/*
Objective:
 1. Get User Input:
    Note's Title and Note's Content
 2. Parse and store it in JSON format on a computer
*/
func main() {

	// get title and content from user
	title, content := getNoteData()

	// create an instance of type Note using Note's Constructor
	userNote, err := note.New(title, content)

	// check if there were any problems create a Note Object
	if err != nil {
		fmt.Println(err)
		return
	}

	// Validate by Printing Note's details
	// userNote.Display()

	// Generate file and save it
	err = userNote.SaveToJsonFile()

	if err != nil {
		fmt.Println("Saving a note failed")
		fmt.Println(err)
		return
	} else {
		fmt.Println("Saving a note succeeded")
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
