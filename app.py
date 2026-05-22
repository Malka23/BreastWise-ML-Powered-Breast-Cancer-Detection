# app.py

import streamlit as st
import numpy as np
from model import load_model_and_scaler
from utils import collect_user_input

# Load trained model and scaler
model, scaler, feature_names, means = load_model_and_scaler()

# UI
st.title("Breastwise: ML-Powered Breast Cancer Detection")
st.markdown("""
Enter the tumor characteristics below. The model will predict whether the tumor is **Benign** or **Malignant**.
""")

# Get input
user_input = collect_user_input(feature_names, means)

# Predict
if st.button("Predict"):
    input_np = np.array(user_input).reshape(1, -1)
    input_scaled = scaler.transform(input_np)
    prediction = model.predict(input_scaled)
    result = "Malignant" if prediction[0] == 0 else "Benign"
    st.success(f"The predicted tumor type is: **{result}**")
