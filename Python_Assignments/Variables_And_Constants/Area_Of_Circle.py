# Program to calculate the area of a circle.

# Constant for the value of pi.
pi=3.142

# Get the radius of the circle from user input.
radius=float(input("Enter radius: "))

# Calculate the area using the formula: area = π * radius^2
area=pi*(radius**2)

# Output the result formatted to two decimal places.
print("Area of Circle is : %.2f"%area)
