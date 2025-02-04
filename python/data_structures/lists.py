fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# filter(functions, itterable_datastructure)
filtered = set(filter(lambda x: True if x=="apple" else False, fruits))
print(filtered)

# list.append(element) - Add an item to the end of the list
fruits.append('grape')
print(fruits)


# list.insert(index, element) - Insert an item at a given position. 
fruits.insert(1, "watermellon")
print(fruits)


# list.remove(x) - Remove the first item from the list whose value is equal to x.
#                  It raises a ValueError if there is no such item.
fruits.remove("watermellon")


# list.pop([i]) - Remove the item at the given position in the list, and return it. 
#                   If no index is specified, a.pop() removes and returns the last item in the list
fruits.pop()


print(fruits)

fruits.sort(reverse=True)

print(fruits)

# list.index(x[, start[, end]]) - Return index of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#                Optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular 
#               subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.


# list.count(x) - Return the number of times x appears in the list.



# list.sort(*, key=None, reverse=False) - Sort the items of the list in place 
#               (the arguments can be used for sort customization, see sorted() for their explanation).


# list.reverse() - Reverse the elements of the list in place.


# list.copy() - Return a shallow copy of the list. Equivalent to a[:].


# list.clear() - Remove all items from the list. Equivalent to del a[:].