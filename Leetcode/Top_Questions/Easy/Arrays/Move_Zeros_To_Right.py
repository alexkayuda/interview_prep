'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this ***in-place*** without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

'''

def moveZeroes(nums: list[int]) -> None:
    
    if len(nums) == 1:
        print(nums)
        return
    
    slow = 0
    fast = 1

    while fast < len(nums):
        if nums[slow] != 0:
            slow += 1

        if nums[slow] == 0 and nums[fast] != 0:
            # swap
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        
        fast += 1 

    print(nums)

if __name__ == "__main__":

    nums = [0,1,0,3,12]
    moveZeroes(nums) # [1, 3, 12, 0, 0]

    nums = [1,0,1]
    moveZeroes(nums) # [1, 1, 0]

    nums = [0]
    moveZeroes(nums) # [0]

    nums = [45192,0,-659,-52359,-99225,-75991,0,-15155,27382,59818,0,-30645,-17025,81209,887,64648]
    moveZeroes(nums) # [45192,-659,-52359,-99225,-75991,-15155,27382,59818,-30645,-17025,81209,887,64648,0,0,0]

    nums = [-58305,-22022,0,0,0,0,0,-76070,42820,48119,0,95708,-91393,60044,0,-34562,0,-88974]
    moveZeroes(nums) # [-58305,-22022,-76070,42820,48119,95708,-91393,60044,-34562,-88974,0,0,0,0,0,0,0,0]