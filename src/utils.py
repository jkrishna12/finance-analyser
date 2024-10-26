# import streamlit as st
import pandas as pd

def json_to_df(response_json):
    """
    Turns response json to pandas dataframe and sorts the dataframe in ascending order of date
    """

    return pd.json_normalize(response_json).sort_values("date", ascending=True).reset_index(drop = True)

def transpose_df(df):
    """
    Function takes in a pandas dataframe and returns a transposed dataframe with calendar year set as column names
    Parameters:
        df: Pandas Dataframe
    Returns:
        df_T: Pandas dataframe
    """
    df = df.sort_values("date", ascending=True).reset_index(drop = True)

    year = df['calendarYear'].to_list()

    df_T = df.T

    df_T.columns = year

    return df_T