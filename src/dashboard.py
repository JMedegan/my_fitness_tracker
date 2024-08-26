
import streamlit as st
from database import get_last_n_rows_for_exercise

def show():
    st.title("Dashboard")
    st.write("Bienvenue sur votre tableau de bord d'entraînement!")
    st.write("Ici, vous verrez des statistiques clés sur vos entraînements, ainsi que des graphiques montrant votre progression.")
    # More visualizations and data presentation can be added here

def display_dashboard():
    st.title("Dashboard")
    
    # List of exercises
    exercises = [
        "Bench Press (Échauffement)",
        "Bench Press",
        "Dumbbell Chest Fly",
        "Incline Dumbbell Chest Fly",
        "Seated Dumbbell Shoulder Press",
        "Cable Straight Bar Pushdown",
        "Double Arm Triceps Kick-Back",
        "Dumbbell Front Raise",
        "Dumbbell Lateral Raise",
        "Seated Rear Delt Fly"
    ]
    
    for exercise in exercises:
        with st.expander(exercise, expanded=True):
            st.header(exercise)
            
            # Get the last two sessions data for weights and reps
            last_weights = get_last_n_rows_for_exercise(exercise, 2, '/data/weight_tracking_data.csv')
            last_reps = get_last_n_rows_for_exercise(exercise, 2, '/data/reps_tracking_data.csv')
            
            if last_weights and last_reps:
                for i, (weight, reps) in enumerate(zip(last_weights, last_reps)):
                    st.write(f"Session {i+1}: {weight} kg x {reps} reps")
            else:
                st.write("Pas de données disponibles pour cet exercice.")


