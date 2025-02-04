# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairsFib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return climbStairsFib(n-1) + climbStairsFib(n-2)

def climbStarsEfficient(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    previous, current = 1, 1

    for i in range(2, n+1):
        temp = current
        current = previous + current
        previous = temp

    return current

if __name__ == "__main__":
    print(climbStairsFib(10))
    print(climbStarsEfficient(10))