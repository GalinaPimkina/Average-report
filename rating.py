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
