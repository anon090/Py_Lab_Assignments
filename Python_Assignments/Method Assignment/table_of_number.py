#Q.4)WAP to get table of a number using function

def print_multiplication_table(number):
    #Print the multiplication table for the given number.
    print(f"---- Multiplication Table for {number} ----- ")
    for i in range(1,11):
        print(f"\t{number} x {i} = {number*i}")
        print("------------------------------------- ")

# Get user input
number=int(input("Enter a number :"))

# Print the multiplication table
print_multiplication_table(number)
