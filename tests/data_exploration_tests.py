"""
JBI010: Assignment 2
Authors: Chiara Liotta

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

from app.data_exploration import *
import pytest
from app_data_exploration


# Fixture to provide the CSV file path for testing

@pytest.fixture():

    # Test to check if the function returns a list of dictionaries
def test_count_states_returns_list_of_dicts(csv_file_path, column_name):
    state_counts = count_states_in_csv(csv_file_path, column_name)
    assert isinstance(state_counts, list)
    assert all(isinstance(item, dict) for item in state_counts)

# Test to check if the function counts states correctly
def test_count_states_counts_correctly(csv_file_path, column_name):
    state_counts = count_states_in_csv(csv_file_path, column_name)
    # You can modify the expected_result based on the content of your CSV file
    expected_result = [{"state": "California", "count": 3}, {"state": "New York", "count": 2}]
    assert state_counts == expected_result
