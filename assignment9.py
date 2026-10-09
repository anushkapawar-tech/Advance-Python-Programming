import csv
import json
from pathlib import Path


def csv_to_json(input_file, output_file):

    # Get the folder where this Python file is located
    folder = Path(__file__).parent

    input_path = folder / input_file
    output_path = folder / output_file

    # Create sample CSV if it does not exist
    if not input_path.exists():
        with open(input_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Age", "Course"])
            writer.writerow([101, "Prajwal", 20, "CSE"])
            writer.writerow([102, "Rahul", 21, "IT"])
            writer.writerow([103, "Ankit", 20, "AI"])

        print("students.csv created successfully!")

    # Read CSV
    with open(input_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Write JSON
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("CSV converted to JSON successfully!")
    print("JSON file:", output_path)


# Run program
csv_to_json("students.csv", "students.json")