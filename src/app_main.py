import streamlit as st
import workouts

# Configuration
st.set_page_config(
    page_title="Fitness Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles
SIDEBAR_STYLE = {
    "background-color": "#f7f7f7",
    "border": "1px solid #e0e0e0",
    "padding": "10px"
}
HEADER_STYLE = {
    "font-weight": "bold",
    "font-size": "24px",
    "margin-bottom": "15px",
    "color": "#30475e"
}

# Main Function
def main():
    st.sidebar.markdown("## 🏋️ Fitness Tracker", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.sidebar.markdown("🏠 [Accueil](#)")
    st.sidebar.markdown("➕ [Ajouter un entraînement](#add_workout)")
    st.sidebar.markdown("📅 [Historique](#history)")
    st.sidebar.markdown("👤 [Profil](#profile)")
    st.sidebar.markdown("---")
    st.sidebar.markdown("---")
    workouts.show()

if __name__ == '__main__':
    main()
