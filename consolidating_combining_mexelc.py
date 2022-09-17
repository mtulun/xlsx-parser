from time import sleep
import pandas as pd
import os

input_location = "/Users/taylan/Desktop/xlsx-parser/excel_files/"
output_location = "/Users/taylan/Desktop/xlsx-parser/"

file_list = os.listdir(input_location)
# print(file_list)

final_df = pd.DataFrame()

for files in file_list:
    if files.endswith(".xlsx") and files != "HostedZones":
        df = pd.read_excel(input_location+files)
        final_df = final_df.append(df.get('Value'))

final_df.to_excel(output_location + "finalDf.xlsx", index=False)