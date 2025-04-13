# Problem
# Given 2 numbers, find there Greatest Common Divisor
import math

# Divide the larger number by the smaller number: Find the remainder. 
# Replace the larger number with the smaller number, and the smaller number with the remainder: . 
# Repeat the process: Continue dividing the new larger number by the new smaller number until you reach a remainder of 0. 
# The last non-zero remainder is the GCD: . 
# Example: 
# Find the GCD of 48 and 18:
# 48 / 18 = 2 remainder 12
# 18 / 12 = 1 remainder 6
# 12 / 6 = 2 remainder 0
# Therefore, GCD(48, 18) = 6. 
def find_GCD(num1: int, num2: int) -> int:
    
    whole = 0
    remainder = float("INF")
    result = 0

    while remainder > 0:
        whole = num1 // num2
        remainder = num1 - (num2 * whole)

        if remainder == 0:
            return result
        else:
            result = remainder
            num1 = num2
            num2 = remainder

def find_GCD_Strings(str1: str, str2: str) -> str:
    if str1 + str2 == str2 + str1:
        index = math.gcd(len(str1), len(str2))
        return str1[0:index]
    else:
        return ""


# Option 1: Just use math.gcd(num1, num2)
print(math.gcd(2378, 1769))

# Option 2: my implimentation of int GCD
print(find_GCD(18, 12))
print(find_GCD(2378, 1769))

# Option 3: my implimentation of str GCD
str1 = "ABCABC"
str2 = "ABC"
print(find_GCD_Strings(str1, str2)) # ABC

str1 = "ABABAB"
str2 = "ABAB"
print(find_GCD_Strings(str1, str2)) # AB



