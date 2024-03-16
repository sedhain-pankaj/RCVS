from utils.pages_to_parse import pages_to_parse  # to get the start and end page numbers
from utils.save_to_csv import save_to_csv  # to save the results to a CSV file
from utils.constants import BASE_URL  # to get the base URL and clinic details
from utils.parse_clinics_details import (
    get_soup,
    process_clinics,
)  # to get the clinic details


# main function
def main():
    # start and end page numbers
    start, end = pages_to_parse()

    # call the save_To_CSV function and store the file name
    file_name = save_to_csv()

    # iterate over the pages from start page to end page
    for page_number in range(start, end + 1):
        url = f"{BASE_URL}/find-a-vet-practice/?filter-choice=&filter-keyword=&filter-searchtype=practice&filter-pss=true&p={page_number}"
        soup = get_soup(url)  # call the get_soup function
        if soup is None:
            continue  # skip to the next page if the soup is None

        # find all divs with class 'practice'
        practices = soup.find_all("div", class_="practice")

        # process the clinic details for each page
        process_clinics(practices, page_number, file_name)

    # print a message depending on whether the results were saved to a CSV file
    if file_name:
        print(f"\nTask completed. Results saved to {file_name}.")
    else:
        print("\nTask completed. Only viewing results. Save to CSV was not requested.")


# run the main function if called from the command line
if __name__ == "__main__":
    main()
