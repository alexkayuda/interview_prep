string = "qwertyuiopqwertyi" # 8

vowel = ('a', 'e', 'i', 'o', 'u', 'y') # only 6

counter = 0

for char in string:
    if char in vowel:
        counter = counter + 1

print(counter)