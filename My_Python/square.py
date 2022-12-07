import csv


# Example headers taken from CoSF specification document
headers = [
    {
        'name': 'FIRST_NAME',
        'length': 30
    },
    {
        'name': 'CHOSENFNAME',
        'length': 25
    },
    {
        'name': 'LAST_NAME',
        'length': 30
    }
]


# Some test data
data = [['Brian', 'Bri', 'Molko'], ['Matthew', 'Matt', 'Bellamy']]


# Function to create headers row with fixed width
def create_headers_with_fixed_width(lst):
    # empty list to store data
    headers_with_fixed_width = []
    # loop through the elements of list
    for header in headers:
        length = header['length']
        name = header['name']
        while len(name) < length:
            name += ' '
        headers_with_fixed_width.append(name)
    return headers_with_fixed_width


# Function to create row data with fixed width
def create_row_data(data):
    row = []
    for i, el in enumerate(data):
        fixed_length = headers[i]['length']
        while len(el) < fixed_length:
            el += ' '
        row.append(el)
    return row


def main():
    # create headers
    headers_with_fixed_width = create_headers_with_fixed_width(headers)
    # create and write data to csv
    with open("C:\\Users\\sdasyapu\\Desktop\\result.txt", "w+", newline='') as f:
        writer = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers_with_fixed_width)
        for element in data:
            row = create_row_data(element)
            writer.writerow(row)


if __name__ == '__main__':
    main()
