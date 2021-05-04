import csv

filename = 'loans_causal_schema.csv'

fields = []
rows = []

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for item in rows:
	if item[0] == '':
		rows.remove(item)

for elements in rows:
	if elements[44] == 'True':
		print(elements)



