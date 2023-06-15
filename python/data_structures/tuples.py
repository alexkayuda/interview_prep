# Tuples are immutable
# 
# tuples can be declared in 2 ways:
# tupple1 = ("one", 2, "three")
# tupple2 = 4, 5, "six" 
# 
#
# Tuples can also be nested:
# v = ([1, 2, 3], [3, 2, 1])


t = 12345, 54321, 'hello!'

print(t[0]) # 12345

print(t) # (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)

print(u) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))