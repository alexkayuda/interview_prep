package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"path/filepath"
)

func generateRandomFile() {
	// Create the logs folder if it doesn't exist
	logsDir := "logs"
	if err := os.MkdirAll(logsDir, os.ModePerm); err != nil {
		fmt.Printf("Error creating logs directory: %s\n", err)
		return
	}

	// Generate a random file name
	// rand.Seed(time.Now().UnixNano())
	fileName := fmt.Sprintf("log_%d.txt", rand.Intn(100000))
	filePath := filepath.Join(logsDir, fileName)

	// Generate some random data
	randomData := fmt.Sprintf("Random data: %d\n", rand.Intn(1000000))

	// Write the random data to the file
	if err := os.WriteFile(filePath, []byte(randomData), 0644); err != nil {
		fmt.Printf("Error writing to file: %s\n", err)
		return
	}

	fmt.Printf("Generated file: %s\n", filePath)
}

func main() {
	println("Hi, I'm here!")

	// Define the handler for the root endpoint
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Set the Content-Type header to text/html
		w.Header().Set("Content-Type", "text/html")

		// Write a simple HTML response
		fmt.Fprintln(w,
			`<!DOCTYPE html>
			<html>
			<head>
				<title>Hello World</title>
			</head>
			<body>
				<h1>Hello, World!</h1>
				<h2>Some Logs are Generated and Saved to /logs folder. COPY IT</h2>
			</body>
			</html>`)
	})

	// Generate a random file when the server starts
	generateRandomFile()

	// Start the server on port 3000
	fmt.Println("Server is listening on port 3000...")
	err := http.ListenAndServe(":3000", nil)
	if err != nil {
		fmt.Printf("Error starting server: %s\n", err)
	}
}
