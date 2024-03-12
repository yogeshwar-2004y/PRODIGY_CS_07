def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine the shift direction based on encryption or decryption
            direction = 1 if encrypt else -1
            # Determine the base ASCII value for lowercase or uppercase letters
            base = ord('a') if char.islower() else ord('A')
            # Calculate the new character position after shifting
            shifted_char = chr(((ord(char) - base + direction * shift) % 26) + base)
            result += shifted_char
        else:
            result += char
    return result

def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice!")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (a positive integer): "))
   
    if choice == 'encrypt':
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
