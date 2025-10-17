import csv


with open('files/products/products1.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'brand', 'price', 'rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'})
    writer.writerow({'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'})
    writer.writerow({'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'})
    writer.writerow({'name': 'iphone 14', 'brand': 'apple', 'price': '799', 'rating': '4.7'})
    writer.writerow({'name': 'galaxy a54', 'brand': 'samsung', 'price': '349', 'rating': '4.2'})


with open('files/products/products2.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'brand', 'price', 'rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'})
    writer.writerow({'name': 'iphone se', 'brand': 'apple', 'price': '429', 'rating': '4.1'})
    writer.writerow({'name': 'galaxy z flip 5', 'brand': 'samsung', 'price': '999', 'rating': '4.6'})
    writer.writerow({'name': 'redmi 10c', 'brand': 'xiaomi', 'price': '149', 'rating': '4.1'})
    writer.writerow({'name': 'iphone 13 mini', 'brand': 'apple', 'price': '599', 'rating': '4.5'})