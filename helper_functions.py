from sqlalchemy import create_engine 
import pymysql 
import pandas as pd 

def connect_to_db(username, pwd, server, database):
    """
    Connects to database and returns connection
    """    
    sql_engine = create_engine(f'mysql+pymysql://{username}:{pwd}@{server}/{database}')
    connection = sql_engine.connect()
    return connection

def diff_of_na(df):
    before_ = len(df)
    new_df = df.dropna()
    after_ = len(new_df)
    diff = before_ - after_ 
    return print("The difference in rows is {}".format(str(diff)))

def sales_by_region(df, grouped_column, agg_col):
    try:
        df = df.groupby([grouped_column])[agg_col].sum()
        return df
    except KeyError:
        print("There was a typo")
