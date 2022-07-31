password = input("password? ")

if len(password) < 4 or len(password) > 20:
    print("A password must have 8 to 20 characters only")
else:
    print("Good to go")
    print("*" * len(password))
