import requests
from bs4 import BeautifulSoup
import csv


def extract_text_and_images(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # divs = soup.find_all("div", attrs={"role": "region"})
    all_tags = soup.find_all(["div", "h1", "h2", "p"])

    pictures = soup.find_all("picture")

    # Extract text
    text_set = set()
    if all_tags:
        for div in all_tags:
            text = div.get_text()
            sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
            text_set.update(sentences)

    text_list = list(text_set)
    # Extract image URLs
    image_urls = []
    if all_tags:
        for div in all_tags:
            images = div.find_all("img")
            for img in images:
                img_url = img["src"]
                image_urls.append(img_url)

    # Extract picture URLs
    picture_urls = []
    if pictures:
        for picture in pictures:
            images = picture.find_all("img")
            picture_urls.extend(img["src"] for img in images)
    # Save text to CSV file
    with open("./Data/text.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text"])
        writer.writerows([[text] for text in text_list])

    # Save image URLs to CSV file
    with open("./Data/image_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Image URL"])
        writer.writerows([[url] for url in image_urls])

    # Save picture URLs to CSV file
    with open("./Data/picture_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Picture URL"])
        writer.writerows([[url] for url in picture_urls])


url = "https://www.booking.com/index.en-gb.html?"
extract_text_and_images(url)
print("Crawling and CSV writing completed!")
