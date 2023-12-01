import pandas as pd
from sqlalchemy import create_engine

def load_data(dataframe, database_url, table_name):
    """ Load data into a SQL database """
    engine = create_engine(database_url)
    dataframe.to
