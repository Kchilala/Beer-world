"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

from app.data_loader import *
import pytest

# Define the test data path
@pytest.fixture
def data_path():
    return "../assets/beer_db_v4.csv"

