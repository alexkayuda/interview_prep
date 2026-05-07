def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

if __name__ == "__main__":

    #ask_ok("Is all good? : ") # will retry 4 times with error message = "please try again"
    
    ask_ok("R U 4 Real? : ", retries=2, reminder="Nope, wrong answer!")