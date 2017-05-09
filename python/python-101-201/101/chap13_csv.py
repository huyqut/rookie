# CSV - COMMA SEPARATED VALUES

import csv


def csv_reader(file_handle):
    """
    Method 1: Read a csv file from a handle using reader()
    Result is an list of strings
    """
    reader = csv.reader(file_handle)
    for row in reader:
        print(row)


def csv_dict_reader(file_handle):
    """
    Method 1: Read a csv from a handle using DictReader
    Result is an OrderedDict (element is ordered in the way you insert, not by its value)
    """
    reader = csv.DictReader(file_handle)
    for row in reader:
        print(row['first_name'] + ' ' + row['last_name'])

input_path = './data/chap13_input.csv'
with open(input_path, 'r') as file_handle:
    csv_dict_reader(file_handle)

output_path = './data/chap13_output.csv'


def csv_writer(data: list):
    with open(output_path, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter = ',')
        for line in data:
            writer.writerow(line)

data_output = [
    "yolo,sup,mofo".split(','),
    "huy,quang,tran".split(','),
    "123,321,222".split(',')
]
# csv_writer(data_output)


def csv_dict_writer(data: list):
    with open(output_path, 'w', newline = '') as f:
        fields = data[0]
        formatted = [dict(zip(fields, values)) for values in data[1:]]
        writer = csv.DictWriter(f, delimiter = ',', fieldnames = fields)
        writer.writeheader()
        for row in formatted:
            writer.writerow(row)

csv_dict_writer(data_output)