# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums: list[int], k: int) -> None:

    for iteration in range(0,k):
        for index in range(0, len(nums)):
            # temp = nums[(index + 1) % len(nums)]
            # nums[(index + 1) % len(nums)] = nums[index]
            nums[index], nums[(index + 1) % len(nums)] = nums[(index + 1) % len(nums)], nums[index]

        print(nums)


if __name__ == "__main__":

    array1 = [1,2,3,4,5,6,7]
    rotate(array1, k=3) # [5,6,7,1,2,3,4]

    array2 = [-1,-100,3,99]
    # rotate(array2, k=2) # [3,99,-1,-100]