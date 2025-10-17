import streamlit as st
import sys, os

# === Add backend folder to Python path ===
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
sys.path.append(backend_path)

from main_backend import predict_heart_disease

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("💓 Heart Disease Prediction App")
st.write("Enter the patient details below:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 20, 100, 45)
    sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
    chest_pain_type = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [1, 0])

with col2:
    resting_ecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])
    max_heart_rate = st.number_input("Max Heart Rate Achieved", 70, 210, 150)
    exercise_induced_angina = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [1, 0])
    st_depression = st.number_input("ST Depression", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope (0–2)", [0, 1, 2])
    num_major_vessels = st.selectbox("Num Major Vessels (0–3)", [0, 1, 2, 3])
    thalassemia = st.selectbox("Thalassemia (1–3)", [1, 2, 3])

if st.button("🔍 Predict"):
    input_data = {
        'age': age,
        'sex': sex,
        'chest_pain_type': chest_pain_type,
        'resting_blood_pressure': resting_blood_pressure,
        'cholesterol': cholesterol,
        'fasting_blood_sugar': fasting_blood_sugar,
        'resting_ecg': resting_ecg,
        'max_heart_rate': max_heart_rate,
        'exercise_induced_angina': exercise_induced_angina,
        'st_depression': st_depression,
        'st_slope': st_slope,
        'num_major_vessels': num_major_vessels,
        'thalassemia': thalassemia
    }

    result = predict_heart_disease(input_data)
    st.markdown("---")
    if result >= 0.5:
        st.error("🚨 High risk of heart disease.")
    else:
        st.success("✅ Low risk of heart disease.")
