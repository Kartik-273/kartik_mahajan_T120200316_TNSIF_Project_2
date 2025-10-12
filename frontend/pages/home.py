import streamlit as st
from backend.model_utils import predict, get_model

def render():
    st.title("⚙️ Manufacturing Parts Per Hour Predictor")
    st.write("Enter machine and process parameters below to predict productivity.")

    # Load feature list dynamically
    _, _, _, feature_columns, target_name = get_model()

    # Create form with numeric fields
    user_input = {}
    with st.form("prediction_form"):
        for col in feature_columns:
            user_input[col] = st.number_input(f"{col}", value=0.0, step=0.1)
        submitted = st.form_submit_button("Predict")

    if submitted:
        with st.spinner("Predicting..."):
            prediction = predict(user_input)
        st.success(f"✅ Predicted **{target_name}**: {prediction:.2f}")
