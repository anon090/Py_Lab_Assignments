customers = {
        101: "John Doe",
        102: "Jane Smith",
        103: "Emily Johnson"
    }

# Print all customers
print("Customers:",customers)

# Print specific customer by ID
print("Customer 101:",customers[101])
print("Customer 103:",customers.get(103))

#find all the keys frorm dictionary
print("Customer IDs:",customers.keys())

#to update dictionary element
customers.update({101:"JOhn"})
print("Updated Customers:",customers)

# To add a new customer
customers.update({104:"Elbert"})
print("Added Elbert:", customers)

#To add another new customer in dictionary
customers[105]="Robin"
print("Added Robin:", customers)

# To remove the last added element from the dictionary
print("Removed last customer:", customers.popitem())
print("After removing last customer:", customers)

#looping over the dictionary keys
for customer_id in customers:
    print("Customer ID:", customer_id)
for customer_id in customers.keys():
    print("Customer ID:", customer_id)

# Looping over the dictionary values
for customer_name in customers.values():
    print("Customer Name:", customer_name)

# Traversing the dictionary
for customer_id, customer_name in customers.items():
    print("Customer ID:", customer_id, "Customer Name:", customer_name)

# Remove a specific customer and handle potential errors
removed_customer = customers.pop(104,None)
if removed_customer is not None:
    print("Removed Customer ID 104:", removed_customer)
else:
    print("Customer ID 104 not found.")

#print final data of customer dictionary
print("Final Customers:", customers)
