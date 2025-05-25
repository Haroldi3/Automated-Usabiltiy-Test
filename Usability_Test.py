import streamlit as st
import pandas as pd
import time
import os

# Create a folder called data in the main project folder
DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Define CSV file paths for each part of the usability testing
CONSENT_CSV = os.path.join(DATA_FOLDER, "consent_data.csv")
DEMOGRAPHIC_CSV = os.path.join(DATA_FOLDER, "demographic_data.csv")
TASK_CSV = os.path.join(DATA_FOLDER, "task_data.csv")
EXIT_CSV = os.path.join(DATA_FOLDER, "exit_data.csv")


def save_to_csv(data_dict, csv_file):
    # Convert dict to DataFrame with a single row
    df_new = pd.DataFrame([data_dict])
    if not os.path.isfile(csv_file):
        # If CSV doesn't exist, write with headers
        df_new.to_csv(csv_file, mode='w', header=True, index=False)
    else:
        # Else, we need to append without writing the header!
        df_new.to_csv(csv_file, mode='a', header=False, index=False)


def load_from_csv(csv_file):
    if os.path.isfile(csv_file):
        return pd.read_csv(csv_file)
    else:
        return pd.DataFrame()


def main():
    st.title("Usability Testing Tool")

    home, consent, demographics, tasks, exit, report = st.tabs(
        ["Home", "Consent", "Demographics", "Task", "Exit Questionnaire", "Report"])

    with home:
        st.header("Introduction")
        st.write("""
        Welcome to the Usability Testing Tool for HCI.

        In this app, you will:
        1. Provide consent for data collection.
        2. Fill out a short demographic questionnaire.
        3. Perform a specific task (or tasks).
        4. Answer an exit questionnaire about your experience.
        5. View a summary report (for demonstration purposes).
        """)

    with consent:
        st.header("Consent Form")

        # TODO: Create your consent form and a variable called consent_given
        st.write("Today you will be reviewing the usability of Apple.com, to assess how user-freindly the system is.",
                 "This information will be used solely for academic purposes related to the Automated Usability Testing Project. ")
        consent_given = st.checkbox("I agree to participate in this Automating Usability Test.")

        if st.button("Submit Consent"):
            if not consent_given:
                st.warning("You must agree to the consent terms before proceeding.")
            else:
                # Save the consent acceptance time
                data_dict = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "consent_given": consent_given
                }
                save_to_csv(data_dict, CONSENT_CSV)

    with demographics:
        st.header("Demographic Questionnaire")

        with st.form("demographic_form"):
            # TODO: Create the demographic form
            # Create a demographic form (Containing: Name/Age/Occupation/Familiarity/ and a Submit button)
            name = st.text_input("Enter your name")
            age = st.number_input("Enter your age",
                                  step = 1, format = "%d" )
            education = st.selectbox("What is your highest level of education completed?",[
                 "High school",
                 "Some College",
                "Associate degree",
                "Bachelor's degree",
                "Master's degree",
                "Doctor's degree",
                "Other"
            ]  )
            occupation = st.text_input("Enter your occupation")
            familiarity = st.selectbox("What is your familiarity with using a usability test?",
                                       ["None","Beginner","Intermediate","Advanced"])
            submitted = st.form_submit_button("Submit Demographics")
            if submitted:
                data_dict = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "name": name,
                    "age": age,
                    "occupation": occupation,
                    "familiarity": familiarity
                }
                save_to_csv(data_dict, DEMOGRAPHIC_CSV)

    with tasks:
        st.header("Task Page")

        st.write("Please select a task and record your experience completing it.")

        # For this template, we assume there's only one task, in project 3, we will have to include the actual tasks
        # Just placeholders until Project #3
        selected_task = st.selectbox("Select Task", [
            "Task 1: Compare two iPhone Models",
            "Task 2: Find and compare MacBook options",
            "Task 3: Locate AppleCare details for iPhones",
            "Task 4: Find product details for AirPods",
        ])
        compare_result = ""
        compare_macbook = ""
        apple_care_details = ""
        airpod_details = ""
        if selected_task == "Task 1: Compare two iPhone Models":
            st.write("Start timer before beginning the task")
            st.write("""
            Visit [apple.com/iphone](https://apple.com/iPhone/) and compare two iPhone Models.
              Describe a difference that surprised you the most (camera, battery life, processor,...).
              """)
            compare_result = st.text_area("Difference between iPhones: ")
        elif selected_task == "Task 2: Find and compare MacBook options":
            st.write("Start timer before beginning the task")
            st.write("""
            Visit [apple.com/macbook](https://apple.com/macbook/) and compare a MacBook pro to a Macbook Air.
            What is the difference between a MacBook Pro and Macbook Air?
            """)
            compare_macbook = st.text_area("Compare MacBooks")

        elif selected_task == "Task 3: Locate AppleCare details for iPhones":
            st.write("Start timer before beginning the task")
            st.write("""
            Locate AppleCare on [apple.com](https://apple.com) and research coverage options for the new iPhone.
            What's the monthly subscription or one-time payment?
            """)
            apple_care_details = st.text_area("Apple Care Details:")

        elif selected_task == "Task 4: Find product details for AirPods":
            st.write("Start timer before beginning the task")
            st.write("""
            Visit [apple.com/airpods](https://apple.com/airpods-pro) and find the battery life of the new AirPod Pros.
            Whats the battery life of the new AirPod Pro?
            """)
            airpod_details = st.text_area("AirPod Battery Life:")
            
            
            
            
        st.write("Task Description: Perform the example task in our system")

        # Track success, completion time, etc.
        start_button = st.button("Start Task Timer")
        if start_button:
            st.session_state["start_time"] = time.time()

        stop_button = st.button("Stop Task Timer")
        if stop_button and "start_time" in st.session_state:
            duration = time.time() - st.session_state["start_time"]
            st.session_state["task_duration"] = duration

        success = st.radio("Was the task completed successfully?", ["Yes", "No", "Partial"])
        notes = st.text_area("Observer Notes")

        if st.button("Save Task Results"):
            duration_val = st.session_state.get("task_duration", None)

            data_dict = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "task_name": selected_task,
                "success": success,
                "duration_seconds": duration_val if duration_val else "",
                "notes": notes,
                "compare_result": compare_result,
                "compare_macbook": compare_macbook,
                "apple_care_details": apple_care_details,
                "airpod_details": airpod_details
            }
            save_to_csv(data_dict, TASK_CSV)

            # Reset any stored time in session_state if you'd like
            if "start_time" in st.session_state:
                del st.session_state["start_time"]
            if "task_duration" in st.session_state:
                del st.session_state["task_duration"]

    with exit:
        st.header("Exit Questionnaire")

        with st.form("exit_form"):
            # TODO: likert scale or other way to have an exit questionnaire
            #satisfaction slider (Contains: Statisfaction/Difficulty sliders)
            satisfaction = st.slider("Leave a rating on how satisfied you were with the usability test.",1,5)
            full_stars = "⭐️" * satisfaction
            st.write(f"Your satisfaction rating: {full_stars}")
            difficulty = st.slider("Rate the difficulty level of this usability test (1 = Very Easy, 5 = Very Hard).",1,5)
            difficulty_names={
                1: "Very Easy",
                2: "Easy",
                3: "Medium",
                4: "Hard",
                5: "Very Hard",
            }
            st.write(f"Difficulty Selected: {difficulty_names[difficulty]}")

            #Feedback (open text)
            open_feedback = st.text_area("Leave a feedback about this usability test (Ways we can improve).")
            recomendation = st.text_area("Would you recommend this usability test?")

            submitted_exit = st.form_submit_button("Submit Exit Questionnaire")
            if submitted_exit:
                data_dict = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "satisfaction": satisfaction,
                    "difficulty": difficulty,
                    "open_feedback": open_feedback,
                    "recomendation": recomendation
                }
                save_to_csv(data_dict, EXIT_CSV)
                st.success("Exit questionnaire data saved.")

    with report:
        st.header("Usability Report - Aggregated Results")

        st.write("**Consent Data**")
        consent_df = load_from_csv(CONSENT_CSV)
        if not consent_df.empty:
            st.dataframe(consent_df)
        else:
            st.info("No consent data available yet.")

        st.write("**Demographic Data**")
        demographic_df = load_from_csv(DEMOGRAPHIC_CSV)
        if not demographic_df.empty:
            st.dataframe(demographic_df)
        else:
            st.info("No demographic data available yet.")

        st.write("**Task Performance Data**")
        task_df = load_from_csv(TASK_CSV)
        if not task_df.empty:
            st.dataframe(task_df)
        else:
            st.info("No task data available yet.")

        st.write("**Exit Questionnaire Data**")
        exit_df = load_from_csv(EXIT_CSV)
        if not exit_df.empty:
            st.dataframe(exit_df)
        else:
            st.info("No exit questionnaire data available yet.")

        # Example of aggregated stats (for demonstration only)
        if not exit_df.empty:
            st.subheader("Exit Questionnaire Averages")
            avg_satisfaction = exit_df["satisfaction"].mean()
            avg_difficulty = exit_df["difficulty"].mean()
            st.write(f"**Average Satisfaction**: {avg_satisfaction:.2f}")
            st.write(f"**Average Difficulty**: {avg_difficulty:.2f}")


if __name__ == "__main__":
    main()