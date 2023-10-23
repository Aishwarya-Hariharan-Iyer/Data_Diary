from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from data_card import data_table


app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

app.layout = html.Div([
    html.H1("Recommendation System"),
    html.Div(
        data_table
    )
])


if __name__ == '__main__':
    app.run(debug=True)