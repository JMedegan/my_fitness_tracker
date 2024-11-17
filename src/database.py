
import pandas as pd
import os
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from datetime import date


import pandas as pd
from typing import Any

def load_data() -> pd.DataFrame:
    """
    Load workout data from a Google Sheets connection.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the "workout_database" worksheet.
    """
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="workout_database", ttl=5)
    return df

def append_new_data(existing_data: pd.DataFrame, new_data: pd.DataFrame) -> None:
    """
    Append new data to the existing workout data and update the Google Sheets worksheet.

    Args:
        existing_data (pd.DataFrame): The existing workout data loaded from the Google Sheet.
        new_data (pd.DataFrame): The new data to append to the existing data.

    Returns:
        None: This function updates the Google Sheets worksheet in-place.
    """
    # Combine existing and new data
    df = pd.concat([existing_data, new_data], ignore_index=True)
    
    # Update Google Sheets with the new combined data
    conn = st.connection("gsheets", type=GSheetsConnection)
    conn.update(worksheet="workout_database", data=df)



def get_last_n_rows_for_exercise(exercise: str, n: int = 5) -> pd.DataFrame:
    """
    Retrieve the last `n` rows of workout data for a specific exercise, sorted by date.

    Args:
        exercise (str): The name of the exercise to filter the data for.
        n (int, optional): The number of recent rows to retrieve. Defaults to 5.

    Returns:
        pd.DataFrame: A DataFrame containing the last `n` rows of the specified exercise's
                      data, sorted by date in ascending order.
    """
    # Load the data
    df = load_data()
    
    # Filter the data for the specific exercise
    df = df[df.Exercise == exercise].reset_index(drop=True)
    
    # Group by date and calculate the mean for 'weight' and 'reps'
    df_analysis = df.groupby("Date")[['weight', 'reps']].mean()
    
    # Sort data by date in descending order and reset index
    df_analysis = df_analysis.sort_values(by="Date", ascending=False).reset_index()
    
    # Get the last `n` rows, sorted by date in ascending order
    try:
        df_analysis = df_analysis.head(n).sort_values(by="Date", ascending=True).reset_index()
    except Exception as e:
        df_analysis = df_analysis.sort_values(by="Date", ascending=True).reset_index()
    
    return df_analysis



def save_weights_reps(exercise: str, set_number: int, weight: float, reps: int) -> None:
    """
    Save the weight and repetitions for a specific exercise and set, and update the database.

    Args:
        exercise (str): The name of the exercise to log.
        set_number (int): The set number being recorded (currently unused but part of the signature for potential extension).
        weight (float): The weight used in the exercise.
        reps (int): The number of repetitions performed.

    Returns:
        None: Updates the Google Sheets database with the new data.
    """
    # Load existing data or create a new DataFrame if it doesn't exist
    existing_data = load_data()
    
    # Create a new entry with the provided data
    new_data = pd.DataFrame(
        [
            {
                "Date": date.today(),
                "Exercise": exercise,
                "weight": weight,
                "reps": reps
            }
        ]
    )
    
    # Append the new data to the existing data and update the database
    append_new_data(existing_data, new_data)


