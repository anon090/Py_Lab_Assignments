# Program to calculate simple interest based on user input for principal amount, rate of interest, and number of years.

# Define the rate of interest
rate_of_interest=2.5

# Prompt the user to enter the principal amount
principal_amount=int(input("Enter Principal Amount : "))

# Prompt the user to enter the number of years
number_of_years=int(input("Enter number of years : "))

# Calculate simple interest
simple_interest=(principal_amount*rate_of_interest*number_of_years)/100

# Print the calculated simple interest, formatted to two decimal places
print("Simple Interest : %.2f"%simple_interest)
