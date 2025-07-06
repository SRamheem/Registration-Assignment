name = input("Enter your name: ")

while True:
    email = input("Enter your email (must end with @gmail.com): ")
    if email.endswith("@gmail.com"):
        break
    else:
        print("Invalid email. Only '@gmail.com' addresses are allowed. Please try again.")

print("Received data:")
print(f"Name - {name}")
print(f"Email - {email}")
