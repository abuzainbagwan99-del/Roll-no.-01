import csv
import json
import os


def read_csv(input_path):
    """Read CSV data and return a list of dictionaries."""
    with open(input_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def write_json(output_path, data):
    """Write data to a JSON file in formatted form."""
    with open(output_path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def convert_csv_to_json(input_path, output_path):
    """Convert a CSV file into a JSON file."""
    data = read_csv(input_path)
    write_json(output_path, data)
    return len(data)


def main():
    input_path = "students.csv"
    output_path = "students.json"

    # Create a sample CSV file
    sample_data = [
        ["Roll_No", "Name", "Age", "Course"],
        ["1", "Amit", "20", "Computer Science"],
        ["2", "Sara", "21", "Information Technology"],
        ["3", "Rahul", "19", "Data Science"]
    ]

    with open(input_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)

    # Display the CSV file contents
    print("Contents of CSV file:")
    with open(input_path, mode="r", encoding="utf-8") as file:
        print(file.read())

    # Convert CSV to JSON
    count = convert_csv_to_json(input_path, output_path)

    print("CSV to JSON conversion completed successfully!")
    print("Number of converted rows:", count)
    print("JSON file location:", os.path.abspath(output_path))

    # Display the resulting JSON file
    print("\nContents of JSON file:")
    with open(output_path, mode="r", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    main()