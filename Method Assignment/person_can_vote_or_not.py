#Q.3)WAP to check whether person can vote or not using function

def check_voting_eligibility(person_age):
    #Check if a person is eligible to vote based on their age.
    if(person_age>=18):
        print("You are eligible for vote")
    else:
        print("you are minor ! That's why you are not eligible for vote")

# Get user input
age=int(input(" Enter your age: "))
# Check voting eligibility
check_voting_eligibility(age)
