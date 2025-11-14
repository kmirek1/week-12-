# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# collections are used to store multiple items in a single variable
#lists are ordered collections of items
#lists are mutable, meaning you can chnage their content
#lists are created using brackets[]
my_list1 = [1, 2, 3, 4, 5]
#INSTEAD OF CREATING A BUNCH of variables we can create a list 
# this makes our job easier 
#when we need to manage multiple items
# performance task answer
print(my_list1)
print(type(my_list1))
print(my_list1[0]) 
print(my_list1[1:4]) 
print(my_list1[0:])
print(my_list1[-1])
my_list1.append(6)
print(my_list1)
my_list1.extend([7,8,9,10,11,12,13,14])
print(my_list1)
# add 500 more numbers 
my_list1.extend(list(range(15,515)))
print(my_list1)
my_list1.extend(list(range(515,1115)))
print(my_list1)

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
karissa_list = ['pasta', 'ice cream', 'tacos', 'shrimp','pizza']
# Print the second and last item.
print(karissa_list[1])
print(karissa_list[-1])
# Add a new item using .append().
karissa_list.append('strawberrys')
print(karissa_list)
# Remove the first item using .pop(0).
karissa_list.pop(0)
print(karissa_list)
# Reverse your list using .reverse().
karissa_list.reverse()
print(karissa_list)
# Create a list of 3 lists (matrix), and access the middle element.
matrix_list = []