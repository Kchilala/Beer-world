"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
from typing import List, Dict


# // BEGIN_TODO [task_2] Loading and preparing the dataset
path = "../assets/beer_db_v4.csv"
def read_dataset(path: str) -> list[dict]:
    """
    this function opens the file name and reads the csv file
    and returns a list of dictionaries.

    :parameter: this is a string of the path of the file
    :returns: it returns a list of dictionaries

    """
    # create an empty list to store dictionary
    data_csv: list = []
    months: list = [
                    'January_22', 'February_22', 'March_22', 'April_22', 'May_22', 'June_22', 'July_22', 'August_22',
                    'September_22', 'October_22', 'November_22', 'December_22'
    ]
    # this code opens the csv file and read each row
    with open(path, 'r', encoding= 'utf-8') as file:
        data = csv.DictReader(file)

        for row in data:
            # this code creates a new key
            new_key_dict = {key.replace('styleId', 'style_id'): value for key, value in row.items()}
            # this code does the same as above
            new_key_dicto = {key.replace('code', 'postal_code'): value for key, value in new_key_dict.items()}
            for key, value in new_key_dicto.items():
                # this code below changes the value from strings to integers
                if key == 'cat_id' or key == 'brewery_id' or key == 'beer_id':
                    new_key_dicto[key] = int(value)
                # this code converts a string to a float
                if key == 'abv':
                    new_key_dicto[key] = float(value)
                if key in months:
                    new_key_dicto[key] = float(value)

            data_csv.append(new_key_dicto)

    return data_csv


print(read_dataset(path))


# // END_TODO [task_2]
