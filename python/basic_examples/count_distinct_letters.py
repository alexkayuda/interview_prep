string1 = "abcdef"	# 6
string2 = "abbcdDDef"	# 6
string3 = "a, b, 1, 2, c, c, d, D, efgb" # 7

# ------------------------------------

setOfLetters1 = set(string1)

# print(f"setOfLetters is of type: {type(setOfLetters1)}" )
print(f"string1 has {len(setOfLetters1)} distinct letters")

# ------------------------------------

setOfLetters2 = set(string2.lower())

# print(setOfLetters2)
print(f"string2 has {len(setOfLetters2)} distinct letters")

# ------------------------------------

setOfLetters3 = set()

for char in string3:
	if char.isalpha():
		setOfLetters3.add(char.lower())


#print(setOfLetters3)
print(f"string3 has {len(setOfLetters3)} distinct letters")










