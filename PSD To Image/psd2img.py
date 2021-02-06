import argparse
import os

from psd_tools import PSDImage


def pngCreator(files, img_extension):
    for file in files:

        # Iterate through the files
        if os.path.isfile(f'{os.getcwd()}\{file}'):

            # Get the base filename
            filename_full = os.path.basename(file)

            # Get the filename and extension
            filename, extension = os.path.splitext(filename_full)

            # Check the extension of file is psd
            if extension == '.psd':

                # Open the file
                psd = PSDImage.open(file)

                # Save the file according to extension provided
                psd.composite().save(f'{filename}.{img_extension}')

                print(f'File created: {filename}.{img_extension}')

            else:
                print(f'Extension NOT Valid for file: {file}')


def main():
    parser = argparse.ArgumentParser(description='Convert PSD to JPEG, PNG')

    # Argument is to accept a file(s)
    parser.add_argument('-f', dest='file', nargs='+', type=str, help='Submit a PSD file(s)', required=True)

    # Argument is to convert psd file to jpeg
    parser.add_argument('-j', dest='jpeg', action='store_true', help='Convert PSD to JPEG')

    # Argument is to convert psd file to png
    parser.add_argument('-p', dest='png', action='store_true', help='Convert PSD to PNG')

    args = parser.parse_args()

    if args.file:
        # Accepts files
        files = args.file

        # JPEG parameter is selected
        if args.jpeg:
            pngCreator(files, 'jpeg')

        # PNG parameter is selected
        elif args.png:
            pngCreator(files, 'png')

        else:
            print('See Help: psd2img.py -h')

    else:
        print('No Files Given')


if __name__ == '__main__':
    main()
