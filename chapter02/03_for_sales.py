# List of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Fruit we want to find
fruit_to_find = "orange"

for fruit in fruits:
    if fruit == fruit_to_find:
        print(f"{fruit_to_find} found in the list!")
        break
else:
    print(f"{fruit_to_find} not found in the list.")