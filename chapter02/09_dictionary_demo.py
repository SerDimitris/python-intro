# Pupolate dict
products = {
    1:"apples",
    2:"bananas",
    3:"honey",
    4:"lemons"
}

print(f"Initial products: {products}")

# Insert a new product
products[15] = "oranges"
print(f"Products after insertion: {products}")

# Get the product with id: 3
print(products[3])

# Update
products[2] = "milk"
print(f"Updated products: {products}")

# Delete
# del products[4]
# print("Products after deletion:", products)

remove_product = products.pop(100, "Not found")
print(f"Removed product by using pop: {remove_product}")

# popitem() remove 'last' item
# product = products.popitem()
#print(type(product))

key, value = products.popitem()
print(f"{key} : {value}")
print(products)

key_to_check = 2

if key_to_check in products:
    print(f"{key_to_check} exists")
else:
    print(f"{key_to_check} doesn't exist")

# Gets keys from dictionary
for key in products.keys():
    print(key)

# Get values from a dictionary
for value in products.values():
    print(value)

# Get keys and values from a dictionary
for key in products.keys():
    print(f"{key} : {products[key]}")

for key, value in products.items():
    print(f"{key} : {value}")