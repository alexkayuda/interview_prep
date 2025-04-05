
# Idea is in copying elements over if they don't match provided value
# if it matches, then skip and move to the next one
# Return k, where k is the number of elements that were swapped.
def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    print(nums[0:k])
    return k

if __name__ == "__main__":

    array1 = [1,2,3,4,4,5,6,4,7,8,9,4]
    removeElement(array1, 4)