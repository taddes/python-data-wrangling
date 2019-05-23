import csv

csvfile = open('data-text.csv', 'r')
document = csv.DictReader(csvfile)

for row in document:
    print(row)