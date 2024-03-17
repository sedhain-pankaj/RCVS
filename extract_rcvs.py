from utils.pages_to_parse import pages_to_parse  # to get the start and end page numbers
from utils.save_to_csv import save_to_csv  # to save the results to a CSV file
from utils.constants import BASE_URL  # to get the base URL
from utils.print_clinics_details import process_clinics  # to process the clinic details
from utils.url_parser_bs4 import get_parsed_URL  # to get the parsed URL


# main function
def main():
    # ask for the start and end page numbers
    start, end = pages_to_parse()

    # ask if the results should be saved to a CSV file
    file_name = save_to_csv()

    # iterate over the pages from start page to end page
    for page_number in range(start, end + 1):
        url = f"{BASE_URL}/find-a-vet-practice/?filter-choice=&filter-keyword=&filter-searchtype=practice&filter-pss=true&p={page_number}"
        url_contents = get_parsed_URL(url)  # get the parsed URL from bs4
        if url_contents is None:
            continue  # skip to the next page if the URL contents are not available

        # find all divs with class 'practice' i.e. individual clinic divs
        practices = url_contents.find_all("div", class_="practice")

        # process the clinic details for each page. print the results and save to a CSV file if requested
        process_clinics(practices, page_number, file_name)

    # print a message based on what was returned by the save_to_csv() function
    if file_name:
        print(f"\nTask completed. Results saved to {file_name}.")
    else:
        print("\nTask completed. Only viewing results. Save to CSV was not requested.")


# run the main function if only called from the command line
if __name__ == "__main__":
    main()
