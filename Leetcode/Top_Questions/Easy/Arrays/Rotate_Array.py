'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

def rotate_left_in_place(nums: list[int], k: int) -> None:

    k = k % len(nums)

    for iteration in range(0,k):
        for index in range(0, len(nums)-1):
            nums[index], nums[(index + 1) % len(nums)] = nums[(index + 1) % len(nums)], nums[index]

        print(nums)

def rotate_right_in_place(nums: list[int], k: int) -> None:

    k = k % len(nums)

    # if k == len(nums), then we don't need to rotate at all since it's gonna be the same as original array
    if k != 0:
        nums[:k], nums[k:] = nums[-k:], nums[:-k]

    print(f"Rotate Right: {nums}")



if __name__ == "__main__":
    
    nums = [1,2,3,4,5,6,7]
    k = 4
    rotate_left_in_place(nums,k) # [4, 5, 6, 7, 1, 2, 3]

    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate_right_in_place(nums,k) # [5, 6, 7, 1, 2, 3, 4]
