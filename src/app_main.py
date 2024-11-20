import streamlit as st
import workouts


# Configuration
st.set_page_config(
    page_title="Fitness Tracker", layout="wide", initial_sidebar_state="expanded"
)


def main() -> None:
    """
    Main function to run the Interactive Fitness Tracker application.

    This function sets up the sidebar with a description of the app and
    initializes the main workout tracking functionality.

    Features:
    - Sidebar description and branding.
    - Displays workout tracking and visualization functionality via `workouts.show()`.

    Returns:
        None: The function runs the Streamlit app interface.
    """
    # Sidebar Setup
    st.sidebar.markdown("## 🏋️ Fitness Tracker", unsafe_allow_html=True)
    st.sidebar.markdown(
        "The Interactive Fitness Tracker is a user-friendly tool designed to help you "
        "visualize and analyze the evolution of your workout metrics over time."
    )
    st.sidebar.markdown("---")

    # Main Content
    workouts.show()


# Run the app
if __name__ == "__main__":
    main()
