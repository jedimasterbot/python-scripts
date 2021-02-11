import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS
import PIL


def img_data(files):
    for file in files:

        print(f"------------------{file} META DATA------------------")

        if os.path.isfile(file):

            try:
                # Read the image
                image = Image.open(file)

                # Extract EXIF data
                exif_data = image.getexif()

                # Iterating over EXIF data values
                for tag_id in exif_data:

                    # get the tag name
                    tag = TAGS.get(tag_id, tag_id)

                    data = exif_data.get(tag_id)

                    # Try, except block
                    try:
                        # Check if instance is bytes
                        if isinstance(data, bytes):
                            # Decode bytes
                            data = data.decode()

                        print(f"{tag:25}: {data}")

                    except UnicodeDecodeError:
                        pass

                print(f"----------------------------------------------------------")

            except PIL.UnidentifiedImageError:
                print(f"Cannot Identify Image: {file}")
                print(f"----------------------------------------------------------")

        else:
            print(f"No File Found: {file}")
            print(f"----------------------------------------------------------")


def main():
    parser = argparse.ArgumentParser(description='EXTRACT METADATA IN IMAGES')

    # Argument is for images files
    parser.add_argument('-f', dest='files', nargs='+', type=str, help='Image File(s)', required=True)

    args = parser.parse_args()

    # Get the files
    files = args.files

    if files:
        img_data(files)


if __name__ == '__main__':
    main()
