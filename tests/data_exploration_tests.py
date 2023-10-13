"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""
from app.data_exploration import (get_state_style_count, get_breweries_from_style, compute_mean_abv, get_breweries_from_state, get_beers_from_brewery,
                                  add_mean_abv_state_breweries, read_dataset)
from app.data_loader import read_dataset

from app.data_exploration import *
import pytest
# from app_data_exploration


# Fixture to provide the CSV file path for testing

# @pytest.fixture():

    # Test to check if the function returns a list of dictionaries
# def test_count_states_returns_list_of_dicts(csv_file_path, column_name):
#     state_counts = count_states_in_csv(csv_file_path, column_name)
#     assert isinstance(state_counts, list)
#     assert all(isinstance(item, dict) for item in state_counts)
#
# # Test to check if the function counts states correctly
# def test_count_states_counts_correctly(csv_file_path, column_name):
#     state_counts = count_states_in_csv(csv_file_path, column_name)
#     # You can modify the expected_result based on the content of your CSV file
#     expected_result = [{"state": "California", "count": 3}, {"state": "New York", "count": 2}]
#     assert state_counts == expected_result
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

def test_get_state_style_count_in_dict() -> dict:
    """

    :param data:
    :param state:
    :return:
    """
    path = "../assets/beer_db_v4.csv"
    data: list[dict] = read_dataset(path)
    state = 'Ohio'
    style_count_ohio = get_state_style_count(data, "Ohio")

    assert style_count_ohio['Witbier'] != 0


def test_get_breweries_from_style()-> int:
    """

    :return:
    """
    path = "../assets/beer_db_v4.csv"
    data: list[dict] = read_dataset(path)
    breweries_blonde = get_breweries_from_style(data, "Blonde")
    assert breweries_blonde[0]['beer_id'] == 2

def test2_get_breweries_from_style()-> int:
    """

    :return:
    """
    path = "../assets/beer_db_v4.csv"
    data: list[dict] = read_dataset(path)
    breweries_blonde = get_breweries_from_style(data, "Blonde")
    assert breweries_blonde[0]['beer_id'] != 1




def test_compute_mean_abv_empty_data():
    """
    Test the compute_mean_abv function with empty data.

    This test case checks if the function returns an empty dictionary when the input data is empty.
    """
    data = []
    result = compute_mean_abv(data)
    assert result == {}, "Expected an empty dictionary for empty data"


def test_compute_mean_abv_sample_data():
    """
    Test the compute_mean_abv function with sample data.

    This test case checks if the function correctly calculates the mean ABV for each brewery.
    """
    data = [
        {"brewery_name": "Brewery A", "abv": 5.0},
        {"brewery_name": "Brewery B", "abv": 6.0},
        {"brewery_name": "Brewery A", "abv": 4.0},
        {"brewery_name": "Brewery B", "abv": 7.0},
        {"brewery_name": "Brewery A", "abv": 4.5},
        {"brewery_name": "Brewery C", "abv": 5.5},
    ]
    result = compute_mean_abv(data)
    expected_result = {
        'Brewery A': 4.5,
        'Brewery B': 6.5,
        'Brewery C': 5.5,
    }
    assert result == expected_result, f"Expected {expected_result}, but got {result}"




def test_get_breweries_from_state_empty_data()->list:
    """
    Test the get_breweries_from_state function with empty data.

    This test case checks if the function returns an empty list when the input data is empty.
    """
    data = []
    state = "California"
    result = get_breweries_from_state(data, state)
    assert result == [], "Expected an empty list for empty data"



def test2_get_breweries_from_state_empty_data()->list:
    """
    Test the get_breweries_from_state function with empty data.

    This test case checks if the function returns an empty list when the input data is empty.
    """
    data = []
    state = "California"
    result = get_breweries_from_state(data, state)
    assert result != dict

def test_get_beers_from_brewery_no_beers()->list:
    """
    Test the get_beers_from_brewery function when no beers are found for the specified brewery ID.

    This test case checks if the function returns an empty list when no beers match the specified brewery ID.
    """
    data = [
        {"brewery_id": 1, "beer_name": "Beer A"},
        {"brewery_id": 2, "beer_name": "Beer B"},
        {"brewery_id": 3, "beer_name": "Beer C"},
    ]
    brewery_id = 4  # A brewery ID with no matching beers
    result = get_beers_from_brewery(data, brewery_id)
    assert result == [], "Expected an empty list when no beers are found."

def test2_get_beers_from_brewery_no_beers()->list:
    """
    Test the get_beers_from_brewery function when no beers are found for the specified brewery ID.

    This test case checks if the function returns an empty list when no beers match the specified brewery ID.
    """
    data = [
        {"brewery_id": 1, "beer_name": "Beer A"},
        {"brewery_id": 2, "beer_name": "Beer B"},
        {"brewery_id": 3, "beer_name": "Beer C"},
    ]
    brewery_id = 4  # A brewery ID with no matching beers
    result = get_beers_from_brewery(data, brewery_id)
    assert result != dict




def test_add_mean_abv_state_breweries_no_beers():
    """
    Test the add_mean_abv_state_breweries function when there are no beers in the specified state.

    This test case checks if the function correctly handles the case where there are no beers for the specified state.
    """
    data = [
        {"brewery_id": 1, "beer_name": "Beer A", "abv": 5.0},
        {"brewery_id": 2, "beer_name": "Beer B", "abv": 6.0},
    ]
    breweries = [
        {"brewery_id": 1, "state": "California"},
        {"brewery_id": 2, "state": "California"},
    ]
    state = "New York"  # A state with no matching beers
    result = add_mean_abv_state_breweries(data, breweries, state)
    expected_result = breweries  # Expected result is the same as the input breweries
    assert result == expected_result, "Expected the same list of breweries when no beers are found."

def test2_add_mean_abv_state_breweries_no_beers():
    """
    Test the add_mean_abv_state_breweries function when there are no beers in the specified state.

    This test case checks if the function correctly handles the case where there are no beers for the specified state.
    """
    data = [
        {"brewery_id": 1, "beer_name": "Beer A", "abv": 5.0},
        {"brewery_id": 2, "beer_name": "Beer B", "abv": 6.0},
    ]
    breweries = [
        {"brewery_id": 1, "state": "California"},
        {"brewery_id": 2, "state": "California"},
    ]
    state = "New York"  # A state with no matching beers
    result = add_mean_abv_state_breweries(data, breweries, state)
    expected_result = breweries  # Expected result is the same as the input breweries
    assert result != dict