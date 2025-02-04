package note

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"strings"
	"time"
)

type Note struct {

	// struct Tags is a built-in feature like a MetaData
	// This metadata will be used by json.Marshal
	// to replace default struct variable names with alternatives
	Title     string    `json:"title"`
	Content   string    `json:"content"`
	CreatedAt time.Time `json:"created_at"`
}

// Return Note or *Note
// Because we deal with a simple struct, Note is fine
// However, if struct is complex -> use Pointers
func New(title, content string) (Note, error) {

	if title == "" || content == "" {
		return Note{}, errors.New("invalid input")
	}

	return Note{
		Title:     title,
		Content:   content,
		CreatedAt: time.Now(),
	}, nil
}

func (note Note) Display() {
	fmt.Println("Note's Title is: ", note.Title)
	fmt.Println("Note's Content is: ", note.Content)
}

func (note Note) SaveToJsonFile() error {

	// Modify the COPY (becaused passed by value and not by reference (no *Note)) of the title
	// and use it as a File Name
	var fileName string
	fileName = strings.ReplaceAll(note.Title, " ", "_")
	fileName = strings.ToLower(fileName)
	fileName = fileName + ".json"

	//convert struct to JSON format to be written to a file
	// IMPORTANT: Marshal automatically converts structs to JSON []byte
	// IMPORTANT: Marshal REQUIRES all fields in struct to be Upper Case (exposed outside of struct)
	jsonContent, err := json.Marshal(note)

	if err != nil {
		// error converting Note to JSON format
		fmt.Println(err)
		return err
	}

	// Note: WriteFile might return an error if failed.
	// Since we are returning error in a function, we can immediately return the result of WriteFile
	return os.WriteFile(fileName, jsonContent, 0644)

}
