MIN_LENGTH = 6
MAX_LENGTH = 20


def main():
    password = get_password()
    while len(password) < MIN_LENGTH and MAX_LENGTH > len(password):
        print("A password must have 6 to 20 characters only")
        password = get_password()
    get_asterisks(password)


def get_password():
    return input("password: ")


def get_asterisks(password):
    print("*" * len(password))


main()
