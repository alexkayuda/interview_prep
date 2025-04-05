'''
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


'''
import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original_array = nums
        

    def reset(self) -> list[int]:
        return self.original_array
        

    def shuffle_Fast(self) -> list[int]:

        # random.shuffle(arr) - shuffles elements in a list arr IN PLACE (MODIFIES THE ORIGINAL LIST)
        # return random.shuffle(self.original_array)

        # random.sample(arr) - shuffles elements in a list and returns a COPY (DOESN'T MODIFY THE ORIGINAL)
        # return a COPY of a shuffled array, instead of modifying the original one
        return random.sample(self.original_array, len(self.original_array))
        
    '''

    def shuffle_SLOW(self) -> list[int]:
        # Generate all premutations and store in a list as tupples
        results = self.__permute(self.original_array)

        # Choose a random number between 0 and a len(list) - 1
        random_number = random.choice([0, len(results) - 1])

        # return list[random number]
        return results[random_number]
        

    def __permute(self, nums: list[int]) -> list[int]:
            
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
        
    '''
        

class ArrayShuffler:

    nums = [1,2,3]

    obj = Solution(nums)

    param_1 = obj.reset()
    print(param_1)

    param_2 = obj.shuffle_Fast()
    print(param_2)

    param_3 = obj.reset()
    print(param_3)