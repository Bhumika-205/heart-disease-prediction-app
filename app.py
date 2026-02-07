import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("heart_disease_model.pkl")  # Change this to your actual model file

st.title("💓 Heart Disease Predictor")
st.markdown("### Enter the patient's data below:")

# Create 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 1, 120, help="Enter the patient's age")
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, help="In mm Hg")
    chol = st.number_input("Serum Cholesterol", 100, 600, help="In mg/dl")
    restecg = st.selectbox("Resting ECG", [0, 1, 2], help="0: Normal, 1: ST-T abnormality, 2: LVH")

with col2:
    sex = st.selectbox("Sex", [0, 1], help="0: Female, 1: Male")
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1], help="1: True, 0: False")
    thalach = st.number_input("Max Heart Rate", 60, 220, help="Maximum heart rate achieved")
    exang = st.selectbox("Exercise Induced Angina", [0, 1], help="1: Yes, 0: No")

with col3:
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], help="0: Typical angina, 1: Atypical, 2: Non-anginal, 3: Asymptomatic")
    oldpeak = st.number_input("Oldpeak", 0.0, 6.0, step=0.1, help="ST depression induced by exercise")
    slope = st.selectbox("Slope", [0, 1, 2], help="0: Upsloping, 1: Flat, 2: Downsloping")
    ca = st.selectbox("CA (Number of vessels)", [0, 1, 2, 3, 4], help="Number of major vessels (0-4)")
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3], help="0: Unknown, 1: Normal, 2: Fixed defect, 3: Reversible defect")

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The patient **may have** heart disease.")
    else:
        st.success("✅ The patient **is unlikely** to have heart disease.")