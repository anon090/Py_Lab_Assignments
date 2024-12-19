products = {
    "Apple": 0.50,
    "Banana": 0.60,
    "Orange": 0.75
}

# Print all products
print("Products:", products)

# Print specific product price
print("Price of Apple:", products["Apple"])
print("Price of Orange:", products.get("Orange"))

# Find all the keys from the dictionary
print("Product Names:", products.keys())

# To update a product's price
products.update({"Banana": 0.55})
print("Updated Products:", products)

# To add a new product
products.update({"Kiwi": 0.60}) 
print("Added Kiwi:", products)

# To add another new product
products["Mango"] = 0.70  
print("Added Mango:", products)

# To remove the last added element from the dictionary
print("Removing item:", products.popitem())
print("After removal:", products)

# Looping over the dictionary keys
for product_name in products:
    print("Product Name:", product_name)
for product_name in products.keys():
    print("Product Name:", product_name)

# Looping over the dictionary values
for product_price in products.values():
    print("Product Price:", product_price)

# Traversing the dictionary
for product_name, product_price in products.items():
    print("Product Name:", product_name, "Product Price:", product_price)

# Remove a specific product and handle potential errors
removed_product = products.pop("Kiwi", None)  
if removed_product is not None:
    print("Removed Product Kiwi:", removed_product)
else:
    print("Product Kiwi not found.")

#Print final data of products dictionary
print("Final Products:", products)
