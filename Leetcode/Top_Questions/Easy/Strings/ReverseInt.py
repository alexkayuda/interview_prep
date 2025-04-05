'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''

import math

def reverseInt(num: int) -> int:

    # INT_MIN = -2**31
    # INT_MAX= 2**31 - 1

    INT_MIN = math.pow(2, 31) * -1
    INT_MAX= math.pow(2, 31) - 1
    isNegative = False


    if num < 0:
        isNegative = True
        num = num * -1
    
    if num % 10 == 0:
        num = num // 10

    # convert num to str
    num_str = str(num)

    # conver str to array of ints
    num_digits = [int(digit) for digit in num_str]

    # reverse digits
    # IMPORTANT! CONVERTS THE ORIGINAL ARRAY
    num_digits.reverse()

    # convert all digits to str
    result_str = "".join(map(str, num_digits))

    # convert str to int
    result = int(result_str)

    if isNegative:
        result = result * -1
    
    if result > INT_MAX or result < INT_MIN:
        return 0
    
    return result

if __name__ == "__main__":

    x = 123
    print(reverseInt(x)) # 321

    x = -123
    print(reverseInt(x)) # -321

    x = 120
    print(reverseInt(x)) # 21