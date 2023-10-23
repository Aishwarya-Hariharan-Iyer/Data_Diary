from dash import html, Output, Input, State, callback, dash_table
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from constants import DATA

# Explore Data
DATA['genres'] = DATA['genres'].str.split('|')
data_explode = DATA.explode('genres')
gen_desc = data_explode.describe()

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
fig_h = px.histogram(data_explode, x='genres')
distribution_plot = dcc.Graph(id='hist-plot', figure=fig_h)

fig_b = px.box(data_explode, x='genres', y='rating')
box_plot = dcc.Graph(id='box-plot', figure=fig_b)


