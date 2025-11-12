# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

# score calculator
score = int(input("Enter your score (0-100):"))
# if the score is between 90 and 100
#assign grade A
if 90 <= score <= 100:
    print("Grade: A")
#if score is between 80 and 89
# assign grade B
elif 80<= score <= 89:
    print("Grade: B")
#if score is between 70 and 79
#assign grade C
elif 70 <= score <= 79:
    print("Grade: C")
#if score is between 60 and 69
#assign grade D
elif 60 <= score <= 69:
    print("Grade: D")
# if score is 50 or below assign grade F
# assign grade F
else 0 <= score <= 50:
    print("Grade: F")

# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
num = int(input("Enter number:"))
if 50<=num<=100:
    print("Number is between 50 and 100.")
else:
    print("Number is not between 50 and 100.")
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

