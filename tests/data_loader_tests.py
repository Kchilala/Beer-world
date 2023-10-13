"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

from app.data_loader import *
import pytest

# Define the test data path
# @pytest.fixture
# def data_path():
#     return "../assets/beer_db_v4.csv"

def test_read_data_set() :
    """
    pytest read_dataset(path)

    """

    path = "../assets/beer_db_v4.csv"
    data: list[dict] = read_dataset(path)
    assert type(data[0]) == dict


def test2_read_data_set() :
    """
    pytest read_read_dataset(path)

    """

    path = "../assets/beer_db_v4.csv"
    data: list[dict] = read_dataset(path)
    assert data[0] in data
