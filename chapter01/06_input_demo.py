name = input("Please insert your name: ")

is_student = input("Are you a student? (yes/no)").lower() == "yes"

print(f"{name}")
print(f"is_student: {is_student}")

if is_student:
    print("You are student")
else:
    print("You are not a student")