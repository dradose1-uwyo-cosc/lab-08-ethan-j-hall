# Ethan Hall
# UWYO COSC 1010
# 11.10.2024
# Lab 08
# Lab Section:
# Sources, people worked with, help given to:
# referenced in class powerpoints 
# w3 schools referenced for structure 
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_string(s):
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return int(s)

    try:
        float_value = float(s)
        
        if '.' in s and s.count('.') == 1 and len(s.split('.')[1]) == 1:
            return float_value
        
        elif '.' in s and s.count('.') > 1:
            return False

        return float_value
    except ValueError:
        return False


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_x, upper_x):

    if not isinstance(lower_x, int) or not isinstance(upper_x, int):
        return False
    if lower_x > upper_x:
        return False

    y_values = []
    x = lower_x
    
    while x <= upper_x:
        y = m * x + b 
        y_values.append(y)
        x += 1 
    
    return y_values

def get_input(prompt):
    
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            return 'exit'
        try:
 
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number (integer or float).")

while True:
    print("\nEnter the line equation parameters or type 'exit' to quit.")
    
    m = get_input("Enter the slope (m): ")
    if m == 'exit':
        break
    
    b = get_input("Enter the y-intercept (b): ")
    if b == 'exit':
        break
    
    lower_x = get_input("Enter the lower bound for x: ")
    if lower_x == 'exit':
        break
    
    upper_x = get_input("Enter the upper bound for x: ")
    if upper_x == 'exit':
        break
    
    if not isinstance(lower_x, int) or not isinstance(upper_x, int):
        print("Error: Both x bounds must be integers. Please try again.")
        continue
    
    result = slope_intercept(m, b, lower_x, upper_x)
    
    if result is False:
        print("Invalid input or logic error. Please check your bounds and try again.")
    else:
        print("The calculated y values for the given x range are:", result)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def safe_sqrt(value):
    if value < 0:
        return None  
    return math.sqrt(value)


def solve_quadratic(a, b, c):

    discriminant = b ** 2 - 4 * a * c
    sqrt_discriminant = safe_sqrt(discriminant)
    
    if sqrt_discriminant is None:
        return "No real roots"  
    
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    
    return x1, x2

def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            return 'exit'
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    print("\nSolve the quadratic equation ax^2 + bx + c = 0")
    
    a = get_input("Enter coefficient a: ")
    if a == 'exit':
        break
    
    b = get_input("Enter coefficient b: ")
    if b == 'exit':
        break
    
    c = get_input("Enter coefficient c: ")
    if c == 'exit':
        break
    
    if a == 0:
        print("Error: 'a' cannot be zero in a quadratic equation. Please try again.")
        continue
    
    result = solve_quadratic(a, b, c)
    
    if result == "No real roots":
        print("The equation has no real roots.")
    else:
        print(f"The solutions are x1 = {result[0]} and x2 = {result[1]}")
