# A set is an unordered collection with no duplicate elements.
# 2 ways to create a set
# 
# emptySet = set()
# notEmptySet = {"one", "two", "three"}


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} # duplicates will be removed

print(basket)                      # {'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)                 # returns True

print('crabgrass' in basket)              # returns False

# --------------------------------------------------------------------------------------------------------------------

setA = set('abracadabra')
setB = set('alacazam')

# Print unique letters in set A
print(setA)                              # {'a', 'r', 'b', 'c', 'd'}

# NOT
# exclude letters that are in Set B from Set A
print(setA - setB)                       # {'r', 'd', 'b'}

# UNION
# combine letters in Set A and Set B
print(setA | setB)                       # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

# INTERSECION
# find elements that are in Set A AND in Set B
print(setA & setB)                              # {'a', 'c'}

# EXCLUSION
# Union - Intersection
# print letters that in Set A AND in Set B BUT not in both
print(setA ^ setB)                              # {'r', 'd', 'b', 'm', 'z', 'l'}
