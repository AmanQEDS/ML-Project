import streamlit as st
import pandas as pd
import numpy as np

from source.Pipeline.predict_pipeline import CustomData, PredictPipeline

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    layout="centered"
)

st.title("🎓 Student Performance Predictor")
st.write("Fill in the details below to predict student performance.")

# -------------------------------
# Input form
# -------------------------------
with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["male", "female"])

    ethnicity = st.selectbox(
        "Race / Ethnicity",
        ["group A", "group B", "group C", "group D", "group E"]
    )

    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )

    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        ["none", "completed"]
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0.0,
        max_value=100.0,
        step=1.0
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0.0,
        max_value=100.0,
        step=1.0
    )

    submit = st.form_submit_button("Predict")

# -------------------------------
# Prediction
# -------------------------------
if submit:
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        st.write("📊 Input Data", pred_df)

        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        st.success(f"✅ Predicted Math Score: {result[0]}")

    except Exception as e:
        st.error("❌ An error occurred during prediction")
        st.exception(e)
        
