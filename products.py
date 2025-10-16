import csv


def get_products_data(files: list):
    products_data = {}

    for d in files:
        with open(d, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products_data[row['name']] = {'brand': row['brand'], 'price': int(row['price']), 'rating': float(row['rating'])}

    return products_data