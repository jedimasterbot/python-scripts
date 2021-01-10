import argparse
import os

from PIL import Image
import stepic


def encode(file, text):
    # Open Image or file in which you want to hide your data
    image = Image.open(file)

    # Convert the string to bytes
    text = bytes(text, 'utf-8')

    # Encode some text into your image file and save it in another file
    encodeImage = stepic.encode(image, text)

    # Get the filename from the path
    filename = os.path.splitext(os.path.basename(file))[0]

    # Save the image in PNG file
    encodeImage.save(f'{filename}_enc.png', 'PNG')

    print(f'File Encoded: {filename}_enc.png')
    print(f'String Used To Encode: {text}')


def decode(path):
    # Open Image or file in which data exists
    image = Image.open(path)

    # Decode the image to extract the text
    decodeImage = stepic.decode(image)

    # Print the text
    print(f'Decoded String From Image: {decodeImage}')


def main():
    parser = argparse.ArgumentParser(description='STEGANOGRAPHY IN IMAGES')

    # Argument is for images to encode/decode
    parser.add_argument('-f', dest='files', nargs='+', type=str, help='Image File', required=True)

    # Argument is to encode in the image
    parser.add_argument('-e', dest='encode', type=str, help='Encode The Text In Image')

    # Argument is to decode from image
    parser.add_argument('-d', dest='decode', action='store_true', help='Decode The Text In Image')

    args = parser.parse_args()

    # Get the files
    files = args.files

    if files:
        # If user wants to encode
        if args.encode:
            # Iterate through the files
            for file in files:
                # Check if the file exists
                if os.path.isfile(file):
                    # Call the function
                    encode(file, args.encode)

                else:

                    print(f'File Not Found: {file}')

        # If user wants to decode
        elif args.decode:
            # Iterate through the files
            for file in files:
                # Check if the file exists
                if os.path.isfile(file):
                    # Call the function
                    decode(file)

                else:
                    print(f'File Not Found: {file}')

        else:
            print('Use -h For Help')

    else:
        print('File Not Found')


if __name__ == '__main__':
    main()
