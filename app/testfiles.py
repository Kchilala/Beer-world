from app.data_exploration import get_state_style_count
from app.data_loader import read_dataset


# def beer_styles_per_country(data: list[dict[str, any]]) -> dict[str,list]:
#     """
#
#     :return:
#     """
#     assert ['United States'] == 78

def test_get_state_style_count() -> dict:
    """

    :param data:
    :param state:
    :return:
    """
    path = "../assets/beer_db_v4.csv"
    data: list[dict] = read_dataset(path)
    state = 'Ohio'
    style_count_ohio = get_state_style_count(data, "Ohio")
    assert style_count_ohio == {
        'American Light Lager': 0, 'Blonde Ale': 0, 'English Barleywine': 0, 'Belgian Blond Ale': 0, 'Best Bitter': 0,
        'Old Ale': 0, 'Winter Seasonal Beer': 1, 'American-Style Stout': 3, 'English Porter': 4, 'Unclassified': 12,
        'Schwarzbier': 0, 'Belgian Tripel': 0, 'Weissbier': 1, 'Fruit Beer': 2, 'Scottish Export': 1,
        'Alternative Grain Beer': 2, 'American IPA': 3, 'American Lager': 5, 'American Brown Ale': 4,
        'Wild Specialty Beer': 0, 'Fruit Lambic': 1, 'American Pale Ale': 5, 'Saison': 1, 'American Stout': 4,
        'American Barleywine': 0, 'Oud Bruin': 0, 'Belgian Dubbel': 0, 'Belgian Golden Strong Ale': 1,
        'American Amber Ale': 4, 'Irish Red Ale': 0, 'Witbier': 1, 'Mild': 1, 'Helles Bock': 0, 'English IPA': 0,
        'Marzen': 1, 'Double IPA': 2, 'Belgian Pale Ale': 0, 'Specialty Wood-Aged Beer': 1, 'German Pils': 3,
        'Scottish Light': 0, 'Weizenbock': 1, 'Kentucky Common': 0, 'British Golden Ale': 0, 'Fruit and Spice Beer': 0,
        'Gose': 0, 'Strong Bitter': 0, 'Kolsch': 0, 'Belgian Dark Strong Ale': 0, 'Dark Belgo Ale': 0, 'Doppelbock': 0,
        'Munich Helles': 1, 'Rauchbier': 0, 'Imperial Stout': 0, 'Munich Dunkel': 0, 'Dunkles Weissbier': 0,
        'Trappist Single': 0, 'Berliner Weisse': 0, 'Cream Ale': 1, 'Pale Kellerbier': 0, 'Oatmeal Stout': 0,
        'Maibock': 0, 'Sweet Stout': 0, 'Czech Amber Lager': 0, 'London Brown Ale': 0, 'Gueuze ': 0,
        'Pre-Prohibition Lager': 0, 'Classic Style Smoked Beer': 0, 'Biere de Garde': 0, 'Czech Pale Lager': 0,
        'Australian Sparkling Ale': 0, 'Autumn Seasonal Beer': 1, 'Ordinary Bitter': 0, 'Altbier': 0,
        'Specialty IPA - Rye IPA': 0, 'Spice, Herb, or Vegetable Beer': 0, 'American Strong Ale': 0, 'Irish Stout': 0,
        'Baltic Porter': 0, 'International Dark Lager': 0, 'British Strong Ale': 0, 'Foreign Extra Stout': 0,
        'International Pale Lager': 0, 'Irish Extra Stout': 0, 'Amber Kellerbier': 0, 'Flanders Red Ale': 0,
        'Dark Mild': 0, 'Out of Category': 0, 'Vienna Lager': 0, 'Alternative Sugar Beer': 0
    }
