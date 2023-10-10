"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import List, Dict
import csv
import pytest


def explore(data: List[Dict[str, any]]) -> None:
    """
    Performs EDA on the passed data.
    :param data: the data that will be used in the EDA
    """

    style_count_ohio = get_state_style_count(data, "Ohio")

    print(f"\033[1mStyle count of beers produced in Ohio: \033[0m")

    for key, value in style_count_ohio.items():
        print(f"{key}: {value}")

    breweries_blonde = get_breweries_from_style(data, "Blonde")

    print("\n\033[1mBreweries in California with blonde ales, and their mean abv:\033[0m")

    abv_cal_breweries = add_mean_abv_state_breweries(data, breweries_blonde, "California")

    for brewery in abv_cal_breweries:
        name = brewery.get("brewery_name")
        abv = brewery.get("mean_abv")
        print(f"{name}: {abv}")


# // BEGIN_TODO [task_3a] count of beer styles produced in the given state
# Create the function get state style count
from app.data_loader import read_dataset
path = "/Users/kecichilala/PycharmProjects/h11-assignment-2-template/assets/beer_db_v4.csv"
def get_state_style_count(dataset, state: str)-> dict:
    """
    This function returns each styles of beer state produces, and how many beers of each style
    :param dataset:given the data (as returned by the read dataset function) and a state
    :return:returns a dictionary where each style name is a key with the count as its value
    """
    # Initialize an empty dictionary to store beer style counts
    style_counts = {}
    # Iterate through the dataset
    for row in dataset:
        if row['state'] == state:
            # Check if the current row's state matches the specified state
            if row["style_name"] not in style_counts:
                style_counts[row["style_name"]] = 1
            # If the style is not in the dictionary, add it with a count of 1
            # If the style is already in the dictionary, increment its count by 1
            elif row["style_name"] in style_counts:
                style_counts[row["style_name"]] += 1
        # If the row's state doesn't match the specified state, ensure the style is in the dictionary
        # If it's not, add it with a count of 0
        if row["style_name"] not in style_counts:
            style_counts[row["style_name"]] = 0

    return style_counts


# // END_TODO [task_3a]


# // BEGIN_TODO [task_3b] Retrieve the breweries producing beers of a specific style
def get_breweries_from_style(dataset: List[Dict[str, Any]], beerstyle: str) -> List[Dict[str, Any]]:
    """
    This function gives information about breweries that have beers with style containing the given substring.
    :param dataset:given the data (as returned by the read dataset function) and a state
    :param beerstyle: this parameter is a string of the beerstyle
    :returns: a list of dictionaries with information about breweries that have beers with style containing the given substring

    """


    lower_beerstyle: str = beerstyle.lower()

    # List to store filtered beer information
    filtered_beers: List[Dict[str, Any]] = []

    # Iterate through the dataset
    for value in dataset:
        # Split style_name into words and check if lower_beerstyle is in the words
        if lower_beerstyle in [word.lower() for word in value['style_name'].split()]:
            # Keys to be removed from the dictionary
            remove_keys: List[str] = ['January_22', 'February_22', 'March_22', 'April_22', 'May_22',
                                  'June_22', 'July_22', 'August_22', 'September_22', 'October_22',
                                  'November_22', 'December_22']

            # Create a new dictionary without specified keys
            new_dict: Dict[str, Any] = {key: v for key, v in value.items() if key not in remove_keys}

            # Check if the new dictionary is not already in filtered_beers list
            if new_dict not in filtered_beers:
                filtered_beers.append(new_dict)
    return filtered_beers
# // END_TODO [task_3b]



# // BEGIN_TODO [task_3c1] Compute the mean abv of the beers in the list of dictionaries
#def compute_mean_abv(list[dict])->float:
"""
This function calculate the average alcohol percentage of the beers for each individual brewery. 
"""
# // END_TODO [task_3C1]


# // BEGIN_TODO [task_3c2] Retrieve the breweries from a specific state.
#def get_breweries_from_state(list[dict])->list[dict]:
# // END_TODO [task_3c2]


# // BEGIN_TODO [task_3c3] Retrieve the beers produced by a specific brewery.
#def get_beers_from_brewery(data)->list[dict]:
# // END_TODO [task_3c3]


# // BEGIN_TODO [task_3c4] Retrieve the breweries in state, calculate mean ABV of their beers, and add as new key
#def add_mean_abv_state_breweries(data)
# // END_TODO [task_3c4]
