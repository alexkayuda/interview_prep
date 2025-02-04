import subprocess

def run_tasklist():
    # Run 'tasklist' command to see the list of running processes
    #command = ['tasklist']

    # Run 'systeminfo' to get details about the machine
    command = ['systeminfo']

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        universal_newlines=True
    )

    # Display output as it comes
    for line in process.stdout:
        print(line, end='')

    for line in process.stderr:
        print(line, end='', flush=True)

    return_code = process.wait()
    print(f"tasklist command finished with exit code {return_code}")

if __name__ == "__main__":
    run_tasklist()
