# Populate a set
bag = {"eggs", "apples", "bananas", "eggs"}

print("Inital set:", bag)

# Add a new item to the set
bag.add("oranges")
print("After adding oranges:", bag)

# Remove
item_to_remove = "eggs"
bag.remove(item_to_remove)
print(f"After removing {item_to_remove}: {bag}")

# Iterate thought the set
for item in bag:
    print(item)