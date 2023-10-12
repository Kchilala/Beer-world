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
path = "../assets/beer_db_v4.csv"
def get_state_style_count(dataset, state: str)-> dict:
    """
    This function returns each styles of beer state produces, and how many beers of each style.
    :param dataset:given the data (as returned by the read dataset function) and a state.
    :return:returns a dictionary where each style name is a key with the count as its value.
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
def get_breweries_from_style(dataset: List[Dict[str, any]], beerstyle: str) -> List[Dict[str, any]]:
    """
    This function gives information about breweries that have beers with style containing the given substring.
    :param dataset:given the data (as returned by the read dataset function) and a state.
    :param beerstyle: this parameter is a string of the beerstyle.
    :returns: a list of dictionaries with information about breweries that have beers with style containing the given substring.

    """


    lower_beerstyle: str = beerstyle.lower()

    # List to store filtered beer information
    filtered_beers: list[Dict[str, any]] = []

    # Iterate through the dataset
    for value in dataset:
        # Split style_name into words and check if lower_beerstyle is in the words
        if lower_beerstyle in [word.lower() for word in value['style_name'].split()]:
            # Keys to be removed from the dictionary
            remove_keys: list[str] = ['January_22', 'February_22', 'March_22', 'April_22', 'May_22',
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
from typing import List, Dict

def compute_mean_abv(data: List[Dict[str, any]]) -> Dict[str, float]:
    """
    Calculate the average alcohol percentage of the beers for each individual brewery.

    :param:data (List[Dict[str, any]]): List of dictionaries containing beer information.

    :return: Dict[str, float]: A dictionary with brewery names as keys and average alcohol content as values.
    """

    # Dictionary to store total ABV and count of beers for each brewery
    abv_mean_dict: Dict[str, float] = {}
    beer_count_dict: Dict[str, int] = {}

    # Iterate through the list of beer dictionaries
    for beer in data:
        brewery_name: str = beer.get("brewery_name", "")
        abv: float = beer.get("abv", 0.0)

        # Update total ABV and beer count for the brewery
        if brewery_name in abv_mean_dict:
            abv_mean_dict[brewery_name] += abv
            beer_count_dict[brewery_name] += 1
        else:
            abv_mean_dict[brewery_name] = abv
            beer_count_dict[brewery_name] = 1

    # Calculate average ABV for each brewery
    for brewery_name, total_abv in abv_mean_dict.items():
        mean_abv: float = total_abv / beer_count_dict[brewery_name]
        abv_mean_dict[brewery_name] = mean_abv

    return abv_mean_dict

# // END_TODO [task_3C1]


# // BEGIN_TODO [task_3c2] Retrieve the breweries from a specific state.
from typing import List, Dict

def get_breweries_from_state(data: List[Dict[str, str]], state: str) -> List[Dict[str, str]]:
    """
    Filters a list of dictionaries containing brewery information based on the specified state.

    :param:data (List[Dict[str, str]]): List of dictionaries with brewery information.
        state (str): The state to filter breweries by.

    :returns: List[Dict[str, str]]: List of filtered dictionaries containing brewery information.

    """

    # List to store filtered brewery information
    filtered_breweries: List[Dict[str, str]] = []

    # Keys to be removed from each dictionary
    keys_to_remove: List[str] = ['January_22', 'February_22', 'March_22', 'April_22', 'May_22',
                                 'June_22', 'July_22', 'August_22', 'September_22', 'October_22',
                                 'November_22', 'December_22']

    # Iterate through the brewery information data
    for brewery_info in data:
        # Check if the brewery is located in the specified state
        if brewery_info['state'] == state:
            # Create a new dictionary excluding the specified keys
            filtered_dict: Dict[str, str] = {key: value for key, value in brewery_info.items() if key not in keys_to_remove}
            # Append the filtered dictionary to the list of filtered breweries
            filtered_breweries.append(filtered_dict)

    # Return the list of filtered breweries
    return filtered_breweries

# // END_TODO [task_3c2]


# // BEGIN_TODO [task_3c3] Retrieve the beers produced by a specific brewery.
from typing import List, Dict

def get_beers_from_brewery(data: List[Dict[str, any]], brewery_id: int) -> List[Dict[str, any]]:
    """
    Get a list of dictionaries containing beers belonging to the specified brewery.

    :param:data (List[Dict[str, any]]): List of dictionaries containing beer data.
        brewery_id (int): ID of the brewery to filter beers.

    :returns:List[Dict[str, any]]: List of dictionaries containing beers from the specified brewery.
    """
    beer_list: list[Dict[str, any]] = []

    # Iterate through the data and filter beers based on brewery ID
    for row in data:
        if row['brewery_id'] == brewery_id:
            # Create a dictionary containing all keys and values from the row
            beer_dict: Dict[str, any] = {key: value for key, value in row.items()}
            # Add the beer dictionary to the beer list
            beer_list.append(beer_dict)

    return beer_list

# // END_TODO [task_3c3]


# // BEGIN_TODO [task_3c4] Retrieve the breweries in state, calculate mean ABV of their beers, and add as new key
def add_mean_abv_state_breweries(data: List[Dict[str, any]], breweries: List[Dict[str, any]], state: str) -> List[Dict[str, any]]:
    """
    Add mean ABV (Alcohol by Volume) field to each brewery dictionary for the given state.

    :param:data (List[Dict[str, Any]]): List of dictionaries containing beer data.
    :param:breweries (List[Dict[str, Any]]): List of dictionaries containing breweries data.
    :param:state (str): State for which mean ABV needs to be calculated and added.

    :returns:List[Dict[str, Any]]: List of dictionaries containing breweries with mean ABV field.
    """
    # Get beers from the specified state
    state_beers = [beer for brewery in breweries if brewery['state'] == state
                   for beer in get_beers_from_brewery(data, brewery['id'])]

    # Calculate mean ABV for the state's beers
    mean_abv = sum(beer['abv'] for beer in state_beers) / len(state_beers) if state_beers else 0

    # Add mean ABV field to each brewery in the specified state
    for brewery in breweries:
        if brewery['state'] == state:
            brewery['mean_abv'] = mean_abv

    return breweries
# // END_TODO [task_3c4]
