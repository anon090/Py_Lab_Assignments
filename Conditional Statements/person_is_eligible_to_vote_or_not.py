# Program to check if a person is eligible to vote or not based on age

# Input: Prompt the user to enter their age
age=int(input("Enter your age : "))

# Eligibility check: Determine if the user is eligible to vote or not.
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are a minor! That's why you are not eligible to vote.")
