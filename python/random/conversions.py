print("---" * 10)

# Convert int array to string
array = [1,2,3,4,5]

str_array = ''.join(map(str, array))

for element in str_array:
    print(f"Element: {element}, Type: {type(element)}")


print("---" * 10)

# convert string to a list of numbers
str_num = '1987'
my_list = list(str_num) # ['1', '9', '8', '7']
print(my_list)


print("---" * 10)

# Convert int to binary

num = 7
bin_num = bin(num)
print(f"Binary Representation of {num} is : {bin_num}") # 0b111
print(type(bin_num))

# remove '0b' and fill with 10 up tp 10 characters
bin_num = bin_num[2:].zfill(10)
print(f"Modified Binary Representation of {num} is : {bin_num}")
print(type(bin_num))


print("---" * 10)

# conver int to a list of str
num = 45678
num_to_str = str(num)
print(num_to_str)

num_list = [char for char in num_to_str]
print(num_list)