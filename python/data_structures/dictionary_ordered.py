from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4


for key, value in ordered_dict.items():
    print(f"Key: {key} and Value: {value}")

'''
Key: a and Value: 1
Key: b and Value: 2
Key: c and Value: 3
Key: d and Value: 4
'''

print('---' * 20)

del ordered_dict['c']
ordered_dict['c'] = 5
ordered_dict['w'] = 3


for key, value in ordered_dict.items():
    print(f"Key: {key} and Value: {value}")

'''
Key: a and Value: 1
Key: b and Value: 2
Key: d and Value: 4
Key: c and Value: 5
Key: w and Value: 3
'''

print('---' * 20)

# reverse the order of the dictionary BY KEY (latest inserted element becomes first)
reversed_ordered_dict = OrderedDict(reversed(list(ordered_dict.items())))

for key, value in reversed_ordered_dict.items():
    print(f"Key: {key} and Value: {value}")

'''
Key: w and Value: 3
Key: c and Value: 5
Key: d and Value: 4
Key: b and Value: 2
Key: a and Value: 1
'''

print('---' * 20)

# SORT BY Value (smallest to largest)
sorted_by_value_asc = dict(sorted(ordered_dict.items(), key=lambda item: item[1]))

'''
Key: a and Value: 1
Key: b and Value: 2
Key: w and Value: 3
Key: d and Value: 4
Key: c and Value: 5
'''

for key, value in sorted_by_value_asc.items():
    print(f"Key: {key} and Value: {value}")

print('---' * 20)

# SORT BY Value (largest to smallest)
sorted_by_value_desc = dict(sorted(ordered_dict.items(), key=lambda item: item[1], reverse=True))

for key, value in sorted_by_value_desc.items():
    print(f"Key: {key} and Value: {value}")

'''
Key: c and Value: 5
Key: d and Value: 4
Key: w and Value: 3
Key: b and Value: 2
Key: a and Value: 1
'''

print('---' * 20)