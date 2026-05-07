string = "qwertyuiopqwertyi"

dict = {}

for char in string:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] = dict[char] + 1

# sort dict by key
for key, value in sorted(dict.items()):
    print(f"{key} : {dict[key]}")

print("---" * 20)

# sort dict by value (asc order) BUT it produces a list of tuples. 
for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=False):
    print(f"{key} : {dict[key]}")

print("---" * 20)

# sort dict by value (desc order)
for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} : {dict[key]}")

print("---" * 20)
