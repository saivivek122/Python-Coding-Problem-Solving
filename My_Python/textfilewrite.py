#
# import csv
# headers = [
#     {'name': 'R1','length': 6},{'name': 'R2','length': 6},
#     {'name': 'R3','length': 6},{'name': 'JOB TITLE','length': 65},
#     { 'name': 'specialty','length': 50} ,{ 'name': 'DEPT','length': 6},
#     { 'name': 'OPENDATE','length': 10},
#     { 'name': 'DEADLINE','length': 10},{ 'name': 'DEACTDT','length': 10},
#     { 'name': 'ELIG','length': 11}
#         ]
# data =[('CBT', '5601', 'REF191O', 'Utility Analyst', 'Utility Financials', 'PUC', None, None, None),
#        ('CBT', '1244', '12345', 'Senior Human Resources Analyst', None, 'DPH', '2021-05-12', None, None), ('CBT', '1684', 'REF209F', 'Auditor II', None, 'CTW', '2021-05-13', None, None), ('CBT', '1244', 'REF210P', 'Senior Human Resources Analyst', None, 'CTW', '2021-05-11', None, None),
#        ('CBT', '9202', 'REF216U', 'Airport Communications Dispatcher', 'Dispatching Communications', 'AIR', None, None, None)]
#
#
#
# def create_headers_with_fixed_width(lst):
#     headers_with_fixed_width = []
#     for header in headers:
#         length = header['length']
#         name = header['name']
#         while len(name) < length:
#             name += ' '
#         headers_with_fixed_width.append(name)
#     return headers_with_fixed_width
#
#
# def create_row_data(data):
#     row = []
#     for i, el in enumerate(data):
#         fixed_length = headers[i]['length']
#         while len(el) < fixed_length:
#             el += ' '
#         row.append(el)
#     return row
#
#
# def main():
#     # create headers
#     headers_with_fixed_width = create_headers_with_fixed_width(headers)
#     # create and write data to csv
#     with open("C:\\Users\\sdasyapu\\Desktop\\result.txt", "w+", newline='') as f:
#         writer = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(headers_with_fixed_width)
#         for element in data:
#             row = create_row_data(element)
#             writer.writerow(row)
#
#         f.write("Number of Records  %s" %(len(data)))
#

# if __name__ == '__main__':
#     main()
import os
os.system('Test.py')