import csv
import json

def extract_data_from_json(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract required data from JSON
    fieldnames = list(data[0].keys())  # Get fieldnames from the first item in the JSON data
    extracted_data = []
    for item in data:
        extracted_data.append(item)

    # Save extracted data to CSV
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extracted_data)

    print(f"Data extracted from JSON file '{json_file}' and saved to CSV file '{csv_file}'.")
