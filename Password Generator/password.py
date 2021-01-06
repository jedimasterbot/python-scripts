import argparse
import random
import string


def PasswordGenerator(combine, length):
    """ Generates a random password having the specified length. Default length 8 is passed """

    # Sends the combined string to choice method
    password = ''.join(random.choice(combine) for x in range(length))

    print(f"String Of Length {length} is: {password}")


def main():
    parser = argparse.ArgumentParser(
        description='GENERATE RANDOM PASSWORD OF LENGTH SPECIFIED WITH MIX AND MATCH. DEFAULT HAS ASCII,DIGITS AND '
                    'PUNCTUATIONS INCLUDED WITH LENGTH OF EIGHT')

    # Argument is for a length of the password
    parser.add_argument('-l', dest='length', type=int, nargs='?', const=8, help='Length For Password', required=True)

    # Argument is for ascii characters
    parser.add_argument('-a', dest='ascii', action='store_true', help='Use ASCII Characters')

    # Argument is for digits
    parser.add_argument('-d', dest='digit', action='store_true', help='Use Digits')

    # Argument is for punctuations
    parser.add_argument('-p', dest='punctuation', action='store_true', help='Use Special Characters')

    args = parser.parse_args()

    # Checks if the number is a positive integer
    if args.length > 0:
        lenPass = args.length

        # create alphanumerical from string constants
        combine = [string.ascii_letters, string.digits, string.punctuation]

        # Generate string using ascii,digit and punctuation
        if args.ascii and args.digit and args.punctuation:
            # Call the function
            PasswordGenerator(str(combine[0] + combine[1] + combine[2]), lenPass)

        # Generate string using ascii and digits
        elif args.ascii and args.digit:
            # Call the function
            PasswordGenerator(str(combine[0] + combine[1]), lenPass)

        # Generate string using ascii and punctuation
        elif args.ascii and args.punctuation:
            # Call the function
            PasswordGenerator(str(combine[0] + combine[2]), lenPass)

        # Generate string using digit and punctuation
        elif args.digit and args.punctuation:
            # Call the function
            PasswordGenerator(str(combine[1] + combine[2]), lenPass)

        # Generate string using ascii
        elif args.ascii:
            # Call the function
            PasswordGenerator(str(combine[0]), lenPass)

        # Generate string using digit
        elif args.digit:
            # Call the function
            PasswordGenerator(str(combine[1]), lenPass)

        # Generate string using punctuation
        elif args.punctuation:
            # Call the function
            PasswordGenerator(str(combine[2]), lenPass)

        else:
            # Call the function
            PasswordGenerator(str(combine[0] + combine[1] + combine[2]), lenPass)

    else:
        print("Enter A Positive Integer")


if __name__ == '__main__':
    main()
