import argparse
import csv


def get_one_type(string):
    return '_'.join([word for word in string.split('-')])


parser = argparse.ArgumentParser(description='Get list of files names')
parser.add_argument(
    '--files',
    nargs='+',
    type=str,
    help='provide a file name',
    required=True,
)
parser.add_argument(
    '--report',
    type=get_one_type,
    help='provide a report name',
    required=True,
)

data = parser.parse_args()
files = data.files
report_type = data.report


def get_products_data(files: list):
    products_data = {}

    for d in files:
        with open(d, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products_data[row['name']] = {'brand': row['brand'], 'price': int(row['price']), 'rating': float(row['rating'])}

    return products_data
