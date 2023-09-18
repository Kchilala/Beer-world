"""
JBI010: Assignment 2
Authors: Chiara Liotta, Gijs Walravens

Copyright (c) 2023 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import dash
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs
import plotly.graph_objs as go
from typing import List, Dict
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Row


def create_dashboard(data: List[Dict[str, any]]) -> Dash:
    """
    Initializes the dashboard with layout, content and interactivity.
    :param data: the prepped data loaded from the CSVs
    :return: dashboard object that is ready to deploy.
    """
    # Turn the data into a DF
    data = pd.DataFrame(data)

    # Set some options for clearer printing
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    # Create Dash app object with correct path and styling
    app = dash.Dash(__name__
                    , assets_folder="../assets"
                    , external_stylesheets=
                    [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

    # Retrieve all item names for the dropdown
    all_names = np.sort(data["country"].unique())

    # region Layout
    app.layout = html.Div([
        # Navigation bar on top of the page
        dbc.Navbar(
            dbc.Container([
                dbc.Row([
                    # Navbar logo
                    dbc.Col(
                        html.Img(src=app.get_asset_url("beer-graphic.jpg"), height="30px")
                    ),
                    # Navbar text
                    dbc.Col(
                        dbc.NavbarBrand("Beer Production By Country", className="ms-2", style={"color": "white",
                                                                                               'fontSize': '25px'})
                    )
                ], align="center", className="g-0")
            ]), color="dark", style={"margin": "0px 0px 20px 0px"}
        ),
        # Main body
        dbc.Container([
            # Item selection card
            dbc.Card([
                dbc.Row([
                    # Thumbnail image
                    dbc.Col(
                        html.Img(src=app.get_asset_url("flag-globe.jpg"), height="50px", id="thumbnail"), width=1),
                    # Dropdown
                    dbc.Col(
                        dcc.Dropdown(
                            id="item-select",
                            options=[{"label": i, "value": i} for i in all_names],
                            value=all_names[0]
                        ), width=11
                    )
                ], align="center"),

            ], body=True, style={'margin': '0px 0px 12px 0px'}),
            # Holder for analysis graphs
            html.Div([
                dbc.Row([
                    dbc.Col(
                        # Line graph card
                        [dbc.Card([
                            html.H4("Beer Category Count", className="display-6",
                                        style={'textAlign': 'center', 'fontSize': '25px'}),
                            dcc.Graph(
                                id="bar-chart"
                            )], body=True
                        )
                        ], width=7
                    ),
                    dbc.Col([
                        # Styles
                        dbc.Card([
                            dbc.Col([
                                html.H4("Category:",
                                        style={'textAlign': 'left', 'marginBottom': '25px', 'fontWeight': 'normal',
                                               'fontSize': "20px"}),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id="item-select-cat",
                                        options=[{"label": i, "value": i} for i in []],
                                    ), id="cat-dropdown", style={"margin": "10px 0px 20px 0px"}
                                ),
                                html.H4("Mean alcohol content by style", className="display-6",
                                        style={'textAlign': 'center', 'marginBottom': '25px', 'fontSize': '25px'}),
                                dbc.Row([
                                    dbc.Col(html.P("Style", style={'textAlign': 'center', 'marginBottom': '25px',
                                                                   'fontWeight': 'bold', 'fontSize': "15px"})),
                                    dbc.Col(html.P("Mean ABV", style={'textAlign': 'center', 'marginBottom': '25px',
                                                                      'fontWeight': 'bold', 'fontSize': "15px"}))
                                ], style={"margin": "30px 0px 0px 0px"}),
                                dbc.Row([
                                ], id="styles-list", style={"margin": "10px 0px 20px 0px"})
                            ]),
                        ], body=True, style={'margin': '0px 0px 20px 0px'}),

                    ])]
                ), dbc.Card(dbc.Col([
                    html.P("Category with highest median alcohol percentage:", className="display-6",
                           style={'textAlign': 'center', 'marginTop': '25px', 'fontSize': '25px'}),
                    html.P("Unknown", id="cat-median-abv", className="display-7",
                           style={'textAlign': 'center'})
                ]), style={'margin': '15px 0px 20px 0px'})
            ])
        ]),
        # Data storage
        dcc.Store(id="item-data"),
        dcc.Store(id="item-data-cat")
    ])

    # endregion

    # region Functionalities
    # region Storing and loading selected item's data in browser session
    @app.callback(
        Output("item-data", "data"),
        Input("item-select", "value")
    )
    def store_item_value(input_val: str) -> str:
        """
        Callback to retrieve the data of the selected item and store it for
        later usage.
        :param input_val: the data from the item selection dropdown
        :return: the data of the currently selected item serialized to JSON.
        """
        # Retrieve the data for the selected item
        if input_val is not None:
            item_data = data.loc[data["country"] == input_val]
        else:
            item_data = data
        # Store it in the browser for later use
        return item_data.to_json(orient="split")

    # region Functionalities
    # region Storing and loading selected item's data in browser session
    @app.callback(
        Output("item-data-cat", "data"),
        Input("item-data", "data"),
        Input("item-select-cat", "value")
    )
    def store_item_value_cat(stored_data: str, input_val: str) -> str:
        """
        Callback to retrieve the data of the selected item and store it for
        later usage.
        :param stored_data:
        :param input_val: the data from the item country selection dropdown
        :return: the data of the currently selected item serialized to JSON.
        """
        item_data_cat = read_item_value(stored_data)

        # Retrieve the data for the selected item
        if input_val is not None:
            item_data_cat = item_data_cat.loc[item_data_cat["cat_name"] == input_val]

        # Store it in the browser for later use
        return item_data_cat.to_json(orient="split")

    def read_item_value(stored_data: str) -> pd.DataFrame:
        """
        Loads the serialized JSON data of the selected item from the user's
        browser and turns it back into a DataFrame.
        :param stored_data: the JSON data of the item
        :return: the data of the selected item in the form of a DataFrame.
        """
        # First check if the data is actually stored
        if stored_data is None:
            # If not, then prevent Dash from doing an update
            return dash.no_update

        # Retrieve data that belongs to the selected item
        item_data = pd.read_json(stored_data, orient="split")

        return item_data

    # endregion
    # region Update the line graph
    @app.callback(
        Output("bar-chart", "figure"),
        Input("item-data", "data")
    )
    def update_bar_chart(stored_data: str) -> plotly.graph_objs.Figure:
        """
        Callback to update the bar chart to the data of the currently selected
        item.
        :param stored_data: data of the currently selected item in the dropdown
        :return: a new Plotly bar chart for the currently selected item.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data)

        item_data = item_data[item_data['cat_name'] != ""]

        # Define the figure
        fig = go.Figure()

        # // BEGIN_TODO [task_5a] Adding a bar chart

        # // END_TODO [task_5a]

        return fig

    # endregion
    # region Update the bar chart
    @app.callback(
        Output("cat-median-abv", "children"),
        Input("item-data", "data")
    )
    def update_cat_median_abv(stored_data: str) -> plotly.graph_objs.Figure:
        """
        Callback to update the bar chart to the data of the currently selected

        item.
        :param stored_data: data of the currently selected item in the dropdown
        :return: name of the beer category with highest median alcohol percentage.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data)

        item_data = item_data[item_data['cat_name'] != ""]
        cat_median_abv = item_data.groupby('cat_name')['abv'].median()

        # dictionary with category names as keys and median abv as value
        cat_median_abv_dict = cat_median_abv.to_dict()

        max_value_key = "unknown"

        # // BEGIN_TODO [task_5b] Adding beer category with highest median abv


        # // END_TODO [task_5b]

        return max_value_key

    @app.callback(
        Output("cat-dropdown", "children"),
        Input("item-data", "data")
    )
    def update_cat_dropdown(stored_data: str) -> dbc.Col:
        """
        Callback to update the style list to the data of the currently selected
        item.
        :param stored_data: data of the currently selected item in the dropdown
        :return: a list of elements with style name and corresponding mean alcohol percentage.
        """

        # Retrieve the stored item data
        item_data = read_item_value(stored_data)
        item_data = item_data[item_data['cat_name'] != ""]

        all_cats = item_data["cat_name"].unique()

        dropdown = dbc.Col(
            dcc.Dropdown(
                id="item-select-cat",
                options=[{"label": i, "value": i} for i in all_cats],
                value=all_cats[0]
            ), style={"margin": "10px 0px 20px 0px"}
        )

        return dropdown

    # endregion
    # region Update the style list
    @app.callback(
        Output("styles-list", "children"),
        Input("item-data-cat", "data")
    )
    def update_style_list(stored_data_cat: str) -> list[Row]:
        """
        Callback to update the style list to the data of the currently selected
        item.
        :param stored_data_cat: data of the currently selected item in the dropdown
        :return: a list of elements with style name and corresponding mean alcohol percentage.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data_cat)
        item_data = item_data[item_data['style_name'] != ""]
        styles_mean_abv = item_data.groupby('style_name')['abv'].mean()

        elements = []

        for style, value in styles_mean_abv.items():
            row = dbc.Row([
                dbc.Col(html.P(style, className="display-7",
                               style={'textAlign': 'center'})),
                dbc.Col(html.P("{:0.2f}".format(value), className="display-7",
                               style={'textAlign': 'center'}))
            ])
            elements.append(row)

        return elements

    return app
