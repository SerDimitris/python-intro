# Populate
fruits = ["apple", "banana", "cherry", "apple"]
print("Initial list of fruits:", fruits)

# Add
fruits.append("orange")
print("After adding orange", fruits)

# Add two or more items
fruits.extend(["Grapes", "Fig"])
print("After multiple appends", fruits)

# Add item at specific position
fruits.insert(1, "Coconut")
print("After adding Coconut at pos 1 (2nd element)", fruits)

# Update
fruits[0] = "Melon"
print("After update Melon at pos 0", fruits)

# Update two elements
fruits[1:3] = ["A", "B"]
print(f"List after updating two elements: {fruits}")

# Delete
remove_item = fruits.pop(1)
print(f"Removed item: {remove_item}")
print(fruits)

new_removed_item = fruits.remove("B")
print(f"2nd removed item is: {fruits}")
print(fruits)

# # Remove a fantastc item
# fruits.remove("exotic_fruit")
# print(fruits)

# Search
pos = fruits.index("Fig")
print(f"in pos: {pos} exists {fruits[pos]}")