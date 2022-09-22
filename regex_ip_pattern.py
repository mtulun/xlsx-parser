import re
import csv

# opening and reading the file
with open('value_list/document.txt') as fh:
    fstring = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# second_pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
# {3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')

# initializing the list object
lst=[]

# extracting the IP addresses
for line in fstring:
    lst.append(pattern.search(line))

# displaying the extracted IP addresses for check
# print(lst)

with open('FILE.csv', mode='w') as csv_file:
    field_names = ['Regex']
    writer = csv.writer(csv_file)
    writer.writerow(field_names)
    writer.writerows(lst)