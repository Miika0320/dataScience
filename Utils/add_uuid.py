import csv
import uuid

def add_uuid_column_and_extract_code(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        header.insert(0, 'incidentUUID')
        header.insert(3, 'crimeCode')  # Inserting a new column for the crime code

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)

            for row in reader:
                uuid_value = str(uuid.uuid4())
                row.insert(0, uuid_value)

                # Extracting the crime code from primViolat column
                prim_violat = row[3]  # Assuming primViolat is at index 3
                code = prim_violat.split('(')[-1].split(')')[0]

                # Removing brackets from primViolat column
                row[3] = prim_violat.split('(')[0].strip()

                # Inserting the extracted code into the new column
                row.insert(3, code)

                writer.writerow(row)

if __name__ == "__main__":
    input_file = "../Data/Criminal_Offences_Cleaned.csv"  # Provide the path to your input CSV file
    output_file = "../Data/Final_Criminal_Offences_Cleaned.csv"  # Provide the desired path for the output CSV file
    add_uuid_column_and_extract_code(input_file, output_file)
