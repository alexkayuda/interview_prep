vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
vec_doubled = [x*2 for x in vec] # [-8, -4, 0, 4, 8]


# filter the list to exclude negative numbers
vec_no_negatives = [x for x in vec if x >= 0] # [0, 2, 4]


# apply a function to all the elements
vec_abs_value = [abs(x) for x in vec] # [4, 2, 0, 2, 4]


# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit_stripped = [fruit.strip() for fruit in freshfruit] # ['banana', 'loganberry', 'passion fruit']


list = [1,2,3,4,5]
double_list1 = [x*2 for x in list] # [2,4,6,8,10]


# create a list of 2-tuples like (number, square)
number_square = [(x, x**2) for x in range(6)] # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


# flatten a list using a listcomp with two 'for'
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat_matrix = [num for elem in matrix for num in elem] # [1, 2, 3, 4, 5, 6, 7, 8, 9]