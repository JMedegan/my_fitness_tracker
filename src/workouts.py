import streamlit as st
import os
import pandas as pd
from database import get_last_n_rows_for_exercise, save_weights_reps
import plotly.express as px
import time


def countdown_timer(duration: int = 60) -> None:
    """
    Function to provide a countdown timer for the rest period.

    Args:
        duration (int): The countdown duration in seconds. Default is 60 seconds.

    Returns:
        None: Displays a countdown timer and a success message when time's up.
    """
    placeholder = st.empty()  # Placeholder for dynamic updates
    for secs in range(duration, 0, -1):
        minutes, seconds = divmod(secs, 60)  # Convert seconds to minutes and seconds
        placeholder.metric("Rest Period", f"{minutes:02d}:{seconds:02d}")
        time.sleep(1)
    placeholder.empty()  # Clear the countdown display
    st.success("Time's up! Get ready for your next set!")


def plot_evolution(df: pd.DataFrame, column: str):
    """
    Creates an interactive and aesthetic line plot of the specified column over time.

    Args:
        df (pd.DataFrame): Data containing the date and column to plot.
        column (str): The column name to plot against Date.

    Returns:
        plotly.graph_objects.Figure: A Plotly figure showing the evolution of the specified column over time.
    """
    fig = px.line(
        df,
        x="Date",
        y=column,
        title=f"Evolution of {column.capitalize()} Over Time",
        labels={"Date": "Date", column: column.capitalize()},
        markers=True,
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        template="plotly_white",
        title_x=0.3,  # Center the title
        legend_title=None,
    )
    return fig


def render_exercise_section(
    exercise: str, default_sets: int, reps: int, rest: int
) -> None:
    """
    Render the interactive section for a specific exercise.

    Args:
        exercise (str): The name of the exercise.
        default_sets (int): The default number of sets.
        reps (int): The default number of repetitions.
        rest (int): Rest period between sets in seconds.

    Returns:
        None
    """
    with st.expander(exercise, expanded=False):
        st.header(exercise)

        # Load and display previous session data for the exercise
        existing_data = get_last_n_rows_for_exercise(exercise)
        weight_evolution = plot_evolution(existing_data, column="weight")
        reps_evolution = plot_evolution(existing_data, column="reps")

        # Display the charts side by side using Streamlit columns
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(weight_evolution, use_container_width=True)

        with col2:
            st.plotly_chart(reps_evolution, use_container_width=True)

        # Get the set count for the exercise
        set_count = st.session_state.get(f"{exercise}_sets", default_sets)

        # Input and save for each set
        for i in range(set_count):
            st.text(f"Set {i+1}")
            col1, col2 = st.columns(2)
            with col1:
                reps_value = st.number_input(
                    f"Reps (Set {i+1})",
                    value=reps,
                    min_value=2,
                    step=2,
                    key=f"freakmode_{exercise}_reps_{i+1}",
                )
            with col2:
                weight = st.number_input(
                    f"Weight (kg)",
                    min_value=10,
                    step=2,
                    key=f"freakmode_{exercise}_weight_{i+1}",
                )

            # Save set data and trigger countdown
            if st.button(f"Save Set {i+1}", key=f"save_{exercise}_set_{i+1}"):
                save_weights_reps(exercise, i + 1, weight, reps_value)
                countdown_timer()


def freakmode_day(title: str, exercises: list, day_label: str) -> None:
    """
    Generalized function to render a workout day.

    Args:
        title (str): Title of the workout day (e.g., "Chest/Shoulders/Triceps").
        exercises (list): List of exercises with their parameters.
        day_label (str): Label for the day (e.g., "Day 1").

    Returns:
        None
    """
    st.title(title)
    date = st.date_input(day_label)

    for exercise, default_sets, reps, rest in exercises:
        render_exercise_section(exercise, default_sets, reps, rest)


def freakmode_day1() -> None:
    """
    Render the workout plan for Freakmode Day 1: Chest/Shoulders/Triceps.
    """
    exercises_day1 = [
        ("Warm Up Bench Press", 2, 10, 1),
        ("Bench Press", 5, 8, 1),
        ("Dumbbell Chest Fly", 3, 8, 1),
        ("Incline Dumbbell Chest Fly", 2, 10, 1),
        ("Seated Dumbbell Shoulder Press", 4, 8, 1),
        ("Dumbbell Front Raise", 3, 7, 0),
        ("Dumbbell Lateral Raise", 3, 7, 0),
        ("Seated Rear Delt Fly", 3, 7, 1),
        ("Cable Straight Bar Pushdown", 3, 8, 1),
        ("Double Arm Triceps Kick-Back", 3, 8, 1),
    ]
    freakmode_day("Chest/Shoulders/Triceps", exercises_day1, "Day 1")


def freakmode_day2() -> None:
    """
    Render the workout plan for Freakmode Day 2: Back/Biceps.
    """
    exercises_day2 = [
        ("TBS Chin UP WarmUp", 2, 5, 1),
        ("TBS Chin Up", 4, 8, 1),
        ("Barbell bent-over row", 3, 8, 1),
        ("Single arm dumbel row - right", 3, 8, 1),
        ("Single arm dumbel row - left", 3, 8, 1),
        ("Barbell curl", 3, 8, 1),
        ("Cross-body hammer curl", 3, 16, 1),
    ]
    freakmode_day("Back/Biceps", exercises_day2, "Day 2")


def freakmode_day3() -> None:
    """
    Render the workout plan for Freakmode Day 3: Legs.
    """
    exercises_day3 = [
        ("Barbell back squat to box - WarmUP", 2, 10, 1),
        ("Barbell back squat to box", 5, 8, 1),
        ("Barbell stiff-legged deadlift", 3, 8, 1),
        ("Leg extension", 3, 8, 1),
        ("Leg curl", 3, 8, 1),
        ("Calf raise", 3, 25, 1),
    ]
    freakmode_day("Legs", exercises_day3, "Day 3")


def freakmode_day4() -> None:
    """
    Render the workout plan for Freakmode Day 4: Cardio.

    This day focuses on core stability and endurance exercises.
    """
    st.title("Cardio")

    exercises = [
        ("Elbow plank", 3, 1),
        ("Side plank - right", 3, 1),
        ("Side plank - left", 3, 1),
        ("Crunch", 3, 1),
    ]

    date = st.date_input("Day 4")

    for exercise, sets, time_minutes in exercises:
        with st.expander(exercise, expanded=False):
            st.header(exercise)
            st.write(f"Sets: {sets}")
            st.write(f"Time (in minutes): {time_minutes}")


def show() -> None:
    """
    Display the workout plans in the sidebar and render the selected plan.

    Users can select a workout plan from the sidebar to view its details.
    """
    st.sidebar.title("Workouts")

    # List of available workout plans
    workout_plans = {
        "Chest/Shoulders/Triceps": freakmode_day1,
        "Back/Biceps": freakmode_day2,
        "Legs": freakmode_day3,
        "Cardio": freakmode_day4,
    }

    # Sidebar selection
    selected_plan = st.sidebar.radio(
        "Select a Workout Plan:", list(workout_plans.keys())
    )

    # Render the selected plan
    workout_function = workout_plans.get(selected_plan)
    if workout_function:
        workout_function()
