import cv2
import hashlib

def encode_message(image_path, secret_message, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found. Check the file path and make sure the image exists.")
        return
    height, width, channels = img.shape
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.digest()
    d = {chr(i): i for i in range(256)}
    n = m = z = 0
    for i in range(len(secret_message)):
        new_value = (int(img[n, m, z]) + d[secret_message[i]] + hashed_password[i % len(hashed_password)]) % 256
        img[n, m, z] = new_value
        m += 1
        if m >= width:
            m = 0
            n += 1
        if n >= height:
            print("Image too small to hold the entire message.")
            break
        z = (z + 1) % 3
    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    print(f"Message has been encoded into '{encrypted_image_path}'.")

def decode_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found. Check the file path and make sure the image exists.")
        return
    height, width, channels = img.shape
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.digest()
    c = {i: chr(i) for i in range(256)}
    n = m = z = 0
    decoded_message = ""
    while True:
        original_value = (int(img[n, m, z]) - hashed_password[len(decoded_message) % len(hashed_password)]) % 256
        decoded_character = c[original_value]
        if decoded_character == '\x00':
            break
        decoded_message += decoded_character
        m += 1
        if m >= width:
            m = 0
            n += 1
        if n >= height:
            break
        z = (z + 1) % 3
    print(f"Decoded message: {decoded_message}")

def main():
    choice = input("Do you want to (E)ncode or (D)ecode a message? ").lower()
    if choice == 'e':
        image_path = input("Enter the path to the image: ")
        secret_message = input("Enter secret message: ")
        password = input("Enter a passcode: ")
        encode_message(image_path, secret_message, password)
    elif choice == 'd':
        image_path = input("Enter the path to the encoded image: ")
        password = input("Enter the passcode: ")
        decode_message(image_path, password)
    else:
        print("Invalid choice. Please enter 'E' to encode or 'D' to decode.")

if __name__ == "__main__":
    main()
