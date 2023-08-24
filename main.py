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

# Description
st.write("""
## Description
The LACE Index helps healthcare professionals identify patients who are at high risk for readmission 
or death within 30 days of discharge. 

By assessing Length of stay, Acuity of the admission, Comorbidity, and Emergency department visits, 
this tool provides a risk score to guide post-discharge care.
""")

# Benefits
st.write("""
## Benefits to Value-Based Care Organizations
1. **Improved Patient Outcomes:** Early identification of high-risk patients can lead to better post-discharge care.
2. **Resource Allocation:** Allocate resources more efficiently by focusing on high-risk patients.
3. **Financial Savings:** Preventing readmissions can lead to significant savings under value-based care reimbursement models.
4. **Enhanced Patient Experience:** Reducing readmissions can lead to higher patient satisfaction scores.
""")

# Usage Instructions
st.write("""
## How to Use
1. Fill in the required fields: length of stay, acuity of admission, comorbidity score, and ED visits.
2. Click on the "Predict" button.
3. The app will display the LACE score and associated risk level for a 30-day readmission.
""")

# Data Input Section
st.write("## Data Input")
with st.expander("Provide Patient Details"):
    length_of_stay = st.number_input("Enter length of stay (in days)", min_value=0, max_value=365)
    acuity = st.selectbox("Select the acuity of the admission", [1, 3], index=1, help="Non-urgent = 1, Urgent = 3")
    comorbidity = st.slider("Comorbidity score (Charlson Comorbidity Index)", 0, 4, 2)
    ed_visits = st.number_input("Enter number of ED visits in the last 6 months", min_value=0, max_value=10)

# Prediction Section
if st.button("Predict"):
    lace_score = predict_readmission(length_of_stay, acuity, comorbidity, ed_visits)
    st.write(f"## LACE Score: {lace_score}")

    if lace_score <= 4:
        st.success("Risk Level: Low risk")
    elif 4 < lace_score <= 9:
        st.warning("Risk Level: Moderate risk")
    elif 9 < lace_score <= 14:
        st.error("Risk Level: High risk")
    else:
        st.error("Risk Level: Very high risk")

# Footer
st.write("""
---
Created by Health Universe. For more information, please contact [hello@healthuniverse.com].
""")
