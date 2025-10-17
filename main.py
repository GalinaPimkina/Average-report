from tabulate import tabulate

from files.filereader import write_report_to_csv_file, read_report_from_csv_file
from utils.parser import parser
from utils.rating import average_rating
from utils.products import get_products_data


def main():
    data = parser.parse_args()
    files = data.files
    report_type = data.report

    products_data = get_products_data(files) # словарь продуктов из всех файлов
    av_rating = average_rating(products_data, report_type) # средний рейтинг в виде словаря
    write_report_to_csv_file(av_rating) # запись в .csv, чтоб получить красивую табличку
    lst = read_report_from_csv_file('files/report/report.csv') # чтение рейтингов из файла

    print(tabulate(lst, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Check file location.\nFile's name must be like 'products1.csv'\nReport's name must be like 'average-report'")