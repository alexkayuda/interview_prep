string1 = "aaBbccdDDeef" # 6
string2 = "1, a,b,cde, ffg, gge" #7

# Option 1: use Sets
list1 = [*set(string1.lower())]
print(len(list1))

# Option 2: Loop Over
list2 = []
for char in string2:
    if char.isalpha() and char not in list2:
        list2.append(char.lower())

#print(list2)
print(len(list2))


# Option 3: Dict
dict = {}
for char in string2:
    if char in dict:
        dict[char] = dict[char] + 1
    else:
       if char.isalpha():
            dict[char] = 1

print(dict)
print(len(dict))

