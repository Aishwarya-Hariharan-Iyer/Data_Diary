from dash import html, Output, Input, State, callback, dash_table
from dash import dcc
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

df_movies = pd.read_csv('assets/movies.csv')
df_ratings = pd.read_csv('assets/ratings.csv')
merged_df = pd.merge(df_movies, df_ratings, on='movieId')

data_table = dash_table.DataTable(
    id='datatable',
    columns=[
        {"name": i, "id": i, "selectable": True} for i in merged_df.columns
        ],
    data=merged_df.to_dict('records'),
    page_action="native",
    page_current= 0,
    page_size= 10,
)


