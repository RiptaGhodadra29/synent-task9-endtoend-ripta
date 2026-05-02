import streamlit as st
import pickle
import numpy as np

# Load model
import os
import pickle

# Get current file directory
current_dir = os.path.dirname(__file__)

# Go to models folder
model_path = os.path.join(current_dir, '..', 'models', 'student_model.pkl')

# Load model
model = pickle.load(open(model_path, 'rb'))

st.title("🎓 Student Performance Predictor")

st.write("Enter student details to predict total score")

# Inputs
study_hours = st.slider("Weekly Study Hours", 0, 40, 10)
attendance = st.slider("Attendance Percentage", 50, 100, 75)
participation = st.slider("Class Participation (0-10)", 0, 10, 5)

if st.button("Predict Score"):
    import pandas as pd

    input_data = pd.DataFrame({
        'weekly_self_study_hours': [study_hours],
        'attendance_percentage': [attendance],
        'class_participation': [participation]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Score: {prediction[0]:.2f}")