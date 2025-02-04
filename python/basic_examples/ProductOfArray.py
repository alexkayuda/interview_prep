from functools import reduce

def productExceptSelf(nums: list[int]) -> list[int]:

    if len(nums) == 2:
        return nums

    result = []



    return result


if __name__ == "__main__":
    # print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
    print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]