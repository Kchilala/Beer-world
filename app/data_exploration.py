"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

from typing import List, Dict


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
def get_state_style_count(data, state: str)-> dict:
    """
    this function returns each styles of beer state produces, and how many beers of each style
    :param:given the data (as returned by the read dataset function) and a state
    :return:returns a dictionary where each style name is a key with the count as its value
    """

# // END_TODO [task_3a]


# // BEGIN_TODO [task_3b] Retrieve the breweries producing beers of a specific style
# // END_TODO [task_3b]


# // BEGIN_TODO [task_3c1] Compute the mean abv of the beers in the list of dictionaries
# // END_TODO [task_3C1]


# // BEGIN_TODO [task_3c2] Retrieve the breweries from a specific state.
# // END_TODO [task_3c2]


# // BEGIN_TODO [task_3c3] Retrieve the beers produced by a specific brewery.
# // END_TODO [task_3c3]


# // BEGIN_TODO [task_3c4] Retrieve the breweries in state, calculate mean ABV of their beers, and add as new key
# // END_TODO [task_3c4]
