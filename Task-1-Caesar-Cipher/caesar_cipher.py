def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char

    return result
def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")

    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        print("Encrypted:", encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted:", decrypt(text, shift))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
    
    