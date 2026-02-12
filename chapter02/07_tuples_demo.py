students = ("Alice", "Bob", "Charlie")

print(type(students))

# Iterate
for index, student in enumerate(students):
    print(f"{index} : {student}")

# Enchanced for
for student in students:
    print(student)

# first_st = students[0]
# second_st = students[1]
# third_st = students[2]

first_st, second_st, third_st = students

print(f"1st student is: {first_st}")
print(f"2nd student is: {second_st}")
print(f"3rd student is: {third_st}")