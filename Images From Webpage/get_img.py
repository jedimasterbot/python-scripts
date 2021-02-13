import argparse
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from urllib.parse import urlparse


class ImageDownloader:
    """
    This class is used to download all the images on the webpage
    Takes only one param

    :param -- Valid URL for the website
    """

    def __init__(self, scrap_url):
        self.url = scrap_url
        self.image_urls = list()
        self.get_images()
        self.download()

    def download(self):

        if self.image_urls:

            for url in self.image_urls:

                # Download the body of response by chunk
                response = requests.get(url, stream=True)

                # Get the total file size
                file_size = int(response.headers.get("Content-Length", 0))

                # Get the file name
                filename = url.split("/")[-1]

                # Progress bar
                progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B",
                                unit_scale=True,
                                unit_divisor=1024)

                # Write to file
                with open(filename, "wb") as f:

                    for data in progress:
                        # Write data to the file
                        f.write(data)

                        # Update the progress bar
                        progress.update(len(data))

    def get_images(self):

        # try, except block
        try:

            # Get the page, with the timeout set to 5
            resp = requests.get(self.url, timeout=5)

            # Check the response code, 200 for valid
            if resp.status_code == 200:

                # Create the soup
                soup = BeautifulSoup(resp.content, "html.parser")

                # Find all the img tags from the page
                links = soup.find_all('img')

                # Extract the src of the images
                data = [y.attrs['src'] for y in links if y.name == 'img']

                # Get the original URL domain
                url_parsing = urlparse(self.url)
                domain = url_parsing.netloc

                for img_url in data:
                    # Parse the image url
                    img_url_parsing = urlparse(img_url)
                    img_path = img_url_parsing.path

                    # Check if the image url contains the domain and use it
                    if img_url_parsing.netloc != '':

                        # Create the complete URL
                        comp_url = f"https://{img_url_parsing.netloc}{img_path}"

                        # Append it into the list
                        self.image_urls.append(comp_url)

                    # Else use the default domain if the site
                    else:

                        # Create the complete URL
                        comp_url = f"https://{domain}{img_path}"

                        # Append it into the list
                        self.image_urls.append(comp_url)

            # Not a valid response code is given by the site
            else:
                print(f"Status Code: {resp.status_code}, For URL: {self.url}")

        # Tries to connect to the site
        except requests.exceptions.ConnectionError:
            print(f"No Response From URL: {self.url}")

        # Generic exception
        except Exception as err:
            print(f"Exception Raised: {err}")


def main():
    parser = argparse.ArgumentParser(description='Download Images From Webpage')

    # Argument is to input the url to download images from
    parser.add_argument('-u', dest='url', type=str, help='URL to extract links from', required=True)

    args = parser.parse_args()

    if args.url:

        url = args.url

        # Check if the url starts with wither http or https
        if not url.startswith("http") and not url.startswith("https"):
            # Add the https in front of the url
            url = "https://" + url

        # Call to the function
        ImageDownloader(url)


if __name__ == '__main__':
    main()
