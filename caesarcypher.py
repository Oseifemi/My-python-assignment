
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift within alphabet range
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Leave spaces and punctuation unchanged
    return result

# Main program
print("=== Caesar Cipher ===")
text = input("Enter your message: ")
while True:
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
        break
    except ValueError:
        print("Please enter a valid number.")

mode = input("Type 'encrypt' to encode or 'decrypt' to decode: ").strip().lower()
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode selected. Defaulting to 'encrypt'.")
    mode = 'encrypt'

output = caesar_cipher(text, shift, mode)
print(f"\n{mode.capitalize()}ed message: {output}")
