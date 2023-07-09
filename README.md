# Booking.com Web Crawler

This web crawler is designed to extract text and image URLs from the Booking.com website. It uses Python along with the `requests` and `BeautifulSoup` libraries for web scraping.

## Requirements

- Python 
- requests library
- BeautifulSoup library

## Usage

- The crawler will extract the text and image URLs from the provided Booking.com page and save them in separate CSV files (text.csv, image_urls.csv, picture_urls.csv), which will be located in the Data folder.
- Run it with the following commands

``` bash 
pip install -r requirements.txt
python crawling.py 