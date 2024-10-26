def transpose_df(df):
    """
    Function takes in a pandas dataframe and returns a transposed dataframe with calendar year set as column names
    Parameters:
        df: Pandas Dataframe
    Returns:
        df_T: Pandas dataframe
    """
    year = df['calendarYear'].to_list()

    df_T = df.T

    df_T.columns = year

    return df_T