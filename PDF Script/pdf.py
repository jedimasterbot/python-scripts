import argparse
import calendar
import os
import sys

import img2pdf
from PyPDF2.pdf import PdfFileWriter, PdfFileReader
import time

# Get the timestamp
ts = calendar.timegm(time.gmtime())


def PdfPassword(filepath, password):
    # Check if file exists
    checkFile = os.path.isfile(filepath)

    if checkFile:
        # Get the path of directory and filename
        path, filename = os.path.split(filepath)

        # Get the file extension to check for pdf files
        file_extension = os.path.splitext(filepath)[1]

        if file_extension == ".pdf":

            # The output filename
            output_file = os.path.join(path, f"temp_{ts}_{filename}")

            # Create a PdfFileWriter object
            pdf_writer = PdfFileWriter()

            # Open our PDF file with the PdfFileReader
            file = PdfFileReader(filepath)

            # Get number of pages in original file
            # Iterate through every page of the original file and add it to our new file
            for idx in range(file.numPages):
                # Get the page at index idx
                page = file.getPage(idx)

                # Add it to the output file
                pdf_writer.addPage(page)

            # Encrypt the new file with the entered password
            pdf_writer.encrypt(password, use_128bit=True)

            # Open a new file
            with open(output_file, "wb") as file:
                # Write our encrypted PDF to this file
                pdf_writer.write(file)

            print('File Written To Path:', output_file)

        else:
            # File extension is not PDF
            print(f"Not A PDF File Given, File Has Extension: {file_extension}")
            sys.exit()

    else:
        # No file exists on the current path
        print("Check The File Path")
        sys.exit()


def PdfMultiplePassword(filepaths, password):
    # Check if files exists
    check_path = [os.path.isfile(x) for x in filepaths]

    # Gets the files extension
    file_extensions = [os.path.splitext(x)[1] for x in filepaths]

    # Check if files extension are pdf
    file_extensions_check = [x for x in file_extensions if x != ".pdf"]

    if False in check_path:

        # Get the index of the file that doesn't exists
        index = check_path.index(False)
        print(f"File Doesn't Exists: {filepaths[index]}")
        sys.exit()

    else:
        # Not a PDF file is given
        if file_extensions_check:
            print("Submit Only PDF Files")
            sys.exit()

        else:
            count = 1
            # Iterate through every pdf of the filepaths
            for path in filepaths:

                # Create a PdfFileWriter object
                pdf_writer = PdfFileWriter()

                # Open our PDF file with the PdfFileReader
                pdf_reader = PdfFileReader(path)

                # Get the page at index idx
                for page in range(pdf_reader.getNumPages()):
                    # Add each page to the writer object
                    pdf_writer.addPage(pdf_reader.getPage(page))

                # The output filename
                output_file = f"merge_enc_{count}_{ts}.pdf"

                # Encrypt the new file with the entered password
                pdf_writer.encrypt(password, use_128bit=True)

                # Write out the merged PDF
                with open(output_file, 'wb') as file:
                    pdf_writer.write(file)

                count += 1
                print('File Written To Path:', output_file)


def PdfMerge(filepaths, password=None):
    # Check if files exists
    check_path = [os.path.isfile(x) for x in filepaths]

    # Gets the files extension
    file_extensions = [os.path.splitext(x)[1] for x in filepaths]

    # Check if files extension are pdf
    file_extensions_check = [x for x in file_extensions if x != ".pdf"]

    if False in check_path:

        # Get the index of the file that doesn't exists
        index = check_path.index(False)
        print(f"File Doesn't Exists: {filepaths[index]}")
        sys.exit()

    else:
        # Not a PDF file is given
        if file_extensions_check:
            print("Submit Only PDF Files")
            sys.exit()

        else:

            # Create a PdfFileWriter object
            pdf_writer = PdfFileWriter()

            # Iterate through every pdf of the filepaths
            for path in filepaths:

                # Open our PDF file with the PdfFileReader
                pdf_reader = PdfFileReader(path)

                # Get the page at index idx
                for page in range(pdf_reader.getNumPages()):
                    # Add each page to the writer object
                    pdf_writer.addPage(pdf_reader.getPage(page))

            if password:
                # The output filename
                output_file = f"merge_enc_{ts}.pdf"

                # Encrypt the new file with the entered password
                pdf_writer.encrypt(password, use_128bit=True)

                # Write out the merged PDF
                with open(output_file, 'wb') as file:
                    pdf_writer.write(file)

                print('File Written To Path:', output_file)

            else:
                # The output filename
                output_file = f"merge_{ts}.pdf"

                # Write out the merged PDF
                with open(output_file, 'wb') as file:
                    pdf_writer.write(file)

                print('File Written To Path:', output_file)


def PdfImage(filepaths, merger=False):
    # Check if files exists
    check_path = [os.path.isfile(x) for x in filepaths]

    if False in check_path:
        # Get the index of the file that doesn't exists
        index = check_path.index(False)
        print(f"File Doesn't Exists: {filepaths[index]}")
        sys.exit()

    else:
        # Check if the merger is True
        if merger:
            try:
                # Write the file with the name as name.pdf
                with open("name.pdf", "wb") as f:
                    f.write(img2pdf.convert(filepaths))
            # Exception if the the image can't be opened
            except img2pdf.ImageOpenError:
                print("Cannot Read Image")
                sys.exit()
        else:
            # Output filename
            output_file = f"img_{ts}.pdf"
            try:
                # Write the file
                with open(output_file, "wb") as f:
                    f.write(img2pdf.convert(filepaths))
            # Exception if the the image can't be opened
            except img2pdf.ImageOpenError:
                print("Cannot Read Image")
                sys.exit()


def PdfMultipleImage(filepaths, password=None):
    # Check if files exists
    files = []
    check_path = [os.path.isfile(x) for x in filepaths]

    if False in check_path:
        # Get the index of the file that doesn't exists
        index = check_path.index(False)
        print(f"File Doesn't Exists: {filepaths[index]}")
        sys.exit()

    else:
        count = 1
        # Iterate over the files
        for path in filepaths:
            # Name of the output file
            output_file = f"img_{count}_{ts}.pdf"
            try:
                # Convert the image to pdf and write the file
                with open(output_file, "wb") as f:
                    f.write(img2pdf.convert(path))
                    # Check if password is provided
                    if password:
                        # Sends the file to the function to be encrypted
                        PdfPassword(output_file, password)
                        # Checks if the file exist
                        if os.path.isfile(output_file):
                            files.append(output_file)
                    else:
                        print('File Written To Path:', output_file)
                    count += 1
            # Exception if the the image can't be opened
            except img2pdf.ImageOpenError:
                print(f"Cannot Read Image: {path}")

        try:
            # Remove the unwanted files
            for rm in files:
                os.remove(rm)
        except:
            pass


def main():
    parser = argparse.ArgumentParser(description='MERGE, ENCRYPT PDF FILES. CONVERT IMAGES TO PDF,ENCRYPT THEM')

    # Argument is for a single filepath
    parser.add_argument('-f', dest='filepath', type=str, help='Path For Single PDF')

    # Argument is for a multiple filepaths
    parser.add_argument('-a', dest='filepaths', nargs='+', type=str, help='Paths For Multiple PDF')

    # Argument is used for to encrypt the file
    parser.add_argument('-e', dest='password', type=str, help='Password To Encrypt The PDF')

    # Argument is used to merge files
    parser.add_argument('-m', dest='merge', nargs='+', type=str, help='Merge Multiple PDF File')

    # Argument is used to convert images into single PDF file
    parser.add_argument('-i', dest='image', nargs='+', type=str, help='Convert Multiple Images To One PDF File')

    parser.add_argument('-s', dest='seprateimage', nargs='+', type=str,
                        help='Convert Multiple Images To Separate PDF File')

    args = parser.parse_args()

    # Merge all the files and encrypt the file
    if args.filepath and args.merge and args.password:
        filename = args.filepath
        filepaths = args.merge
        filepaths.append(filename)
        PdfMerge(filepaths, args.password)

    # Convert the images into PDF, merge them with the PDF file(s) and encrypt the file
    elif args.image and args.password and (args.merge or args.filepath):
        if args.filepath:
            files = [args.filepath, "name.pdf"]
            PdfImage(args.image, True)
            PdfMerge(files, args.password)
            if os.path.isfile("name.pdf"):
                os.remove("name.pdf")
        else:
            PdfImage(args.image, True)
            filepaths = args.merge
            filepaths.append("name.pdf")
            PdfMerge(filepaths, args.password)
            if os.path.isfile("name.pdf"):
                os.remove("name.pdf")

    # Merge the single file and other files
    elif args.filepath and args.merge:
        filename = args.filepath
        filepaths = args.merge
        filepaths.append(filename)
        PdfMerge(filepaths)

    # Encrypt the PDF file
    elif args.filepath and args.password:
        PdfPassword(args.filepath, args.password)

    # Merge and encrypt the PDF files into one
    elif args.merge and args.password:
        PdfMerge(args.merge, args.password)

    # Encrypt Multiple files
    elif args.filepaths and args.password:
        PdfMultiplePassword(args.filepaths, args.password)

    # Merge Image and PDF files provided
    elif args.image and args.merge:
        PdfImage(args.image, True)
        filepaths = args.merge
        filepaths.append("name.pdf")
        PdfMerge(filepaths)
        if os.path.isfile("name.pdf"):
            os.remove("name.pdf")

    # Convert Images to individual PDF and encrypt them
    elif args.seprateimage and args.password:
        PdfMultipleImage(args.seprateimage, args.password)

    # Merge PDF files is provided
    elif args.merge:
        PdfMerge(args.merge)

    # Convert Images to single PDF
    elif args.image:
        PdfImage(args.image)

    # Convert Images to individual PDF
    elif args.seprateimage:
        PdfMultipleImage(args.seprateimage)


if __name__ == '__main__':
    main()
