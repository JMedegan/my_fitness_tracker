
# Personal Fitness Tracker

This project is a **Streamlit application** designed to help users record and track their bodybuilding sessions. Whether it's weights lifted or repetitions performed, the app provides an intuitive interface to log workouts, monitor progress, and avoid plateaus often encountered by fitness enthusiasts. 

All workout data, including weights and repetitions, are securely saved in a Google Sheets file for easy access and further analysis.

The application is deployed and accessible online at: [My Personal Fitness Tracker](https://my-personal-fitnesstracker.streamlit.app)

---

## Features
- **Track Workouts:** Log weights and repetitions for each exercise in your bodybuilding routine.
- **Monitor Progress:** Visualize your performance trends over time with interactive charts.
- **Cloud Storage:** Automatically saves data to a connected Google Sheets file for secure, persistent storage.
- **Customizable:** Easily adapt the app to suit your own workout goals and data tracking preferences.

---

## Installation

Follow these steps to install and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JMedegan/my_fitness_tracker.git
   ```

2. **Install the dependencies**:
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**:
   Launch the app in your browser using the following command:
   ```bash
   streamlit run src/app_main.py
   ```

---

## Customization

You can easily adapt this project to suit your own needs:

1. **Clone and rename the repository**:
   Modify the project to reflect your personal requirements.

2. **Set up your own Google Sheet**:
   Create a new Google Sheets file to store your workout data. Update the connection settings in the app to point to your Google Sheet.

3. **Enhance the application**:
   Add features like:
   - New workout plans or exercises.
   - Advanced visualizations.

---

## Bug Reports and Contributions

### Found a bug?
If you encounter an issue or have an idea for improvement, please use the **Issues** tab on GitHub to submit a report. Provide as much detail as possible to help me address the problem.

### Want to contribute?
Contributions are welcome! Feel free to fork the repository, make your changes, and submit a **Pull Request** referencing the related issue.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

### Acknowledgements
- Built using [Streamlit](https://streamlit.io/) for a seamless web-based interface.
- Data storage powered by Google Sheets.
