# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
# two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    nums1[m:] = nums2
    nums1.sort()

    print(nums1)


if __name__ == "__main__":

    array1 = [1,3,5,7,8,9]
    array2 = [1,2,3,4,10,19]
    merge(array1, len(array1), array2, len(array2))