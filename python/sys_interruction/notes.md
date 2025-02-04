# OS vs SYS modules

## os module:
The os module provides a way to interact with the operating system in a way that is portable across different platforms. It contains functions to interact with the file system, directories, processes, and other OS-level features.

### Common os functionalities:
- File and directory manipulation: 
  - Creating, removing, and changing directories, listing files, etc.
    - `os.mkdir()`, `os.remove()`, `os.rmdir()`, `os.listdir()`, `os.rename()`, etc.
  - Environment variables: Accessing or modifying environment variables.
    - `os.environ`, `os.getenv()`, `os.putenv()`, etc.
  - Path manipulation: Functions to work with paths.
    - `os.path.join()`, `os.path.exists()`, `os.path.isfile()`, `os.path.isdir()`, etc.
  - Working with processes: Functions to interact with processes.
    - `os.system()`, `os.spawn()`, `os.fork()`, etc.

``` python3
import os

# Get the current working directory
print(os.getcwd())

# List files in a directory
print(os.listdir('.'))

# Create a new directory
os.mkdir('new_folder')
```

---

## sys module
The sys module provides access to variables and functions that interact directly with the Python interpreter. It is more focused on the Python runtime environment and command-line arguments.

### Common sys functionalities:
- Command-line arguments: Accessing arguments passed to the script via the command line.
    - `sys.argv`
- Exiting a program: Terminating a program with a specific exit status.
    - `sys.exit()`
- Interpreter information: Retrieving details about the Python interpreter and environment.
    - `sys.version`, `sys.executable`, `sys.platform`, etc.
- Standard I/O: Redirecting or managing standard input, output, and error streams. 
  - `sys.stdin`, `sys.stdout`, `sys.stderr`

``` python3
import sys

# Print command-line arguments
print("Arguments passed to the script:", sys.argv)

# Exit the program with a specific exit code
sys.exit(0)

```