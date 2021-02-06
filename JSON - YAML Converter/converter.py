import argparse
import json
import os
import yaml


def json2yaml(files):
    for file in files:
        # Iterate through the files
        if os.path.isfile(f"{os.getcwd()}\{file}"):
            # Get the base filename
            filename_full = os.path.basename(file)
            # Get the filename and extension
            filename, extension = os.path.splitext(filename_full)

            if extension == '.json':
                # Opening the file
                source_file = open(filename_full, "r")
                source_content = json.load(source_file)
                source_file.close()

                # Processing the conversion
                output = yaml.dump(source_content)

                # If the target file already exists exit
                new_filename = f'{filename}.yaml'
                if os.path.exists(new_filename):
                    print("ERROR: " + new_filename + " already exists")

                # Otherwise write to the specified file
                else:
                    target_file = open(new_filename, "w")
                    target_file.write(output)
                    target_file.close()
                    print(f"YAML File Converted: {new_filename}")

            else:
                print(f"Extension NOT Valid for file: {file}")


def yaml2json(files):
    for file in files:
        # Iterate through the files
        if os.path.isfile(f"{os.getcwd()}\{file}"):
            # Get the base filename
            filename_full = os.path.basename(file)
            # Get the filename and extension
            filename, extension = os.path.splitext(filename_full)

            if extension == ".yaml":
                # Opening the file
                source_file = open(filename_full, "r")
                source_content = yaml.safe_load(source_file)
                source_file.close()

                # Processing the conversion
                output = json.dumps(source_content)

                # If the target file already exists exit
                new_filename = f'{filename}.json'
                if os.path.exists(new_filename):
                    print(f"ERROR: {new_filename} already exists")

                # Otherwise write to the specified file
                else:
                    target_file = open(new_filename, "w")
                    target_file.write(output)
                    target_file.close()
                    print(f"JSON File Converted: {new_filename}")
            else:
                print(f"Extension NOT Valid for file: {file}")


def main():
    parser = argparse.ArgumentParser(description='Convert JSON to YAML and YAML to JSON')

    # Argument is to accept a file(s)
    parser.add_argument('-f', dest='file', nargs='+', type=str, help='Submit a file(s)', required=True)

    # Argument is to convert file to json
    parser.add_argument('-j', dest='json', action='store_true', help='Convert YAML to JSON')

    # Argument is to convert file to yaml
    parser.add_argument('-y', dest='yaml', action='store_true', help='Convert JSON to YAML')

    args = parser.parse_args()

    if args.file:
        # Accepts files
        files = args.file

        if args.json:
            # Call to function
            yaml2json(files)

        if args.yaml:
            # Call to function
            json2yaml(files)


if __name__ == '__main__':
    main()
