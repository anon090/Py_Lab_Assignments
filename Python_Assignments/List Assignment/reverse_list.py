#Q.2)WAP to reverse the element in List

# Initialize the original list
list=[12,13,14,17,15,16,17]
rev_list=[]  # Initialize an empty list to hold the reversed elements

#print the original list
print(f"original list : {list}")

# Reverse the list without using the reverse() method
for i in list[::-1]:   # Slicing the list to get elements in reverse order
    rev_list.append(i) # Append each element to the rev_list

# Print the reversed list without using the method
print(f"Reversed list without method : {rev_list}")

# Reverse the list using the reverse() method
list.reverse()  # In-place reversal of the original list

print(f"Reversed list with method : {list}")
