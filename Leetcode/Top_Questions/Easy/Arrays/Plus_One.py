'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 2:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
'''

def plusOne(digits: list[int]) -> list[int]:

    for index in range(len(digits) -1, -1, -1):
        if digits[index] + 1 < 10:
            digits[index] += 1
            return digits
        else:
            digits[index] = 0

        # we only get to this point if we had [9, 9, 9, 9, 9]
        if index == 0:
            digits.insert(0, 1) # at INDEX=0 insert 1
            return digits


if __name__ == "__main__":

    digits = [4,3,2,1]
    print(f"Final Result: {plusOne(digits)}")

    digits = [4,3,9]
    print(f"Final Result: {plusOne(digits)}")

    digits = [9,9]
    print(f"Final Result: {plusOne(digits)}")