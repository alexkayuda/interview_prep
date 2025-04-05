'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

from typing import Dict, List

def twoSum(nums: list[int], target: int) -> list[int]:

    # Annotating a dictionary with int as key and list of ints as value
    #occurrences: Dict[int, list[int]] = {}

    occurrences = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in occurrences:
            return [occurrences[complement], i]
        
        occurrences[nums[i]] = i
    
    # No solution found
    return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))

    nums = [3,3]
    target = 6
    print(twoSum(nums, target))