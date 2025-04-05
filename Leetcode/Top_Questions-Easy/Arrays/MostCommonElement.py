import math
from typing import List


# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

def majorityElement(nums: List[int]) -> int:
    sortedList = sorted(nums)

    return sortedList[math.floor(len(nums) / 2)]

if __name__ == "__main__":
    array1 = [2,2,1,1,1,2,2,3,4,5,6]

    print(majorityElement(array1))