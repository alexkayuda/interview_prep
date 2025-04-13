'''
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

def multiply(num1: str, num2: str) -> str:
    num1_int = int(num1)
    num2_int = int(num2)

    return str(num1_int * num2_int)



num1 = "2"
num2 = "3"
print(multiply(num1, num2))

num1 = "123"
num2 = "456"
print(multiply(num1, num2))