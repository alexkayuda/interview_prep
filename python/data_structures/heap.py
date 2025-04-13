'''
Key Methods:
heappush(): Push an element onto the heap.

heappop(): Pop the smallest element from the heap.

heappushpop(): Push an element and pop the smallest element in one operation.

heapreplace(): Pop the smallest element and push a new element in one operation.

nlargest(): Get the n largest elements from an iterable.

nsmallest(): Get the n smallest elements from an iterable.

heapify(): Convert a list into a valid heap.
'''

import heapq as hq


# heap sort
# Pushing all values onto a heap and then 
# popping off the smallest values one at a time
def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value) # Pushing all values onto a heap
    return [hq.heappop(h) for i in range(len(h))] # popping off the smallest values one at a time

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# //////////////////////////////////////////////////////////////////////////////////

array = [25, 44, 68, 21, 39, 23, 89]

# find 3 smallest elements in array
smallest_nums = hq.nsmallest(3, array)
print(f"{smallest_nums}") # [21, 23, 25]

# find 3 largest elements
largest_nums = hq.nlargest(3, array)
print(f"{largest_nums}") # [89, 68, 44]

def find_Kth_Largest(nums: list[int], k: int) -> int:
        # h is used as a heap.
        h = []

        # Push all elements to a max heap
        # 
        # -element is used to simulate a MAX heap (min heap is the default one).
        # 
        # +element: Keeps the original element value.
        for element in nums:
            hq.heappush(h, (-element, element))


        # Pop elements from the heap until the k-th largest is found
        for i in range(k):
            negative_element, actual_element = hq.heappop(h)
            if i == k - 1:
                return actual_element

def find_Kth_Smallest(nums: list[int], k: int) -> int:
    h = []
    
    # Push all elements to a min-heap
    for element in nums:
        hq.heappush(h, element)

    # Pop the smallest elements k times
    for i in range(k):
        smallest = hq.heappop(h)
        if i == k - 1:
            return smallest

print(find_Kth_Largest(array, 3)) # 44
print(find_Kth_Smallest(array, 3)) # 25


# to turn list into a heap
# hq.heapify(array)