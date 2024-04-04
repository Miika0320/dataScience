import csv
import uuid

def add_uuid_column_and_extract_code(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        header.insert(0, 'incidentUUID')

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)

            for row in reader:
                uuid_value = str(uuid.uuid4())
                row.insert(0, uuid_value)

                writer.writerow(row)

if __name__ == "__main__":
    input_file = "../Data/Criminal_Offences_Cleaned.csv"  # Provide the path to your input CSV file
    output_file = "../Data/Final_Criminal_Offences_Cleaned.csv"  # Provide the desired path for the output CSV file
    add_uuid_column_and_extract_code(input_file, output_file)
