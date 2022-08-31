import os
import glob
from time import sleep
import pandas as pd
import json

# specifying the path to csv files
path = '/Users/taylan/Desktop/spread_sheet/excel_files'

# csv files in the path
excel_files_list = glob.glob(path + "/*.xlsx")

sheet_names_list = []
values_list = []
all_sheets_and_xlsx = []

concatenated_list = []

for files in excel_files_list:

    all_sheets_and_xlsx.append(pd.read_excel(files, sheet_name= None))

    # concatenated_list = pd.concat(all_sheets_and_xlsx, ignore_index=True)
    
    # concatenated_list.to_excel('ConcatenateRoute53Files.xlsx', index=False)

    # print(files)

    print(all_sheets_and_xlsx)

    # sleep(0.85)
    # For sheet names
    f = pd.ExcelFile(files)
    countz = 1

    for name in f.sheet_names:
        if name != 'HostedZones':
            # print(f'{countz}\t'+ name+"\n")
            countz += 1
            sheet_names_list.append(name)

    # write method supports 'str' type, convert list to str with '\n'
    joint = '\n'.join(sheet_names_list)

    with open('value_list/sheet_names.txt', 'w') as fp:
        fp.write(joint)

    # Load Excel file using Pandas with `sheet_name=None` read all sheets
    df_dict = pd.read_excel(files, sheet_name=None)

    # combine data from all worksheets
    df_all = pd.concat(df_dict.values(), ignore_index=True)


    value_dict = df_all.get('Value')
    values_list = format(value_dict.to_string())
    # concatenated_list ='\n'.join(value_dict)

    with open('value_list/sample.txt', 'w') as s:
        s.write(values_list)


 
n = sheet_names_list.__len__()
print(n)


# print(all_sheets_and_xlsx)