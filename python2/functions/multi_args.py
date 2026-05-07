# *args -> accepts any number of params and convert them to a tuple
# 

from functools import reduce 

def addUp(*args) -> int:
    return sum(args)

def apply(*args, operator):
    if operator == "+":
        return addUp(*args)
    elif operator == "*":
        return reduce((lambda a,b : a*b), args)
    else:
        return "Check Operator"

print(apply(1,2,3,4,5, operator="+")) # -> this will be transformed to apply((1,2,3,4,5), operator="+")
                                    # tuple (1,2,3,4,5) will be sent to a function where it can be looped over
print(apply(1,2,3,4, operator="*"))

