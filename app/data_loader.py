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
    data = []

    #this code allows us to read each row in the csv file
    with open(path, 'r') as file:
        data = csv.reader(file)
        for row in data:
            print(row)
# // END_TODO [task_2]
