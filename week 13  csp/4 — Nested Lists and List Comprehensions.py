list1 = [1,2,3]
list2 = [4,5,6]
nested_list = [list1,list2]
print(nested_list)
print(nested_list[1][2]) #output = 6

#2d list
fruits = ["apples", "oranges", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries[1][2]) #output = "potatoes"
print(groceries[0][0]) #apples
print(groceries[0]) #fruits list
print(groceries[0][2])

groceries = [["apples", "oranges", "banana", "coconut"],["celery", "carrots", "potatoes"],["chicken", "fish", "turkey"]]
#nested "for" loop
for collection in groceries:
    print(collection)
    for food in collection:
        print(food, end=" ")
    print()


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

#nested "for" loop
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()




# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2]) 
print(matrix[0][0])

# List comprehension

first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix = [
    [9, 6, 5],
    [4, 5, 7],
    [16, 8, 90]
]
# Print the first list.
print(matrix[0])
# Print the second item from the third list.
print(matrix[2][1])
# Use a list comprehension to extract the last item from each sub-list.
com_list = [row[2] for row in matrix]
print(com_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squared_nums = [x**2 for x in range (1,1)]