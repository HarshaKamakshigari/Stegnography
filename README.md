

# Image Steganography

This project implements a simple image steganography tool using Python. It allows you to encode a secret message into an image and decode the hidden message from an image.

## Features

- **Encode Message**: Hide a secret message within an image using a passcode.
- **Decode Message**: Extract the hidden message from an encoded image using the same passcode.

## Requirements

- Python 3.x
- OpenCV
- hashlib

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/image-steganography.git
    cd image-steganography
    ```

2. Install the required dependencies:
    ```sh
    pip install opencv-python
    ```

## Usage

Run the script:
```sh
python steganography.py
```

### Encoding a Message

1. Choose the encoding option.
2. Enter the path to the image file.
3. Enter the secret message you want to hide.
4. Enter a passcode.

The encoded image will be saved as `encryptedImage.jpg`.

### Decoding a Message

1. Choose the decoding option.
2. Enter the path to the encoded image file.
3. Enter the passcode used during encoding.

The decoded message will be printed.

## Example

1. **Encoding**:
    ```sh
    Do you want to (E)ncode or (D)ecode a message? e
    Enter the path to the image: path/to/image.jpg
    Enter secret message: Hello, World!
    Enter a passcode: mysecret
    Message has been encoded into 'encryptedImage.jpg'.
    ```

2. **Decoding**:
    ```sh
    Do you want to (E)ncode or (D)ecode a message? d
    Enter the path to the encoded image: encryptedImage.jpg
    Enter the passcode: mysecret
    Decoded message: Hello, World!
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify the above template to suit your specific needs. Replace `your-username` with your GitHub username and `path/to/image.jpg` with the actual path to your image.
