# prime is divisible by 1 and itself

# solves in O(n)
import math

def isPrime(number : int) -> bool:
    
    for i in range(2, number):
        if number % i == 0:
            return False

    print(f"Wow, took {number-2} iterations")
    return True

def isPrime_faster(number :int) -> bool:
    for i in range (2, math.floor(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    print(f"Wow, took {math.floor(math.sqrt(number) + 1)-2} iterations")
    return True

if __name__ == "__main__":
    print(isPrime(97))

    # sqrt(97) = 9.84
    # 9.84 + 1 = 10.84
    # floor(10.84) = 10
    print(isPrime_faster(97))