# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
temperature = int(input("What is today's temperature?:"))
# Prints whether it’s cold, warm, or hot using comparison operators.
if temperature <= 50:
    print("It is cold.")
else:
    if temperature >= 80:
        print("It is hot.")
    else:
        print("It is warm.")
if temperature <= -10 or temperature >= 110:
    print("Extreme temperature warning!")


# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”


# Starter Code:

