import pandas as pd

DATA_MOVIES = pd.read_csv('assets/movies.csv')
DATA_RATINGS = pd.read_csv('assets/ratings.csv')
DATA = pd.merge(DATA_MOVIES, DATA_RATINGS, on='movieId', how='inner')