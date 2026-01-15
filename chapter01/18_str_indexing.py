message = "Hello World!"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])
print(message[6])
print(message[7])
print(message[8])
print(message[9])
print(message[10])
print(message[11])

print(f"Number of letters in '{message}': {len(message)}")

for char in message:
    print(char, end=" ")
print()

for i in range(10):
    print(i, end=" ")
print()

for i in range(0, len(message), 2):
    print(message[i], end=" ")
print()