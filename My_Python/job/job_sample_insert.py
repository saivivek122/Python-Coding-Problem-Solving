import csv


def all_data():
    with open('C:\\Users\\sdasyapu\\Desktop\\job_sample.csv', 'r') as f:
        reader = csv.DictReader(f)
        reader = list(reader)
    # print(reader)
    return reader


def take_data(reader):
    return reader


take_data(all_data())
all_data()
