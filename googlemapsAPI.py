from dataclasses import dataclass
from dataclasses_json import dataclass_json
import requests
import openpyxl

# Assuming your API key and other details are correctly set
key = 'AIzaSyD5xNG5OiWwHhiimFPkXMOqyIWY_jaZqhI'
address = 'Shefford Rez'  # Example address input

def getGeoCoord(address):
    params = {
        'key': key,
        'address': address
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        # Iterate through address components to find the neighborhood
        for component in result['address_components']:
            if 'neighborhood' in component['types']:
                neighborhood = component['long_name']
                return neighborhood
        # If no neighborhood is found, return a placeholder or None
        return "Neighborhood not found"
    else:
        return "Error: " + data['status']
# writeToExcel()
def getPlaceInfo(query):
    # Parameters for the API request
    params = {
        'query': query,
        'key': key
    }
    # Google Places API Text Search endpoint
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['status'] == 'OK':
        # Assume the first result is the most relevant
        result = data['results'][0]
        
        # Extract the formatted address
        formatted_address = result.get('formatted_address', 'Address not found')
        
        return formatted_address
    else:
        return "Error: " + data['status']
    
def writeToExcel():
    # Load the workbook and select the active worksheet
    workbook_path = 'aptinfoOn.xlsx'  # Specify the path to your Excel file
    workbook = openpyxl.load_workbook(workbook_path)
    sheet = workbook.active

    # Starting from row 2, read addresses from column A and apply your neighborhood logic
    for row in range(2, sheet.max_row + 1):
        address_cell = sheet[f'A{row}']
        address = address_cell.value

        

        # Apply your neighborhood logic here
        # For demonstration, let's just say every neighborhood is "Example Neighborhood"
        # Replace this with your actual logic
        realladdress = getPlaceInfo(address)
        neighborhood = getGeoCoord(realladdress)
        print(realladdress,neighborhood)
        # Write the neighborhood to column H
        sheet[f'H{row}'] = neighborhood

    # Save the workbook with the changes
    workbook.save(filename='aptinfoOn.xlsx')
writeToExcel()
# Example usage
# query = 'shefford rez, Ottawa, On, CA'  # Your search query
# result = getPlaceInfo(query)
# print(result)
# final = getGeoCoord('396 Blake Blvd, Ottawa, ON K1L 6L2')
# print(final)