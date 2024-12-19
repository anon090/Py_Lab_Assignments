# Program to calculate the average of three numbers.

# Get input for the three numbers and convert them to float for decimal support.
number1=float(input("Enter value of number 1: ")) # First number user input.
number2=float(input("Enter value of number 2: ")) # Second number user input.
number3=float(input("Enter value of number 3: ")) # Third number user input.

# Calculate the average of the three numbers : formula: average=(sum of all numbers of elements)/(total number of elements)
average=(number1+number2+number3)/3 

# Print the average, formatted to two decimal places.
print("Average of Three Numbers is : %.2f"%average) 
 
