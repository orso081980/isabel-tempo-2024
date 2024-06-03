import gspread
import json

# Service Account Credentials
gc = gspread.service_account(filename='credential-tempo.json')

# List of Google Sheets URLs
sheet_urls = [
    'https://docs.google.com/spreadsheets/d/14D0cI9HeO8pwXO2BMqFkyXL2QMrsLEI7idzrzAL15WU/edit#gid=1465229029',
    'https://docs.google.com/spreadsheets/d/1vaeEOGYmp9fExMnFRQ_MVXoN8IVdZ2PD9PRV95wypJs/edit#gid=337465910',
    'https://docs.google.com/spreadsheets/d/1-dfxg8E_F-L7eepAAiygQ9n2N0XOL-QJycNmP84bxvg/edit#gid=796197169',
    'https://docs.google.com/spreadsheets/d/13np2xdB6KZcYQOm-3H0414wk1EB2RY78ubwyBLqq740/edit#gid=2010614004',
    'https://docs.google.com/spreadsheets/d/1r41LYfBe5491iuGvA_M2ayfk18ZFQQwXXWWvmVGDCdQ/edit#gid=0'
]

# Function to parse the data
def parse_tempo_data(rows, headers):
    finca_time = 0
    isabelgroup_time = 0
    freetime_time = 0
    total_time = 0
    finca_data = []  # List to store additional data for 'finca'

    for row in rows:
        row_dict = dict(zip(headers, row))
        parent_key = row_dict['Parent Key'].strip().lower()  # Convert to lowercase and strip any extra spaces
        hours = float(row_dict['Hours'])
        total_time += hours

        if "finca" in parent_key:
            finca_time += hours
            # Collect additional data for 'finca'
            finca_data.append({
                'Work Description': row_dict['Work Description'],
                'Billed Hours': row_dict['Billed Hours'],
                'Work date': row_dict['Work date']
            })
        elif "isabelgroup" in parent_key:
            isabelgroup_time += hours
        elif "freetime" in parent_key:
            freetime_time += hours

    finca_percentage = (finca_time / total_time) * 100 if total_time else 0
    isabelgroup_percentage = (isabelgroup_time / total_time) * 100 if total_time else 0
    freetime_percentage = (freetime_time / total_time) * 100 if total_time else 0

    return {
        'finca_time': finca_time,
        'isabelgroup_time': isabelgroup_time,
        'freetime_time': freetime_time,
        'finca_percentage': finca_percentage,
        'isabelgroup_percentage': isabelgroup_percentage,
        'freetime_percentage': freetime_percentage,
        'finca_data': finca_data  # Include additional data for 'finca'
    }

# Process each sheet and collect results
results = {}
for url in sheet_urls:
    sh = gc.open_by_url(url)
    sheet_name = sh.title  # Use the sheet's title as the key
    worksheet = sh.get_worksheet(0)  # Assuming the data is in the first worksheet
    data = worksheet.get_all_values()
    headers = data[0]
    rows = data[1:]
    results[sheet_name] = parse_tempo_data(rows, headers)

# Convert results to JSON
json_data = json.dumps(results, indent=4)

# Write JSON data to a file
with open('tempo_report.json', 'w') as json_file:
    json_file.write(json_data)

print("Report generated successfully! Check tempo_report.json")
