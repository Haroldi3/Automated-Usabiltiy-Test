# Automated Usability Testing Tool

This Streamlit app was created for a Human Computer Interaction Project. 
The goal for this project is to automate a usability test, using tasks, collecting data, and generating a summary report.

# Features
The app has 6 tabs
1. Home - Introducting the usability test.
2. Consent - Obtaining consent from users' to participate in the automated usability test.
3. Demographics - Collects Name, Age, Occupation, Education Level, and Familiarity with usaibility testing.
4. Task - Guides users through sample task with time tracking, a written response, and observational feedback.
5. Exit Questionnaire - Obtains satisfaction ratings and feedback.
6. Report - Displays all collected data.

# Data Storage
All user inputs are saved into CSV Files inside a '/data' folder
- 'consent_data.csv'
- 'demographic_data.csv'
- 'task_data.csv'
- 'exit_data.csv'

# How to Run the App
1. Copy and paste:
   bash
   git clone https://github.com/Haroldi3/automated-usability-test.git
   cd automated-usability-test

2. Install streamlit
   pip install streamlit pandas

3. Run the app
   streamlit run usability_test.py

Author
Harold David Inirio
Bachelor's of Art in Computer Science
Florida International University
