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
else:
    print("Grade: F")

# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
num = int(input("Enter number:"))
if 50<=num<=100:
    print("Number is between 50 and 100.")
else:
    print("Number is not between 50 and 100.")
# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
num2 = int(input("Enter a number:"))
if num2 != 0 and num2 > 10:
    print("Number is NOT equal to 0 and greater than 10.")
else: 
    print("Number is invalid")
# Use chained comparison to check if 3 < 4 < 5.
num3 = 4
print(num3 > 3 and num3 < 5)   # True
print(num3 < 5 or num3 == 4)   # True
print(not(num3 == 5))       # True
print(3 < 4 < 5)         # True
# Challenge: Create a password rule using logical operators:

password = int(input("Enter password (password must be a number between 200 and 700):"))
if 200<=password<=700:
    print("Password is valid")
else:
    print("Password is invalid")