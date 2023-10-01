"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
from typing import List, Dict


# // BEGIN_TODO [task_2] Loading and preparing the dataset
path = "/Users/kecichilala/PycharmProjects/h11-assignment-2-template/assets/beer_db_v4.csv"
def read_dataset(path: str) -> list[dict]:
    """
    this function opens the file name and reads the csv file
    and returns a list of dictionary's.

    :parameter: this is a string of the path of the file
    :returns: it returns a list of dictionaries

    """
    #create an empty list to store dictionary
    data_csv: list = []

    #this code opens the csv file and read each row
    with open(path, 'r', encoding= 'utf-8') as file:
        data = csv.DictReader(file)

        for row in data:
            # this code creates a new key
            new_key_dict = {key.replace('styleId', 'style_id'): value for key, value in row.items()}
            # this code does the same as above
            new_key_dicto = {key.replace('code', 'postal_code'): value for key, value in new_key_dict.items()}
            data_csv.append(new_key_dicto)

    return data_csv


print(read_dataset(path))


# // END_TODO [task_2]
