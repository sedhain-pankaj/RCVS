import csv  # to write to CSV
from utils.constants import (
    BASE_URL,
    CLINIC_DETAILS,
)  # to get the base URL and clinic details
from utils.url_parser_bs4 import get_parsed_URL  # to get the parsed URL
from utils.parse_clinics_details import (
    get_title,
    get_embedded_website_url,
    get_address,
    get_contact,
)  # to get the clinic details


# iterate over all practices for the current page
def process_clinics(practices, page_number, file_name):
    for index, practice in enumerate(practices):
        # Clinic ID (page number, iteration of the loop + 1)
        clinic_id = f"Page {page_number} No {index + 1}"  # e.g. "Page 2 No 5"

        name = get_title(practice)  # get the title of the practice
        address = get_address(practice)  # get the address
        phone = get_contact(practice)  # get the contact details

        # get the link to the practice and prepend the base URL if href is a relative URL
        link = BASE_URL + practice.find("h2", class_="item-title").find("a")["href"]
        url_contents = get_parsed_URL(link)  # get the parsed URL
        website_url = get_embedded_website_url(
            url_contents
        )  # get the website inside the practice page

        # print the details to the console
        print()  # add a new line
        print(f"{CLINIC_DETAILS[0]}: {clinic_id}")
        print(f"{CLINIC_DETAILS[1]}: {name}")
        print(f"{CLINIC_DETAILS[2]}: {website_url}")
        print(f"{CLINIC_DETAILS[3]}: {address}")
        print(f"{CLINIC_DETAILS[4]}: {phone}")

        # write the data to the CSV file
        if file_name:
            with open(file_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([clinic_id, name, website_url, address, phone])
