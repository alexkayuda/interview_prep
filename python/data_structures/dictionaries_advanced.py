complex_dict = {}
complex_dict['a'] = [1]
complex_dict['b'] = [1]
complex_dict['c'] = [1]

for key, value in complex_dict.items():
    print(f"{key} : {value}")

complex_dict['a'].append(2)

for key, value in complex_dict.items():
    print(f"{key} : {value}")

print("---" * 20)

emp2 = {
    'name' : 'mike',
    'age' : 30,
    'departments' : ['Dev']
}

employees = {
    "emp1" : {
        'name' : 'alex',
        'age' : 20,
        'departments' : ['Finance', 'Marketing']
},
    "emp2" : emp2,
    "emp3" : ["what", "so", "ever"]
}

print(employees)

print("---" * 20)

users = [
    (0, "Bob", "Teacher"),
    (1, "Mike", "Mechanic"),
    (2, "Rob", "IT")
]

# create a map with key = Name and value = original tuple
user_mapping = {user[1]: user for user in users}

# getting Bob's Name and Profession
_, name, prof = user_mapping["Bob"]
print(f"Name: {name}, Profession: {prof}")