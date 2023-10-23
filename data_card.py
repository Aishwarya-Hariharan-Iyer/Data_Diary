from dash import html, Output, Input, State, callback, dash_table
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
from constants import DATA

data_table = dash_table.DataTable(
    id='datatable',
    columns=[
        {"name": i, "id": i, "selectable": True} for i in DATA.columns
        ],
    data=DATA.to_dict('records'),
    page_action="native",
    page_current= 0,
    page_size= 10,
)


