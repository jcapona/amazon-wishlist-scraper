import argparse
import scraper


parser = argparse.ArgumentParser()
parser.add_argument("url",
        help="The url for the Amazon wishlist to scrape.", type=str)
args = parser.parse_args()
url = args.url

print(scraper.get_data(url))
