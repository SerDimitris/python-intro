import random

random_numbers = []

# Use for loop to populate the list with 10 random numbers

for _ in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

# Last even number found in the list
for num in random_numbers:
    if num % 2 == 0:
        even = num

print(f"The last item of the list: {num}")
print(f"The last even number found in the list: {even}")