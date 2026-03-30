from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print("Image Encrypted!")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print("Image Decrypted!")


def main():
    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
    key = int(input("Enter key (number): "))

    if choice == 'e':
        encrypt_image("input.png", "encrypted.png", key)
    elif choice == 'd':
        decrypt_image("encrypted.png", "decrypted.png", key)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()