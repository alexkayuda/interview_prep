import heapq as heap

# ---------------------------------------------------------------------------------------------
# 
print("----- MIN HEAP -----")

myList = [9, 5, 4, 1, 3, 2]
heap.heapify(myList)            # turn myList array into a Min Heap (modifies the original)
print(myList)                   # => [1, 3, 2, 5, 9, 4]
print(myList[0])                # first value is always the smallest in the heap

# create array to store heap
heap_list = []
for item in myList:
    heap.heappush(heap_list, item)

heap.heappush(heap_list, 10)    # insert 10
x = heap.heappop(heap_list)     # pop and return smallest item
print(x)                        # => 1


# ---------------------------------------------------------------------------------------------

print("----- MAX HEAP -----")

myList = [9, 5, 4, 1, 3, 2]
myList = [-val for val in myList] # multiply by -1 to negate
heap.heapify(myList)

print(myList)

x = heap.heappop(myList)
print(-x) # => 9 (making sure to multiply by -1 again)

# ---------------------------------------------------------------------------------------------

print("----- HEAP Sort -----")

# Pushing all values onto a heap and then 
# popping off the smallest values one at a time
def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value) # Pushing all values onto a heap
    return [hq.heappop(h) for i in range(len(h))] # popping off the smallest values one at a time

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# ---------------------------------------------------------------------------------------------

array = [25, 44, 68, 21, 39, 23, 89]

# find 3 smallest elements in array
smallest_nums = hq.nsmallest(3, array)
print(f"{smallest_nums}") # [21, 23, 25]

# find 3 largest elements
largest_nums = hq.nlargest(3, array)
print(f"{largest_nums}") # [89, 68, 44]