from app.data_loader import read_dataset
path = "../assets/beer_db_v4.csv"

from typing import List, Dict



def beer_styles_per_country(data: list[dict],) -> dict[str,int]:
    """
    Gives a dictionary which tells me how many beer styles per country there are.
    :param data: this is the list which contains a dictionary with all the data.
    :return: this gives me a dictionary with a string and a lists.

    """

    count1_styles: dict(str, list[str]) = {}

    for beer in data:

        if beer ['country'] not in count1_styles:
            lst: list = []
            lst.append(beer['style_name'])
            count1_styles[beer['country']] = lst

        else:
            count1_styles[beer['country']].append(beer['style_name'])

    count2_styles:  dict(str, list(str)) = {}

    for country, styles in count1_styles.items():
        special_items_set = set(['unclassified'])
        special_list: list = []

        for style in styles:

            if style not in special_items_set:
                special_items_set.add(style)
                special_list.append(style)

            else:
                pass

        count2_styles[country] = special_list


    count3_styles: dict[str, int] = {}

    for country, styles in count2_styles.items():
        count3_styles[country] = len(styles)

    sorted_styles = dict(sorted(count3_styles.items(), key = lambda item: item[1], reverse = True))

    return sorted_styles

print(beer_styles_per_country(read_dataset(path)))
print()

def total_beer_production(data: list[dict]) -> dict[str, int]:
    """
    This funtion computes how much beer is produced.
    :param data: this is the file with all the information.
    :return: dictionary with the country and a number.
    """

    production: dict = {}

    for beer in data:

        months: int = list(beer.values())[-12:]

        if beer['country'] in production:
            production[beer['country']] += sum(months)

        else:
            production[beer['country']] = sum(months)

    return production

print(total_beer_production(read_dataset(path)))



def compute_mean_abv(data: list[dict]) -> Dict[str, float]:
    """
    Calculate the average alcohol percentage of the beers for each individual brewery.

    :param:data (List[Dict[str, any]]): List of dictionaries containing beer information.

    :returns: Dict[str, float]: A dictionary with brewery names as keys and average alcohol content as values.
    """

    # Dictionary to store total ABV and count of beers for each brewery
    abv_mean_dict: Dict[str, float] = {}
    beer_count_dict: Dict[str, int] = {}

    # Iterate through the list of beer dictionaries
    for beer in data:
        style_name: str = beer.get("style_name", "")
        abv: float = beer.get("abv", 0.0)

        # Update total ABV and beer count for the brewery
        if style_name in abv_mean_dict:
            abv_mean_dict[style_name] += abv
            beer_count_dict[style_name] += 1
        else:
            abv_mean_dict[style_name] = abv
            beer_count_dict[style_name] = 1

    # Calculate average ABV for each style
    for style_name, total_abv in abv_mean_dict.items():
        mean_abv: float = total_abv / beer_count_dict[style_name]
        abv_mean_dict[style_name] = mean_abv

    return abv_mean_dict




print(compute_mean_abv(read_dataset(path)))







