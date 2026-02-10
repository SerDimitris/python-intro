# Populate a list
ages = [23, 45, 12, 67]

print("Initial ages:", ages)

for index, value in enumerate(ages):
    print(f"Index: {index}, Value: {value}")

print("\nIterate with enchanced for loop")
for age in ages:
    print(age, end=" ")
print()