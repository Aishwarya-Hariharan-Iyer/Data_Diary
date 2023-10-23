from dash import html, Output, Input, State, callback, dash_table
from dash import dcc
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from constants import DATA

# Explore Data
gen_desc = DATA.describe()

summary_table = dash_table.DataTable(
    id='datatable-summary',
    columns=[
        {"name": i, "id": i, "selectable": True} for i in gen_desc.columns
        ],
    data=gen_desc.to_dict('records'),
    page_action="native",
    page_current= 0,
    page_size= 10,
)

html.Div(id="report-summary", children=[
    html.H5("Summary Of Data"),
    summary_table
])


# Generate Visualisations



# Data Preprocessing
