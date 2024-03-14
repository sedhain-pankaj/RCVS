# Extract RCVS Website Data

This Python script is used to scrape data from the RCVS (Royal College of Veterinary Surgeons) [website](https://findavet.rcvs.org.uk/find-a-vet-practice/). It retrieves information about veterinary practices, including the clinic ID, name, website URL, address, and phone number.

## How to Run

1. Make sure you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

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

## Data

The script retrieves the following data for each veterinary practice:

- Clinic ID: A unique identifier for the clinic, based on the page number and the order of the clinic on the page.
- Name: The name of the clinic.
- Website URL: The URL of the clinic's website.
- Address: The address of the clinic.
- Phone: The phone number of the clinic.

The data is either printed to the terminal or saved to an Excel file, depending on your input.
