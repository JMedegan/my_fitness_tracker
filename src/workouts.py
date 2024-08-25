import streamlit as st
import os
import pandas as pd
import os.path
from database import load_from_csv, save_to_csv
from database import get_last_n_rows_for_exercise

import time

# Styles
BUTTON_STYLE = {
    "font-size": "16px",
    "text-align": "center",
    "background-color": "#68a0cf",
    "border": "none",
    "color": "white",
    "padding": "10px 15px",
    "text-decoration": "none",
    "display": "inline-block",
    "margin": "4px 2px",
    "cursor": "pointer",
    "border-radius": "16px",
    "font-weight": "bold"
}

def countdown_timer():
    """Function to provide a countdown timer for the rest period."""
    for _ in range(60): 
        time.sleep(1)
    st.success("Time's up! Get ready for your next set!")


def freakmode_day1():
    st.title("Chest/Shoulders/Triceps")
    
    exercises = [
        ("Warm Up Bench Press", 2, 10, 1),
        ("Bench Press", 5, 8, 1),
        ("Dumbbell Chest Fly", 3, 8, 1),
        ("Incline Dumbbell Chest Fly", 2, 10, 1),
        ("Seated Dumbbell Shoulder Press", 4, 8, 1),
        ("Dumbbell Front Raise", 3, 7, 0),
        ("Dumbbell Lateral Raise", 3, 7, 0),
        ("Seated Rear Delt Fly", 3, 7, 1),
        ("Cable Straight Bar Pushdown", 3, 8, 1),
        ("Double Arm Triceps Kick-Back", 3, 8, 1)
        
    ]
    

    date = st.date_input("Jour 1")
    
    for exercise, default_sets, reps, rest in exercises:
        display_name = exercise

        with st.expander(display_name, expanded=False):
            st.header(exercise)
            
            # Load and display previous session data for the exercise
            weights = get_last_n_rows_for_exercise(exercise, default_sets, '\data\weight_tracking_data.csv')
            reps_data = get_last_n_rows_for_exercise(exercise, default_sets, '\data\reps_tracking_data.csv')
            
            st.write("Poids précédents:", weights)
            st.write("Reps précédents:", reps_data)
            
            set_count = st.session_state.get(f"{exercise}_sets", default_sets)
            
            for i in range(set_count):
                st.text(f"Set {i+1}")
                col1, col2, col3 = st.columns([1,1,2])
                with col1:
                    reps_value = st.number_input(f"Repetitions (Set {i+1})", value=reps, min_value=1, step=1, key=f"freakmode_{exercise}_reps_{i+1}")
                with col2:
                    weight = st.number_input(f"Poids (Set {i+1} kg)", min_value=0.0, step=1.0, key=f"freakmode_{exercise}_weight_{i+1}")
                with col3:
                    if st.button(f"Enregistrer Set {i+1}", key=f"save_{exercise}_set_{i+1}"):
                        save_weights_reps(exercise, i+1, weight, reps_value)

                if i < set_count - 1 and rest:
                    if st.button(f"Start Countdown Timer after Set {i+1} for {exercise}", key=f"timer_freakmode_{exercise}_set_{i+1}"):
                        countdown_timer()
        
            if st.button(f"Ajouter un set supplémentaire pour {exercise}", key=f"add_set_{exercise}"):
                st.session_state[f"{exercise}_sets"] = set_count + 1


def freakmode_day2():
    st.title("Back/Biceps")
    
    exercises = [
        ("TBS Chin UP WarmUp", 2, 5, 1),
        ("TBS Chin Up", 4, 8, 1),
        ("Barbell bent-over row", 3, 8, 1),
        ("Single arm dumbel row - right", 3, 8, 1),
        ("Single arm dumbel row - left", 3, 8, 1),
        ("Barbell curl", 3, 8, 1),
        ("Cross-body hammer curl", 3, 16, 1)
    ]
    
    date = st.date_input("Jour 2")
    
    for exercise, default_sets, reps, rest in exercises:
        with st.expander(exercise, expanded=False):
            st.header(exercise)
            
            # Load and display previous session data for the exercise
            weights = get_last_n_rows_for_exercise(exercise, default_sets, '\data\weight_tracking_data.csv')
            reps_data = get_last_n_rows_for_exercise(exercise, default_sets, '\data\reps_tracking_data.csv')
            st.write("Poids précédents:", weights)
            st.write("Reps précédents:", reps_data)
            
            set_count = st.session_state.get(f"{exercise}_sets", default_sets)
            
            for i in range(set_count):
                st.text(f"Set {i+1}")
                col1, col2, col3 = st.columns([1,1,2])
                with col1:
                    reps_value = st.number_input(f"Repetitions (Set {i+1})", value=reps, min_value=1, step=1, key=f"freakmode_{exercise}_reps_{i+1}")
                with col2:
                    weight = st.number_input(f"Poids (Set {i+1} kg)", min_value=0.0, step=1.0, key=f"freakmode_{exercise}_weight_{i+1}")
                with col3:
                    if st.button(f"Enregistrer Set {i+1}", key=f"save_{exercise}_set_{i+1}"):
                        save_weights_reps(exercise, i+1, weight, reps_value)

                if i < set_count - 1 and rest:
                    if st.button(f"Start Countdown Timer after Set {i+1} for {exercise}", key=f"timer_freakmode_{exercise}_set_{i+1}"):
                        countdown_timer()
        
            if st.button(f"Ajouter un set supplémentaire pour {exercise}", key=f"add_set_{exercise}"):
                st.session_state[f"{exercise}_sets"] = set_count + 1


def freakmode_day3():
    st.title("Legs")
    
    exercises = [
        ("Barbell back squat to box - WarmUP", 2, 10, 1),
        ("Barbell back squat to box", 5, 8, 1),
        ("Barbell stiff-legged deadlift", 3, 8, 1),
        ("Leg extension", 3, 8, 1),
        ("Leg curl", 3, 8, 1),
        ("Calf raise", 3, 25, 1)
    ]
    
    date = st.date_input("Jour 3")
    
    for exercise, default_sets, reps, rest in exercises:
        with st.expander(exercise, expanded=False):
            st.header(exercise)
            
            # Load and display previous session data for the exercise
            weights = get_last_n_rows_for_exercise(exercise, default_sets, '\data\weight_tracking_data.csv')
            reps_data = get_last_n_rows_for_exercise(exercise, default_sets, '\data\reps_tracking_data.csv')
            st.write("Poids précédents:", weights)
            st.write("Reps précédents:", reps_data)
            
            set_count = st.session_state.get(f"{exercise}_sets", default_sets)
            
            for i in range(set_count):
                st.text(f"Set {i+1}")
                col1, col2, col3 = st.columns([1,1,2])
                with col1:
                    reps_value = st.number_input(f"Repetitions (Set {i+1})", value=reps, min_value=1, step=1, key=f"freakmode_{exercise}_reps_{i+1}")
                with col2:
                    weight = st.number_input(f"Poids (Set {i+1} kg)", min_value=0.0, step=1.0, key=f"freakmode_{exercise}_weight_{i+1}")
                with col3:
                    if st.button(f"Enregistrer Set {i+1}", key=f"save_{exercise}_set_{i+1}"):
                        save_weights_reps(exercise, i+1, weight, reps_value)

                if i < set_count - 1 and rest:
                    if st.button(f"Start Countdown Timer after Set {i+1} for {exercise}", key=f"timer_freakmode_{exercise}_set_{i+1}"):
                        countdown_timer()
        
            if st.button(f"Ajouter un set supplémentaire pour {exercise}", key=f"add_set_{exercise}"):
                st.session_state[f"{exercise}_sets"] = set_count + 1

def freakmode_day4():
    st.title("Cardio")
    
    exercises = [
        ("Elbow plank", 3, 1),
        ("Side plank - right", 3, 1),
        ("Side plank - left", 3, 1),
        ("Crunch", 3, 1)
    ]
    
    date = st.date_input("Jour 4")
    
    for exercise, sets, time_minutes in exercises:
        with st.expander(exercise, expanded=False):
            st.header(exercise)
            st.write(f"Sets: {sets}")
            st.write(f"Time (in minutes): {time_minutes}")


def save_weights_reps(exercise, set_number, weight, reps):
    '''Save the weights and reps to CSV files.'''
    # Load existing data or create new DataFrame if not exists
    weights_df = load_from_csv('\data\weight_tracking_data.csv')
    reps_df = load_from_csv('\data\reps_tracking_data.csv')

    # Check if the exercise column exists in the DataFrame, if not create it
    if exercise not in weights_df.columns:
        weights_df[exercise] = None
    if exercise not in reps_df.columns:
        reps_df[exercise] = None

    # Find the last non-empty row for the specific exercise/column
    last_non_empty_weight_row = weights_df[exercise].last_valid_index()
    last_non_empty_reps_row = reps_df[exercise].last_valid_index()

    # Append new data to the next row of the last non-empty row
    weights_df.loc[last_non_empty_weight_row + 1 if pd.notna(last_non_empty_weight_row) else 0, exercise] = weight
    reps_df.loc[last_non_empty_reps_row + 1 if pd.notna(last_non_empty_reps_row) else 0, exercise] = reps

    # Save back to CSV
    save_to_csv(weights_df, '\data\weight_tracking_data.csv')
    save_to_csv(reps_df, '\data\reps_tracking_data.csv')




def show():
    st.sidebar.title("Workouts")
    selected_plan = st.sidebar.radio("", ["Chest/Shoulders/Triceps", "Back/Biceps","Legs", "Cardio"])
    
    if selected_plan == "Chest/Shoulders/Triceps":
        freakmode_day1()
    elif selected_plan == "Back/Biceps":
        freakmode_day2()
    elif selected_plan == "Legs":
        freakmode_day3()

    elif selected_plan == "Cardio":
        freakmode_day4()
    else:
        pass
