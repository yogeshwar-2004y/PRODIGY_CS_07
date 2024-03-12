from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    # Get the dimensions of the image
    width, height = img.size
    # Convert the image to RGB mode
    img = img.convert("RGB")

    # Encrypt the image by applying a basic mathematical operation to each pixel
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # Apply encryption operation (e.g., XOR operation with the key)
            r ^= key
            g ^= key
            b ^= key
            encrypted_pixels.append((r, g, b))

    # Create a new image with the encrypted pixel values
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    return encrypted_img

def decrypt_image(encrypted_img, key):
    # Get the dimensions of the encrypted image
    width, height = encrypted_img.size

    # Decrypt the image by applying the reverse operation to each pixel
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = encrypted_img.getpixel((x, y))
            # Apply decryption operation (e.g., XOR operation with the key)
            r ^= key
            g ^= key
            b ^= key
            decrypted_pixels.append((r, g, b))

    # Create a new image with the decrypted pixel values
    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
    decrypted_img.putdata(decrypted_pixels)
    return decrypted_img

def main():
    # Path to the image file
    image_path = input("Enter the path to the image file: ")
    # Encryption key (an integer)
    key = int(input("Enter the encryption key (an integer): "))

    # Encrypt the image
    encrypted_img = encrypt_image(image_path, key)
    encrypted_img.show()
    encrypted_img.save("encrypted_image.png")

    # Decrypt the image
    decrypted_img = decrypt_image(encrypted_img, key)
    decrypted_img.show()

if __name__ == "__main__":
    main()
