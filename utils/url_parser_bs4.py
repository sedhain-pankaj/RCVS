import requests  # to make HTTP requests
from bs4 import BeautifulSoup  # to parse HTML
import time  # to add a delay before retrying
from utils.constants import RETRIES  # to get the number of retries


# read the HTML from the URL and pass on to BeautifulSoup
def get_parsed_URL(url):
    for _ in range(RETRIES):
        try:
            html = requests.get(url).content
            return BeautifulSoup(html, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"\nError making request:\n{e}")
            time.sleep(1)  # wait for 1 second before retrying
    return None
