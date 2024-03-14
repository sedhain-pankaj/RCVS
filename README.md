# Extract RCVS Website Data

This Python script is used to scrape data from the RCVS (Royal College of Veterinary Surgeons) <a href="https://findavet.rcvs.org.uk/find-a-vet-practice/?filter-choice=name&filter-keyword=&filter-searchtype=practice&filter-pss=true&p=1" target="_blank">website</a>. It retrieves information about veterinary practices, including the clinic ID, name, website URL, address, and phone number in UK.

## How to Run

1. Make sure you have Python installed on your machine. You can download Python from the <a href="https://www.python.org/downloads/" target="_blank">Python's official website</a>.

2. Install the required Python libraries by running the following command in your terminal:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

3. Run the script by typing the following command in your terminal:

```bash
python extract_rcvs.py
```

## User Prompts

When you run the script, it will ask you for the following inputs:

- Start page: The page number to start scraping data from.
- End page: The page number to stop scraping data at.
- Save to Excel: Whether you want to save the scraped data to an Excel file. If you enter 'y', it will ask you for a file name and save the data to an Excel file with that name. If you enter 'n', it will print the data to the terminal.

## Demo

### If you choose to save the data to an Excel file

![Save to Excel](/demo%20terminal%20-%20save%20to%20excel.png)

### If you choose to just view the data in the terminal

![Print to Terminal](/demo%20terminal%20-%20just%20viewing.png)

### The Excel file with the scraped data of Page 1

![Excel File](/demo%20of%20excel.png)

## Data

The script retrieves the following data for each veterinary practice:

- Clinic ID: A unique identifier for the clinic, based on the page number and the order of the clinic on the page.
- Name: The name of the clinic.
- Website URL: The URL of the clinic's website.
- Address: The address of the clinic.
- Phone: The phone number of the clinic.

The data is either printed to the terminal or saved to an Excel file, depending on your input.
