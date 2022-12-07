import csv

with open('C:\\Users\\sdasyapu\\Desktop\\raw_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    # next(reader)
    reader = list(reader)
    # print(reader)
    a = []
    for line in reader:
        a.append(line['exam_a'])
    print(a)
