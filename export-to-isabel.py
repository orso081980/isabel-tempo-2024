import gspread
import csv
from datetime import datetime
# Service Account Credentials
gc = gspread.service_account(filename='credential-tempo.json')

# List of Google Sheets URLs
sheet_urls = [
    'https://docs.google.com/spreadsheets/d/18puvaMBVhvuOjVXXO9dVB6rkZI7JlW5AWR9MzWrCMHA/edit?gid=3477297#gid=3477297',
    'https://docs.google.com/spreadsheets/d/1wYWjclZTn1fQ2k9qHJDy3O9547zeZJMQtGPmM0MgJm0/edit?gid=1403137524#gid=1403137524'
]

def parse_tempo_data(rows, headers):
    total_time = 0
    data = {
        'finca': {'time': 0, 'data': []},
        'isabelgroup': {'time': 0, 'data': []},
        'freetime': {'time': 0, 'data': []}
    }

    for row in rows:
        row_dict = dict(zip(headers, row))
        parent_key = row_dict['Parent Key'].strip().lower()

        # Filter for date between June and August
        try:
            work_date = datetime.strptime(row_dict.get('Work date', ''), '%Y-%m-%d %H:%M:%S')
            # print("Parsed Work Date:", work_date)  # Debug: Print work date
            
        except ValueError:
            print("Invalid Date Format for row:", row_dict)  # Debug: Inform about invalid date
            continue  # Skip row if date is invalid

        # Convert 'Hours' to float, skip if it fails
        try:
            hours = float(row_dict['Hours'])
        except ValueError:
            continue

        total_time += hours

        for key in data.keys():
            if key in parent_key:
                data[key]['time'] += hours
                data[key]['data'].append({
                    'Work Description': row_dict['Work Description'],
                    'Billed Hours': row_dict['Billed Hours'],
                    'Work date': row_dict['Work date']
                })

    # Create a new dictionary to store the updated data
    result_data = {}
    for key in data.keys():
        result_data[f"{key}_time"] = data[key]['time']
        result_data[f"{key}_percentage"] = (data[key]['time'] / total_time) * 100 if total_time else 0
        result_data[f"{key}_data"] = data[key]['data']

    return result_data

# CSV writing setup
with open('tempo_report.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write CSV header
    writer.writerow([
        'Sheet Name', 'Finca Time', 'Isabelgroup Time', 'Freetime Time', 
        'Finca Percentage', 'Isabelgroup Percentage', 'Freetime Percentage', 
        'Work Description', 'Billed Hours', 'Work date'
    ])
    
    # Process each sheet and collect results
    for url in sheet_urls:
        sh = gc.open_by_url(url)
        sheet_name = sh.title  
        worksheet = sh.get_worksheet(0) 
        data = worksheet.get_all_values()
        headers = data[0]
        rows = data[1:]
        # print(headers)

        # Parse data for each sheet
        result = parse_tempo_data(rows, headers)
        
        finca_time = result.get('finca_time', 0)
        isabelgroup_time = result.get('isabelgroup_time', 0)
        freetime_time = result.get('freetime_time', 0)
        finca_percentage = result.get('finca_percentage', 0)
        isabelgroup_percentage = result.get('isabelgroup_percentage', 0)
        freetime_percentage = result.get('freetime_percentage', 0)

        # Get only the "finca" data
        finca_data = result.get('finca_data', [])
        
        # Write data to CSV
        if finca_data:
            first_row = [
                sheet_name, finca_time, isabelgroup_time, freetime_time,
                finca_percentage, isabelgroup_percentage, freetime_percentage,
                finca_data[0]['Work Description'], finca_data[0]['Billed Hours'], finca_data[0]['Work date']
            ]
            writer.writerow(first_row)

            # Subsequent rows for this sheet, without repeating the sheet name and totals
            for row in finca_data[1:]:
                writer.writerow([
                    '', '', '', '', '', '', '',
                    row['Work Description'], row['Billed Hours'], row['Work date']
                ])

print("CSV report generated successfully! Check tempo_report.csv")
