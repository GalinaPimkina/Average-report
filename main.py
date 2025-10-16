from tabulate import tabulate

from average_report_file import write_report_to_csv_file, read_report_from_csv_file
from parser import parser
from rating import average_rating
from products import get_products_data


def main():
    data = parser.parse_args()
    files = data.files
    report_type = data.report

    products_data = get_products_data(files) # словарь продуктов из всех файлов
    aver_rating = average_rating(products_data) # средний рейтинг в виде словаря
    write_report_to_csv_file(aver_rating) # запись в .csv, чтоб получить табличку
    lst = read_report_from_csv_file('report.csv') # чтение рейтингов из файла

    print(tabulate(lst, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()