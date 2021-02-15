import argparse
import pdfkit


def converter(url, filename):
    path_wkthmltopdf = "wkhtmltopdf/bin/wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    pdfkit.from_url(url, filename, configuration=config)


def main():
    parser = argparse.ArgumentParser(description='Convert Webpage To PDF')

    # Argument is to input the url to download images from
    parser.add_argument('-u', dest='url', type=str, help='URL to convert to PDF', required=True)

    # Argument is to input the url to download images from
    parser.add_argument('-f', dest='file', type=str, help='Filename of the PDF', required=True)

    args = parser.parse_args()

    if args.url:

        url = args.url

        # Check if the url starts with wither http or https
        if not url.startswith("http") and not url.startswith("https"):
            # Add the https in front of the url
            url = "https://" + url

        # Call to the function
        filename = str(args.file)

        if filename.endswith('.pdf'):
            converter(url, filename)

        else:
            print(f"The Extension Of Fil Should be .pdf, you entered: {filename}")


if __name__ == '__main__':
    main()
