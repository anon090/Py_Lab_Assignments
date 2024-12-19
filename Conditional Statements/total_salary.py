# Program to calculate total salary based on basic salary, DA, and HRA

# Input: Prompt the user to enter their basic salary
basic_salary=float(input("Enter Your Basic Salary : "))

# Initialize allowances
da=basic_salary*0.10   # 10% DA
hra=basic_salary*0.12  # 12% HRA

# Calculate total salary
if(basic_salary > 50000):
    total_salary=hra+da+basic_salary    # Total salary includes DA and HRA
else:
    total_salary=basic_salary           # No DA and HRA if salary is less than or equal to 50000

# Output: Display the total salary formatted to two decimal places
print("Your total salary : %.2f"%total_salary)
    
