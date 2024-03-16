import requests  # to make HTTP requests
from bs4 import BeautifulSoup  # to parse HTML
import csv  # to write to CSV
import time  # to add a delay before retrying
from utils.constants import (
    BASE_URL,
    CLINIC_DETAILS,
    RETRIES,
)  # to get the base URL and clinic details


# iterate over all practices for the current page
def process_clinics(practices, page_number, file_name):
    for index, practice in enumerate(practices):
        # Clinic ID (page number, iteration of the loop + 1)
        clinic_id = f"Page {page_number} No {index + 1}"

        name = get_title(practice)  # get the title of the practice

        # get the link to the practice and prepend the base URL if href is a relative URL
        link = BASE_URL + practice.find("h2", class_="item-title").find("a")["href"]
        soup = get_soup(link)
        website_url = get_website_url(soup)  # get the website URL

        address = get_address(practice)  # get the address

        phone = get_contact(practice)  # get the contact details

        # print the details to the console
        print()  # add a new line
        print(f"{CLINIC_DETAILS[0]}: {clinic_id}")
        print(f"{CLINIC_DETAILS[1]}: {name}")
        print(f"{CLINIC_DETAILS[2]}: {website_url}")
        print(f"{CLINIC_DETAILS[3]}: {address}")
        print(f"{CLINIC_DETAILS[4]}: {phone}")

        # append the details to the data list
        data = [clinic_id, name, website_url, address, phone]

        # write the data to the CSV file
        if file_name:
            with open(file_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)


# read the HTML from the URL and pass on to BeautifulSoup
def get_soup(url):
    for _ in range(RETRIES):
        try:
            html = requests.get(url).content
            return BeautifulSoup(html, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"\nError making request:\n{e}")
            time.sleep(1)  # wait for 1 second before retrying
    return None


# get the title of the practice
def get_title(practice):
    # title is the text inside the h2 tag > a tag
    a_tag = practice.find("h2", class_="item-title").find("a")
    return a_tag.text.strip() if a_tag else None


# get the website URL embedded in the practice page
def get_website_url(soup):
    website_div = soup.find("div", class_="practice-contactSection practice-numbers")
    # check if this div is defined but empty (edge case detected on page 5 no 7)
    if website_div and not website_div.find_all("div"):
        return None
    website_href = website_div.find_all("div")[-1].find("a", string="Website")
    if website_href:
        return website_href["href"]
    else:
        return None


# get the address
def get_address(practice):
    # find the address by concatenating the strings and the span
    address = practice.find("div", class_="item-address")
    if address:
        address_text = address.contents[0].strip()
        postcode = address.find("span", class_="u-nowrap").text.strip()
        return f"{address_text}, {postcode}"
    else:
        return None


# get the contact details
def get_contact(practice):
    # get all child nodes of the span
    contact = practice.find("div", class_="item-contact").find(
        "span", class_="item-contact-tel"
    )
    if contact:
        # return the last item
        return list(contact.children)[-1].strip()
    else:
        return None
