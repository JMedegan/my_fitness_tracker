
import pandas as pd
import os

def save_to_csv(data, filename):
    '''Save a DataFrame to a CSV file.'''
    data.to_csv(filename, index=False)

def load_from_csv(filename):
    '''Load data from a CSV file into a DataFrame.'''
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame()

def append_to_csv(data, filename, column_name):
    '''Append data to a specific column in a CSV file.'''
    df = load_from_csv(filename)
    df.loc[len(df), column_name] = data
    save_to_csv(df, filename)

    
def get_last_n_rows_for_exercise(exercise, n, filename):
    '''Get the last n non-empty rows for a specific exercise from CSV file.'''
    df = load_from_csv(filename)
    
    # Check if exercise exists in the dataframe
    if exercise in df.columns:
        # Drop NA values for the specific column and then get the last n values
        non_empty_values = df[exercise].dropna()
        return non_empty_values.tail(n).tolist()
    
    return []

