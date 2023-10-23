from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from data_card import data_table
from eda_preprocessor import summary_table, box_plot, distribution_plot

app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

app.layout = html.Div([
    html.H1("Recommendation System"),
    html.Div([
        data_table,
        summary_table,
        distribution_plot,
        box_plot]
    )
])


if __name__ == '__main__':
    app.run(debug=True)