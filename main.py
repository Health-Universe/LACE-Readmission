import streamlit as st
import pandas as pd

def predict_readmission(length_of_stay, acuity, comorbidity, ed_visits):
    """
    Function to calculate the LACE score to predict likelihood of readmission.
    """
    # Calculate Length of stay score
    if length_of_stay <= 4:
        los_score = 0
    elif 4 < length_of_stay <= 6:
        los_score = 2
    elif 6 < length_of_stay <= 13:
        los_score = 3
    else:
        los_score = 4

    # Acuity score is provided as an argument (either 1 or 3)
    
    # Comorbidity score is directly taken from the Charlson Comorbidity Index (0-4)
    
    # Calculate ED visits score
    if ed_visits == 0:
        ed_score = 0
    elif 0 < ed_visits < 4:
        ed_score = 1
    else:
        ed_score = 2

    lace_score = los_score + acuity + comorbidity + ed_score
    return lace_score

st.title("30-Day Readmission Prediction using LACE Index")

st.write("Predict the likelihood of a 30-day readmission to the hospital using the LACE Index.")

# Collect data from the user
length_of_stay = st.number_input("Enter length of stay (in days)", min_value=0, max_value=365)
acuity = st.selectbox("Select the acuity of the admission", [1, 3], index=1, help="Non-urgent = 1, Urgent = 3")
comorbidity = st.slider("Comorbidity score (Charlson Comorbidity Index)", 0, 4, 2)
ed_visits = st.number_input("Enter number of ED visits in the last 6 months", min_value=0, max_value=10)

if st.button("Predict"):
    lace_score = predict_readmission(length_of_stay, acuity, comorbidity, ed_visits)
    st.write(f"LACE Score: {lace_score}")

    if lace_score <= 4:
        st.write("Risk Level: Low risk")
    elif 4 < lace_score <= 9:
        st.write("Risk Level: Moderate risk")
    elif 9 < lace_score <= 14:
        st.write("Risk Level: High risk")
    else:
        st.write("Risk Level: Very high risk")
