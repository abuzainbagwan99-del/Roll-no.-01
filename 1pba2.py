import re
from datetime import datetime

def identify_dates(text):
    # Regex pattern for DD-MM-YYYY format
    date_pattern = re.compile(
        r'(?<![\d-])(?P<day>\d{2})-'
        r'(?P<month>\d{2})-'
        r'(?P<year>\d{4})(?!\d)'
    )

    # Pattern for dates written in YYYY-MM-DD format
    wrong_format_pattern = re.compile(
        r'(?<!\d)\d{4}-\d{2}-\d{2}(?!\d)'
    )

    valid_dates = []
    invalid_dates = []
    wrong_format_dates = []

    # Find and validate dates in DD-MM-YYYY format
    for match in date_pattern.finditer(text):
        date_str = match.group()

        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            valid_dates.append(date_str)
        except ValueError:
            invalid_dates.append(date_str)

    # Identify dates written in the wrong format
    for match in wrong_format_pattern.finditer(text):
        wrong_date = match.group()

        if wrong_date not in wrong_format_dates:
            wrong_format_dates.append(wrong_date)

    print("\n--- DATE IDENTIFICATION REPORT ---")

    print("\nValid dates:")
    if valid_dates:
        for date in valid_dates:
            print(date)
    else:
        print("No valid dates found.")

    print("\nInvalid calendar dates:")
    if invalid_dates:
        for date in invalid_dates:
            print(date)
    else:
        print("No invalid calendar dates found.")

    print("\nDates in the wrong format:")
    if wrong_format_dates:
        for date in wrong_format_dates:
            print(date)
    else:
        print("No incorrectly formatted dates found.")


# Main program
text = input("Enter a text string: ")
identify_dates(text)