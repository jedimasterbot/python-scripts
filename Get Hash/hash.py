import argparse
from filehash import FileHash
import magic
import os


def file_type_hashes(files):
    # Declare the type of hash you want
    md5Hash = FileHash('md5')
    sha1Hash = FileHash('sha1')
    sha256Hash = FileHash('sha256')
    sha512Hash = FileHash('sha512')
    crcHash = FileHash('crc32')
    adler32Hash = FileHash('adler32')

    # Iterate through the files
    for file in files:

        # Check if file exists
        if os.path.isfile(file):

            # Generate the file hash and the file type as well
            file_info = {
                "filename": file,
                "filetype": magic.from_file(file),
                "md5": md5Hash.hash_file(file),
                "sha1": sha1Hash.hash_file(file),
                "sha256": sha256Hash.hash_file(file),
                "sha512": sha512Hash.hash_file(file),
                "crc32": crcHash.hash_file(file),
                "adler32": adler32Hash.hash_file(file)
            }

            print(file_info)

        else:
            print(f"No File Found: {file}")


def file_type(files):

    # Iterate through the files
    for file in files:

        # Check if file exists
        if os.path.isfile(file):

            # Generate the file type
            print(f"Filename: {file} , File Type: {magic.from_file(file)}")

        else:
            print(f"No File Found: {file}")


def main():
    parser = argparse.ArgumentParser(description='Get The Hashes And File Type Of File(s)')

    # Argument is to accept a file(s)
    parser.add_argument('-f', dest='file', nargs='+', type=str, help='Submit file(s)', required=True)

    # Argument is to display only the file type of file(s)
    parser.add_argument('-t', dest='type', action='store_true', help='Get only the file type of file(s)')

    args = parser.parse_args()

    if args.file:
        # Accepts files
        files = args.file

        if files:
            # Display the file type only
            if args.type:
                file_type(files)

            # Show the hashes and the file type as well
            else:
                file_type_hashes(files)


if __name__ == '__main__':
    main()
