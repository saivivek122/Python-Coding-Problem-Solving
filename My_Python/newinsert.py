import csv

with open('C:\\Users\\sdasyapu\\Desktop\\job_sample.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    reader = list(reader)
    print(reader)
    for row in reader:
        print(row)
