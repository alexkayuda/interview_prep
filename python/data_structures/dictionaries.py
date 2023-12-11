# Dictionary = HashMap
# Key-Value Pair


tel = {'jack': 4098, 'sape': 4139}

for key, value in tel.items():
        print(f"Key: {key}, Value: {value} ")

tel['guido'] = 4127

print(tel)                  # {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel['jack'])          # 4098

del tel['sape']

tel['irv'] = 4127

print(tel)                  # {'jack': 4098, 'guido': 4127, 'irv': 4127}

# only prints Keys
print(list(tel))                   # ['jack', 'guido', 'irv']

# sorts keys
print(sorted(tel))                 # ['guido', 'irv', 'jack']

print('guido' in tel)       # returns True

print('jack' not in tel)    # returns False

# -------------------------------------------------------------