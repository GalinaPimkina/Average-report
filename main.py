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


def get_brand_rating_data(data: dict):
    rating_dct = {}

    for product in data:
        brand = data[product]['brand']
        rating = data[product]['rating']

        if brand not in rating_dct:
            rating_dct[brand] = []

        rating_dct[brand].append(rating)

    return rating_dct


def average_rating(data: dict):
    brand_rating_data = get_brand_rating_data(data)

    rating = {}
    for brand in brand_rating_data:
        lst_ratings = brand_rating_data[brand]

        if brand not in rating:
            rating[brand] = 0

        rat = round(sum(lst_ratings) / len(lst_ratings), 2)
        rating[brand] = rat

    return dict(sorted(rating.items(), key=lambda item: item[1], reverse=True))


print(average_rating(get_products_data(files)))
