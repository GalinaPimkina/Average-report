def get_items_for_rating(report_type: str) -> tuple:
    # в зависимости от требуемого рейтинга нужно только дописать сюда if с нужными 2 параметрами
    if report_type == 'average_rating':
        return 'brand', 'rating'
    # if report_type == 'average_price':
    #     return 'brand', 'price'


def get_data_for_rating(data: dict, report_type: str) -> dict:
    # получаем словарь с данными, по которым будет вычисляться рейтинг
    rating_dct = {}
    items = get_items_for_rating(report_type)

    for product in data:
        param1 = data[product][items[0]]
        param2 = data[product][items[1]]

        if param1 not in rating_dct:
            rating_dct[param1] = []

        rating_dct[param1].append(param2)

    return rating_dct


def average_rating(data: dict, report_type: str) -> dict:
    # вычисление среднего рейтинга для каждого из брендов, результат отсортирован по убыванию
    data = get_data_for_rating(data, report_type)

    rating = {}
    for key in data:
        lst_ratings = data[key]

        if key not in rating:
            rating[key] = 0

        rat = round(sum(lst_ratings) / len(lst_ratings), 2)
        rating[key] = rat

    return dict(sorted(rating.items(), key=lambda item: item[1], reverse=True))
