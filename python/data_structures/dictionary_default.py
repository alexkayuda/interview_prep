from collections import defaultdict

# default dict is a wrapper around default dict
# we can specify what we want as a value (int, list, set, ...)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


s = 'mississippi'
d = defaultdict(int)
for letter in s:
    d[letter] += 1

print(sorted(d.items()))
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

print(d['i'])