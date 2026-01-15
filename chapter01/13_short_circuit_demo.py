name = "Jim"

valid_user = None or "User"
print(f"Hello {valid_user}")

valid_user = name or "User"
print(f"Hello {valid_user}")

email = "bob@example.com"
valid_email = email and email != ""

print(valid_email)

if valid_email:
    print(f"Hello {valid_user}, your email is {email}")
else:
    print(f"Hello {valid_email}, please give your email.")