#Q.1)Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.

# Initialize an empty list
no_list=[]
print("Enter 5 elements for peforming some operations ...")

# Loop to collect 5 elements from the user
for i in range(5):
    no=int(input("Enter number to adding in a list :"))
    no_list.append(no)  # Add the entered number to the list

# Variable to control the operation loop
ch="y"
print("now you perform operations :")
while(ch=="y"):
    print("1.. Adding \n2.. Removing\n3.. Exit")
    chk=input("Enter your choice :")
    
    if(chk=="1"):
        # Adding an element to the list
        no=int(input("Enter number you want to add :"))
        no_list.append(no)  # Append the new number to the list
        print(f"Result after adding element :{no_list}")
    elif(chk=="2"):
        # Removing an element from the list
        print(f"list data : {no_list}")
        no=int(input("Enter number you want to remove :"))
        while no in no_list:
            no_list.remove(no) # Remove all occurrences of the number
        print(f"Result after removing element :{no_list}")
    elif(chk=="3"):
        ch="n"  # Exit the loop
        print("Execution is completed")
    else:
        print("please enter valid input")
        ch="y"  # continuing the loop
    
