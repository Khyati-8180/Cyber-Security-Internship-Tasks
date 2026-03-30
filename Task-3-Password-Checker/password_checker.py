def check_password(password):
    length = len(password) >= 8
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium 😐"
    else:
        return "Weak 😢"


def main():
    password = input("Enter your password: ")
    strength = check_password(password)
    print("Password Strength:", strength)


if __name__ == "__main__":
    main()