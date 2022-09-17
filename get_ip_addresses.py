import csv
import glob
import pandas as pd

# Specifying the path to csv files
path = '/Users/taylan/Desktop/xlsx-parser/excel_files'

# Csv files in the path
excel_files_list = glob.glob(path + "/*.xlsx")

# Use this list to convert "DataFrame" to "List" object.
some_list = []

# Use this list to create csv file.
formatted_list = []

for files in excel_files_list:

    # Load Excel file using Pandas with `sheet_name=None` read all sheets
    df_dict = pd.read_excel(files, sheet_name=None)

    # Combine data from all worksheets
    df_all = pd.concat(df_dict.values(), ignore_index=True)

    some_list = df_all.values.tolist()

    for items in some_list:
        formatted_list.append(items)

with open('value_list/sample.csv', mode='w') as csv_file:
    field_names = ['AliasDNSName','AliasEvaluateTargetHealth','AliasHostedZoneId','Failover','GeoLocationContinentCode','GeoLocationCountryCode','GeoLocationSubdivisionCode','HealthCheckId','Name','Region','SetIdentifier','TTL','Type','Weight','Value']
    writer = csv.writer(csv_file)
    writer.writerow(field_names)
    writer.writerows(formatted_list)