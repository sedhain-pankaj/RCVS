import csv  # to write to CSV
import os  # to check if a file exists
from utils.constants import CLINIC_DETAILS  # to get the clinic details


# Yes or No prompt
def ask_yes_no(question):
    while True:
        answer = input(question).lower().strip()
        if answer in ["y", "n"]:
            return answer == "y"
        print("Invalid input. Please enter 'y' or 'n'.")


# get the file name from the user
def get_file_name():
    while True:
        file_name = input("Enter the file name: ").strip()

        if not file_name.endswith(".csv"):
            file_name += ".csv"

        if os.path.exists(file_name):
            if ask_yes_no(
                f"\n{file_name} already exists. Do you want to overwrite it? (y/n): "
            ):
                print(f"Overwriting {file_name}...")
            else:
                continue

        return file_name


# save the results to a CSV file. None or file name is returned
def save_to_csv():
    if not ask_yes_no("\nDo you want to save the results to a CSV file? (y/n): "):
        print("Only viewing results. Not saving to CSV.")
        return None

    file_name = get_file_name()

    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(CLINIC_DETAILS)
    except PermissionError:
        print(f"Permission denied: '{file_name}'")
        return None

    return file_name
