"""
JBI010: Assignment 2
Authors: Chiara Liotta, Gijs Walravens

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""
import data_loader
import dashboard

# Press the green button in the gutter to run the script.
from app import data_exploration

if __name__ == '__main__':
    # Load in the data and prep it
    data = data_loader.read_dataset("../assets/beer_db_v4.csv")

    # Run Dashboard? (set to True to run Dash, set to False for console printing)
    # Leave this on false until you are done with the data prep and EDA exercises!
    dash_mode: bool = False

    if dash_mode:
        my_dashboard = dashboard.create_dashboard(data)
        my_dashboard.run_server(debug=False)
    else:

        data_exploration.explore(data)
