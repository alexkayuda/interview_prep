'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

*** You must write an algorithm that runs in O(n) time and without using the division operation. ***
'''

def productExceptSelf(nums: list[int]) -> list[int]:
    output = [1] * len(nums)
    
    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]
    
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output

if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
    print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]