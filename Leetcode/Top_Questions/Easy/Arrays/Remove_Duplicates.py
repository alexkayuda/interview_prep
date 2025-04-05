'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/


Given an integer array nums sorted in non-decreasing order, remove the duplicates ***in-place*** such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

# Approach 1: Smart Way
# Take the list, add to set to remove duplicates, convert back to array, then sort it
# Because we need to do remove IN-PLACE, we need to modify existing array by using nums[:]


def removeDuplicatesSmart(nums: list[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


def removeDuplicates(nums: list[int]) -> int:

    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1

    slow = 0

    for i in range(1, len(nums)):

        if nums[slow] != nums[i]:
            slow += 1
            nums[slow] = nums[i]
            
    return slow + 1

if __name__ == "__main__":

    nums = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicatesSmart(nums)) # expected 5
    print(removeDuplicates(nums))

    print("---" * 20)
    for i in range(0, removeDuplicates(nums)):
        print(nums[i])