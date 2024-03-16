# ask the user for which page to start and end
def pages_to_parse():
    while True:
        try:
            start = int(input("Enter the start page: ").strip())
            end = int(input("Enter the end page: ").strip())

            if start < 1 or end < 1:
                print("Invalid input. Start and end pages must be positive numbers.\n")
                continue

            if start > end:
                print(
                    "Invalid input. End page must be greater than start page.\n"
                    "Use the same number for both to parse only a single page.\n"
                )
                continue

            return start, end  # return the start and end page numbers

        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
