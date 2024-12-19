# Q.4) Perform Intersection operation on two lists

# Define two lists
list1=[12,13,14,15,16,17]
list2=[12,13,14,15,16,17,18]

# Print the original lists
print(f"first list : {list1} \nsecond list : {list2}")

# Perform intersection using built-in functions
# Convert lists to sets and find the intersection
print(f"intersection operation on list with using built-in fuctions : {list(set(list1)&set(list2))}")

# Perform intersection without using the intersection() method
# Initialize an empty list to store the intersection results
new_list=[]

# Iterate through the first list
for item in list1:
    # Check if the current item from list1 is in list2
    if item in list2:
        # Check if the item is not already in the intersection list
        if item not in new_list:
            new_list.append(item)

# Print the intersection result without using built-in functions
print(f"intersection operation on list wihtout using built-in fuctions : {new_list}")
