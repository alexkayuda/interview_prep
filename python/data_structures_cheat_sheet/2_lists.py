# ---------------------------------------------------------------------------------------------
#
# Create an empty list using square brackets.
numbers = []
print(numbers) # Output: []

# Create an empty list using list().
numbers = list()
print(numbers) # Output: []

# Create a list of numbers.
numbers = [1, 2, 3]
print(numbers) # Output: [1, 2, 3]

# Create a list of numbers in a range.
numbers = list(range(1, 4))
print(numbers) # Output: [1, 2, 3]

# ---------------------------------------------------------------------------------------------
#
# Access elements of a list by indexing.
str_list = ["hey", "there!", "how", "are", "you?"]
print(str_list[0]) # Output: "hey"
print(str_list[len(str_list) - 1]) # Output: "you?"
print(str_list[-1]) # Output: "you?"

# Slicing a list.
str_list = ["hey", "there!", "how", "are", "you?"]
print(str_list[2:]) # Output: ["how", "are", "you?"]
print(str_list[:2]) # Output: ["hey", "there!"]
print(str_list[-3:]) # Output: ["how", "are", "you?"]
print(str_list[:-3]) # Output: ["hey", "there!"]
print(str_list[1:4]) # Output: ["there!", "how", "are"]
# Get a copy of list by slicing.
print(str_list[:]) # Output: ["hey", "there!", "how", "are", "you?"]

# Append to a list.
numbers = [1, 2]
print(numbers) # Output: [1, 2]
numbers.append(3)
print(numbers) # Output: [1, 2, 3]

# Insert item to a list.
greeting = ["how", "you?"]
greeting.insert(1, "are")
print(greeting) # Output: ["how", "are", "you?"]

# pop() Removes and returns the last element of the list lst.
numbers = [1, 2, 3]
num = numbers.pop()
print(num) # Output: 3
print(numbers) # Output: [1, 2]

# remove(x) Removes and returns the first occurrence of element x in the list lst.
numbers = [1, 2, 99, 4, 99]
numbers.remove(99)
print(numbers) # Output: [1, 2, 4, 99]

# ---------------------------------------------------------------------------------------------
#
# .reverse() Reverses the order of elements in the list lst.
lst = [1, 2, 3, 4]
lst.reverse()
print(lst) # Output: [4, 3, 2, 1]

# sort() Sorts the elements in the list lst in ascending order.
lst = [88, 12, 42, 11, 2]
lst.sort() 
print(lst) # Output: [2, 11, 12, 42, 88]

lst.sort(reverse=True)
print(lst) # Output: [88, 42, 12, 11, 2]

# Sort ints by the first digit
# (converts each num to str, takes the first 'letter' (or a digit) and sorts)
lst.sort(key=lambda x: str(x)[0])
print(lst) # Output: [11, 12, 2, 42, 88]

# ---------------------------------------------------------------------------------------------
#
# count(x) Counts the number of occurrences of element x in the list lst.
numbers = [1, 2, 42, 2, 1, 42, 42]
print(numbers.count(42)) # Output: 3
print(numbers.count(2)) # Output: 2


# index(x) Returns the position (index) of the first occurrence of value x in the list lst.
array = ["Alice", 42, "Bob", 99]
print(array.index("Alice")) # Output: 0

# search for 99 from range [1,2]
print(array.index(99, 1, 3)) # Output: ValueError: 99 is not in list

# ---------------------------------------------------------------------------------------------
#
# Concatenate lists.
numbers = [1, 2]
strings = ["Hey", "there"]
print(numbers + strings) # Output: [1, 2, "Hey", "there"]
print(numbers.extend(strings)) # Output: [1, 2, "Hey", "there"]

# Mutate a list, that is, change its contents.
numbers = [1, 2, 3]
numbers[0] = 100
print(numbers) # Output: [100, 2, 3]
numbers[0:2] = [300, 400]
print(numbers) # Output: [300, 400, 3]
numbers[1:3] = []
print(numbers) # Output: [300]
numbers[:] = []
print(numbers) # Output: []