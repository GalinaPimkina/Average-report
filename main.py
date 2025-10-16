from parser import parser
from rating import average_rating
from products import get_products_data


def main():
    data = parser.parse_args()
    files = data.files
    report_type = data.report

    products_data = get_products_data(files)
    aver_rating = average_rating(products_data)
    print(aver_rating)


if __name__ == "__main__":
    main()