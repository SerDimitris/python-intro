username = input("Enter your usename: ")

email = input("Enter your email: ")

valid_user = username or "User"

print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or "please provide your email."))