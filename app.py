import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model


# =========================
# Load Model & Preprocessing
# =========================

model = load_model("diabetes_model.h5")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")


# =========================
# Page
# =========================

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="",
    layout="centered"
)

st.title("🩺 Diabetes Prediction")
st.write("Enter the patient's information below.")


# =========================
# Input Fields
# =========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=3,
        max_value=120,
        value=30
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=120.0,
        value=25.0
    )

    hba1c = st.number_input(
        "HbA1c Level",
        min_value=3.0,
        max_value=20.0,
        value=5.5
    )


with col2:

    race = st.selectbox(
        "Race",
        [
            "AfricanAmerican",
            "Asian",
            "Caucasian",
            "Hispanic",
            "Other"
        ]
    )

    hypertension = st.selectbox(
        "Hypertension",
        [0, 1]
    )

    heart_disease = st.selectbox(
        "Heart Disease",
        [0, 1]
    )

    glucose = st.number_input(
        "Blood Glucose",
        min_value=40.0,
        max_value=500.0,
        value=100.0
    )

    smoking = st.selectbox(
        "Smoking History",
        [
            "current",
            "ever",
            "former",
            "never",
            "not current"
        ]
    )


# =========================
# Prediction
# =========================

if st.button("Predict", use_container_width=True):

    # Create input dictionary
    data = {
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "bmi": bmi,
        "hbA1c_level": hba1c,
        "blood_glucose_level": glucose,
        "smoking_history": smoking
    }

    df = pd.DataFrame([data])


    # =========================
    # Encode Gender
    # =========================

    df["gender"] = df["gender"].map({
        "Male": 1,
        "Female": 0
    })


    # =========================
    # Encode Smoking History
    # =========================

    df = pd.get_dummies(
        df,
        columns=["smoking_history"],
        drop_first=True,
        dtype=int
    )


    # =========================
    # Encode Race
    # =========================

    race_columns = [
        "race:AfricanAmerican",
        "race:Asian",
        "race:Caucasian",
        "race:Hispanic",
        "race:Other"
    ]

    for col in race_columns:
        df[col] = 0

    df[f"race:{race}"] = 1


    # =========================
    # Match Training Features
    # =========================

    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )


    # =========================
    # Scaling
    # =========================

    X = scaler.transform(df)


    # =========================
    # Prediction
    # =========================

    prediction = model.predict(X, verbose=0)

    prob = float(prediction[0][0])


    # =========================
    # Result
    # =========================

    st.subheader("Prediction Result")

    if prob >= 0.5:

        st.error(" Diabetes Detected")

    else:

        st.success("No Diabetes")


    st.write(
        f"Prediction Probability: **{prob:.2%}**"
    )