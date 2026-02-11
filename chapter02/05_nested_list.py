items = [1, 2, 3.14, True, "Hello World!"]

for item in items:
    print(item, end=" ")
print()

nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"Nested list: {nested_list}")
print(f"1st item of the nested list: {nested_list[0]}")
print(f"1st item of the 2nd nested list: {nested_list[1][0]}")

print(nested_list[1::-1])

for outer_item in nested_list:
    for inner_item in outer_item:
        if inner_item % 2 == 0:
            result = inner_item

print("Final even num:", result)