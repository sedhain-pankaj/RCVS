import requests # to make HTTP requests
from bs4 import BeautifulSoup # to parse HTML
import pandas as pd # to create a dataframe


# read the HTML from the URL and pass on to BeautifulSoup
def get_soup(url):
    html = requests.get(url).content
    return BeautifulSoup(html, "html.parser")


# get the title of the practice
def get_title(practice):
    # title is the text inside the h2 tag > a tag
    a_tag = practice.find("h2", class_="item-title").find("a")
    return a_tag.text.strip()


# get the website URL 
def get_website_url(soup):
    # find a div with class practice-contactSection practice-numbers and get the last div inside it
    website_div = soup.find("div", class_="practice-contactSection practice-numbers").find_all("div")[-1]
    # check if the div contains an anchor tag with the text "Website"
    website_href = website_div.find("a", string="Website")
    return website_href['href'] if website_href else None


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
    contact = practice.find("div", class_="item-contact").find("span", class_="item-contact-tel")
    if contact:
        # return the last item
        return list(contact.children)[-1].strip()
    else:
        return None


# process the clinic details for each page
def process_clinics(practice, practices, page_number, data):
    # Clinic ID (page number, iteration of the loop + 1)
    clinic_id = f"Page {page_number} No {practices.index(practice) + 1}"
    name = get_title(practice) # get the title of the practice

    # get the link to the practice and prepend the base URL if href is a relative URL
    link = 'https://findavet.rcvs.org.uk' + practice.find("h2", class_="item-title").find("a")["href"]
    soup = get_soup(link)
    website_url = get_website_url(soup) # get the website URL

    address = get_address(practice) # get the address
    phone = get_contact(practice) # get the contact details

    # append the details to the data list
    data.append([clinic_id, name, website_url, address, phone])


# main function
def main():
    # ask the user for which page to start and end
    start = int(input("Enter the start page: "))
    end = int(input("Enter the end page: "))

    # ask the user if they want to save the results to a Excel file
    save_to_excel = input("Do you want to save the results to an Excel file? (y/n): ").lower().strip()
    print ("Processing...")
    data = [] # create an empty list to store the results

    # iterate over the pages from start page to end page
    for page_number in range(start, end + 1):
        url = f"https://findavet.rcvs.org.uk/find-a-vet-practice/?filter-choice=&filter-keyword=&filter-searchtype=practice&filter-pss=true&p={page_number}"
        soup = get_soup(url) # call the get_soup function

        # find all divs with class 'practice'
        practices = soup.find_all("div", class_="practice")

        # iterate over all practices for the current page
        for practice in practices:
            process_clinics(practice, practices, page_number, data)

    # if the user wants to save the results to an Excel file
    if save_to_excel == "y":
        file_name = input("Enter the file name: ") # ask the user for the file name
        if not file_name.endswith(".xlsx"):
            file_name += ".xlsx"
        # create a dataframe from the data list
        df = pd.DataFrame(data, columns=["Clinic ID", "Name", "Website URL", "Address", "Phone"])
        df.to_excel(file_name, index=False)
        print(f"Results saved to {file_name}") # print a message
    elif save_to_excel == "n":
        print (pd.DataFrame(data, columns=["Clinic ID", "Name", "Website URL", "Address", "Phone"])) # print the results


# run the main function if called from the command line
if __name__ == "__main__":
    main()