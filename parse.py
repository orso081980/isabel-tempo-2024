import gspread
import json

# Service Account Credentials
gc = gspread.service_account(filename='credential-tempo.json')

# List of Google Sheets URLs
sheet_urls = [
    'https://docs.google.com/spreadsheets/d/1W_fGj6EvcCiESrd26f_vPh9edEfJVHeluufRxVd1NA0/edit?gid=1412630792#gid=1412630792',
    'https://docs.google.com/spreadsheets/d/1z6y7Z70jsLEx9brwFWvAFlVLQuMaM6weLAbqdBWqQtk/edit',
    'https://docs.google.com/spreadsheets/d/1YUjck0k1ndXZeiIj_98vTjREVI1e6589Ta0HNr28SaI/edit?gid=1094173024#gid=1094173024',
    'https://docs.google.com/spreadsheets/d/1aieY-9msLcWH4tVJ1EJWdvjhZxFIcPFJMouWAZ5PNhk/edit?gid=1787780418#gid=1787780418',
    'https://docs.google.com/spreadsheets/d/1porAAIejY4m-YrTDPgTePnnwa1-TUFh0UUiBhacjRRw/edit?gid=454204543#gid=454204543',
    'https://docs.google.com/spreadsheets/d/14D0cI9HeO8pwXO2BMqFkyXL2QMrsLEI7idzrzAL15WU/edit#gid=1465229029',
    'https://docs.google.com/spreadsheets/d/1vaeEOGYmp9fExMnFRQ_MVXoN8IVdZ2PD9PRV95wypJs/edit#gid=337465910',
    'https://docs.google.com/spreadsheets/d/1-dfxg8E_F-L7eepAAiygQ9n2N0XOL-QJycNmP84bxvg/edit#gid=796197169',
    'https://docs.google.com/spreadsheets/d/13np2xdB6KZcYQOm-3H0414wk1EB2RY78ubwyBLqq740/edit#gid=2010614004',
    'https://docs.google.com/spreadsheets/d/1r41LYfBe5491iuGvA_M2ayfk18ZFQQwXXWWvmVGDCdQ/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1bQ2edw0ZLaThOw7cB9Kw_iOlSfGqG7T6Kx0nvgxi7ZY/edit?gid=1167031740#gid=1167031740',
    'https://docs.google.com/spreadsheets/d/1PjfG9oCWzZBJAASRO2TRAk-koAU07VnvVhtc2mE7PTs/edit?gid=823307320#gid=823307320',
    'https://docs.google.com/spreadsheets/d/1EqardPBwYfle6ZYe_Bni1WOmap2IP1xMUmv9ciNOucw/edit?gid=1797234630#gid=1797234630',
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
        hours = float(row_dict['Hours'])
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
        result_data[f"{key}_data"] = data[key]['data']  # Move data under the new key

    return result_data

# Process each sheet and collect results
results = {}
for url in sheet_urls:
    sh = gc.open_by_url(url)
    sheet_name = sh.title  
    worksheet = sh.get_worksheet(0) 
    data = worksheet.get_all_values()
    headers = data[0]
    rows = data[1:]
    results[sheet_name] = parse_tempo_data(rows, headers)

# Convert results to JSON
json_data = json.dumps(results, indent=4)

# Write data to a JSON file
with open('tempo_report.json', 'w') as json_file:
    json_file.write(json_data)

print("Report generated successfully! Check tempo_report.json")