import argparse
import PIL
from PIL import Image


def img_data_delete(files):
    for file in files:

        # try, except block
        try:

            # Open image file
            image = Image.open(file)

            # Getting the original image mode and size
            stripped = Image.new(image.mode, image.size)

            # Cleaning and saving the file
            stripped.putdata(list(image.getdata()))
            stripped.save(f"clean_{file}")

            print(f"Clean Image File: clean_{file}")

        except PIL.UnidentifiedImageError:
            print(f"Cannot Identify Image: {file}")

        except IOError:
            print(f'Problem Reading Image: {file}')


def main():
    parser = argparse.ArgumentParser(description='DELETE METADATA IN IMAGES')

    # Argument is for images files
    parser.add_argument('-f', dest='files', nargs='+', type=str, help='Image File(s)', required=True)

    args = parser.parse_args()

    # Get the files
    files = args.files

    if files:
        img_data_delete(files)


if __name__ == '__main__':
    main()
