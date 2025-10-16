import csv


def write_report_to_csv_file(data: dict):
    with open('report.csv', 'w', newline='') as csvfile:
        fieldnames = ["", "brand", "rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        i = 1
        for key in data:
            writer.writerow({"": i, "brand": key, "rating": data[key]})
            i += 1


def read_report_from_csv_file(file):
    with open(file, newline='') as csvfile:
        lst = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            lst.append(row)
        return lst