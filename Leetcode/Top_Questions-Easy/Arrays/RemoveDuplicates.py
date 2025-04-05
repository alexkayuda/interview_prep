# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def removeDuplicatesSAVAGE(nums: list[int]) -> int:

    # num = sorted(set(nums)) # this will take O(n) space but we need to do it IN PLACE
    nums[:] = sorted(set(nums)) # "slice" original list and sort a set

    return len(nums)

def removeDuplicates(nums: list[int]) -> int:
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow + 1] = nums[fast]
            fast += 1
            slow += 1

    return slow + 1

if __name__ == "__main__":

    array1 = [0,1,2,3,4,4,5]

    print(array1[0:removeDuplicates(array1)])
    print(array1[0:removeDuplicatesSAVAGE(array1)])

