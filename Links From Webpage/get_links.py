import argparse
from bs4 import BeautifulSoup
from pprint import pprint
import re
import requests


def get_urls(url):

    # try, except block
    try:

        # Get the page, with the timeout set to 5
        resp = requests.get(url, timeout=5)

        # Check the response code, 200 for valid
        if resp.status_code == 200:
            # Create the soup
            soup = BeautifulSoup(resp.content, "html.parser")

            # Find all the links from the page
            links = soup.find_all('a')

            # Extract the href of the links
            data = [y.attrs['href'] for y in links if y.name == 'a']

            # Create a string with all the links found
            str_data = " ".join(data)

            # Regex is used to filter out the links
            link_regex = re.compile("((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)", re.DOTALL)

            # Gets all the valid links
            regex_links = re.findall(link_regex, str_data)

            # Extract the links from the matched regex
            f_links = [link[0] for link in regex_links]

            # Pretty print
            pprint(f_links)

        # Not a valid response code is given by the site
        else:
            print(f"Status Code: {resp.status_code}, For URL: {url}")

    # Tries to connect to the site
    except requests.exceptions.ConnectionError:
        print(f"No Response From URL: {url}")

    # Generic exception
    except Exception as err:
        print(f"Exception Raised: {err}")


def main():

    parser = argparse.ArgumentParser(description='Extract Links From Webpage')

    # Argument is to input the url to extract links from
    parser.add_argument('-u', dest='url', type=str, help='URL to extract links from', required=True)

    args = parser.parse_args()

    if args.url:

        url = args.url

        # Check if the url starts with wither http or https
        if not url.startswith("http") and not url.startswith("https"):

            # Add the https in front of the url
            url = "https://" + url

        # Call to the function
        get_urls(url)


if __name__ == '__main__':
    main()
