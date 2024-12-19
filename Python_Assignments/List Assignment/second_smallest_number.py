#Q.3)WAP to find second smallest element in the list

# Define the list
my_list=[15,16,13,14,15,12]
print("Your list :",my_list)

# Without using sorting() method to find the second smallest number
# Bubble sort implementation
for i in range(len(my_list)):
    for j in range(len(my_list)-1-i):
        if my_list[j] > my_list[j+1]:
            my_list[j] , my_list[j+1]= my_list[j+1] , my_list[j]

# Print the sorted list after bubble sort
print("Your list sorted without using built-in method:",my_list)

# The second smallest number is at index 1 after sorting
print("Second smallest number :",my_list[1])

# With using sorting() method to find the second smallest number
my_list.sort(reverse=True) # Sort in descending order
print("Your list sorted with using built-in method in decending order:",my_list)

# The second smallest number is the second last element in a descending sorted list
print("Second smallest number :",my_list[-2])
