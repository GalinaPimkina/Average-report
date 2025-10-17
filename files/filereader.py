import csv


def write_report_to_csv_file(data: dict):
    # запись данных в .csv файл, чтобы получить таблицу
    with open('files/report/report.csv', 'w', newline='') as csvfile:
        fieldnames = ["", "brand", "rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        i = 1
        for key in data:
            writer.writerow({"": i, "brand": key, "rating": data[key]})
            i += 1


def read_report_from_csv_file(file) -> list:
    # из файла с таблицей получаем вложенный список с данными
    with open(file, newline='') as csvfile:
        lst = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            lst.append(row)
        return lst