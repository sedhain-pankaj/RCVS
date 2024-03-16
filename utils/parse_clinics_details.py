# get the title of the practice
def get_title(practice):
    # title is the text inside the h2 tag > a tag
    a_tag = practice.find("h2", class_="item-title").find("a")
    return a_tag.text.strip() if a_tag else None


# get the embedded website URL for a clinic 
def get_embedded_website_url(soup):
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
