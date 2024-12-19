#Q.1)WAP to get factorial of a number using function

def factorial_recursive(number):
    if (number==1) or (number==0): # Handle 0! case
        return 1
    else:
        return number*factorial_recursive(number-1)

# Another approach using iteration

def factorial_iterative(number):
    #Calculate factorial using iteration.
    result=1
    for i in range(1,number+1):
        result=result*i
    return result

# Get user input
number=int(input("Enter a non-negative integer:")) # Clarified input requirement
# Print the results of both approaches
print(f"Factorial of {number} is : {factorial_recursive(number)} and Another Approach : {factorial_iterative(number)}")
